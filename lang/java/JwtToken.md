# JwtToken



### 引入需要的maven包

```xml
        <dependency>
            <groupId>io.jsonwebtoken</groupId>
            <artifactId>jjwt-api</artifactId>
            <version>0.11.2</version>
        </dependency>
        <dependency>
            <groupId>io.jsonwebtoken</groupId>
            <artifactId>jjwt-impl</artifactId>
            <version>0.11.2</version>
        </dependency>
        <dependency>
            <groupId>io.jsonwebtoken</groupId>
            <artifactId>jjwt-jackson</artifactId>
            <version>0.11.2</version>
        </dependency>
```



### 封装jwtToken

```java
public class JwtToken {

    private static final String jwtKeySecret = "HiJuYuiIiUHoKiLpHtNuBtV6F3L1H4G8";
    private Key jwtKey = null;

    public JwtToken() {
        jwtKey = new SecretKeySpec(jwtKeySecret.getBytes(), SignatureAlgorithm.HS512.getJcaName());
    }

    public String generate(Long uid, String openId, Long seconds) {
        return Jwts.builder()
                .claim("uid", uid)
                .claim("openId", openId)
                .setExpiration(new Date(System.currentTimeMillis() + seconds * 1000))
                .signWith(jwtKey).compact();
    }

    public Claims verify(String token) {
        Jws<Claims> claimsJws = Jwts.parserBuilder()
                .setSigningKey(jwtKey)
                .build().parseClaimsJws(token);
        return claimsJws.getBody();
    }
}
```

