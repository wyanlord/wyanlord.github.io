### Redis配置信息

```java
package com.wyanlord.admin.infra.configure;

import com.fasterxml.jackson.annotation.JsonAutoDetect;
import com.fasterxml.jackson.annotation.PropertyAccessor;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.jsontype.impl.LaissezFaireSubTypeValidator;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.data.redis.connection.lettuce.LettuceConnectionFactory;
import org.springframework.data.redis.core.RedisTemplate;
import org.springframework.data.redis.serializer.Jackson2JsonRedisSerializer;
import org.springframework.data.redis.serializer.StringRedisSerializer;

@Configuration
public class RedisConfiguration {

    @Bean
    @SuppressWarnings({"rawtypes", "unchecked"})
    public <K, V> RedisTemplate<K, V> redisTemplate(LettuceConnectionFactory factory) {
        RedisTemplate<K, V> redisTemplate = new RedisTemplate<>();
        redisTemplate.setConnectionFactory(factory);

        // set key serializer
        StringRedisSerializer stringRedisSerializer = new StringRedisSerializer();
        redisTemplate.setKeySerializer(stringRedisSerializer);
        redisTemplate.setHashKeySerializer(stringRedisSerializer);

        // build jackson serializer
        Jackson2JsonRedisSerializer jackson2JsonRedisSerializer = new Jackson2JsonRedisSerializer(Object.class);

        ObjectMapper objectMapper = new ObjectMapper();
        objectMapper.setVisibility(PropertyAccessor.ALL, JsonAutoDetect.Visibility.ANY);
        objectMapper.activateDefaultTyping(LaissezFaireSubTypeValidator.instance, ObjectMapper.DefaultTyping.NON_FINAL);
        jackson2JsonRedisSerializer.setObjectMapper(objectMapper);

        // set value serializer
        redisTemplate.setValueSerializer(jackson2JsonRedisSerializer);
        redisTemplate.setHashValueSerializer(jackson2JsonRedisSerializer);

        redisTemplate.afterPropertiesSet();
        return redisTemplate;
    }

    @Bean
    public <K, V> RedisTemplate<K, V> redisBinaryTemplate(LettuceConnectionFactory factory) {
        RedisTemplate<K, V> redisTemplate = new RedisTemplate<>();
        redisTemplate.setConnectionFactory(factory);

        // set key serializer
        StringRedisSerializer stringRedisSerializer = new StringRedisSerializer();
        redisTemplate.setKeySerializer(stringRedisSerializer);
        redisTemplate.setHashKeySerializer(stringRedisSerializer);

        redisTemplate.afterPropertiesSet();
        return redisTemplate;
    }
}

```

### Redis缓存自定义

```java
package com.wyanlord.admin.infra.utility;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.data.redis.core.RedisTemplate;
import org.springframework.stereotype.Component;

import javax.annotation.Resource;
import java.util.concurrent.TimeUnit;

@Component
public class RedisCache<K, V> {

    @Value("${cache.prefix}")
    private String prefix;

    @Resource
    private RedisTemplate<String, V> redisTemplate;

    @Resource
    private RedisTemplate<String, V> redisBinaryTemplate;

    public V get(K k) {
        return redisTemplate.opsForValue().get(makeKey(k));
    }

    public V getWithBinary(K k) {
        return redisBinaryTemplate.opsForValue().get(makeKey(k));
    }

    public void set(K k, V v, Long timeout, TimeUnit timeUnit) {
        redisTemplate.opsForValue().set(makeKey(k), v, timeout, timeUnit);
    }

    public void setWithBinary(K k, V v, Long timeout, TimeUnit timeUnit) {
        redisBinaryTemplate.opsForValue().set(makeKey(k), v, timeout, timeUnit);
    }

    public Boolean setnx(K k, V v, Long timeout, TimeUnit timeUnit) {
        return redisTemplate.opsForValue().setIfAbsent(makeKey(k), v, timeout, timeUnit);
    }

    public void delete(K k) {
        redisTemplate.delete(makeKey(k));
    }

    public V remember(K k, Long timeout, TimeUnit timeUnit, RememberFunc<V> func) {
        V v = this.get(k);
        if (v == null) {
            v = func.execute();
            if (v != null) {
                this.set(k, v, timeout, timeUnit);
            }
        }
        return v;
    }

    public String makeKey(K k) {
        return prefix + k.toString();
    }

    public interface RememberFunc<V> {
        V execute();
    }
}

```

### Redis锁的问题

```java
package com.wyanlord.admin.infra.utility;

import java.util.HashMap;
import java.util.Map;
import java.util.UUID;
import java.util.concurrent.TimeUnit;

public class RedisLocker {
    private RedisCache<String, String> redisCache;

    private Map<String, String> lockers = new HashMap<>();

    public RedisLocker(RedisCache<String, String> redisCache) {
        this.redisCache = redisCache;
    }

    public boolean acquire(String k, Long timeout, TimeUnit timeUnit) {
        String lockValue = UUID.randomUUID() + ":" + System.nanoTime();

        Boolean bLocked = redisCache.setnx(k, lockValue, timeout, timeUnit);

        if (bLocked != null && bLocked.equals(true)) {
            lockers.put(k, lockValue);
            return true;
        } else {
            this.release();
            return false;
        }
    }

    public void release() {
        if (lockers.isEmpty()) {
            return;
        }

        for (Map.Entry<String, String> entry : lockers.entrySet()) {
            String lockValue = redisCache.get(entry.getKey());
            if (entry.getValue().equals(lockValue)) {
                redisCache.delete(entry.getKey());
            }
        }
    }
}

```

------

