### Json序列化的问题

```java
package com.wyanlord.admin.infra.utility;

import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.DeserializationFeature;
import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.SerializationFeature;
import lombok.extern.slf4j.Slf4j;

import java.text.SimpleDateFormat;

@Slf4j
public class JsonUtils {

    private static ObjectMapper om = new ObjectMapper();

    static {
        // 去掉null, 空字符串、空集合，以及isEmpty方法为true的，时间戳为0等等
        om.setSerializationInclusion(JsonInclude.Include.NON_EMPTY);

        // Bean上没有注解标识为可序列化，如get和set方法时，序列化为空对象，而不是报错
        om.configure(SerializationFeature.FAIL_ON_EMPTY_BEANS, false);

        // 没有属性或者set属性的方法，不报异常
        om.configure(DeserializationFeature.FAIL_ON_UNKNOWN_PROPERTIES, false);

        // 时间字段格式化为标准的时间格式
        om.configure(SerializationFeature.WRITE_DATES_AS_TIMESTAMPS, false);
        om.setDateFormat(new SimpleDateFormat("yyyy-MM-dd HH:mm:ss"));
    }

    /**
     * 将T类型的对象序列化为字符串
     * @param obj 可序列化的对象
     * @param <T> 可序列化的类型
     * @return String类型的返回值
     */
    public static <T> String toJson(T obj) {
        try{
            return om.writeValueAsString(obj);
        } catch (JsonProcessingException e) {
            log.error("json serialize exception: {}", e.getMessage(), e);
            throw new RuntimeException();
        }
    }

    /**
     * 将字符串反序列化为T对象
     * @param <T> 反序列化的目标类型
     * @param jsonStr 可反序列化的字符串
     * @return 返回T类型的对象
     */
    public static <T> T fromJson(String jsonStr, Class<T> valueType) {
        try {
            return om.readValue(jsonStr, valueType);
        } catch (JsonProcessingException e) {
            log.error("json deserialize exception: {}", e.getMessage(), e);
            throw new RuntimeException();
        }
    }

    /**
     * 将字符串解析为JsonNode
     * @param jsonStr 可反序列化的字符串
     * @return 返回JsonNode
     */
    public static JsonNode fromJson(String jsonStr) {
        try {
            return om.readTree(jsonStr);
        } catch (JsonProcessingException e) {
            log.error("json deserialize exception: {}", e.getMessage(), e);
            throw new RuntimeException();
        }
    }
}
```

------
