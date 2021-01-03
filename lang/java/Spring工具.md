# SpringBoot应用技巧

### 1.配置讲解

给配置类添加注解@Configuration



# 自定义RequestBody校验注解

##### 1、使用示例
```java
package com.wyanlord.demo1.controller.req;

import com.wyanlord.demo1.validator.CustomValidator;
import com.wyanlord.demo1.validator.CustomValidatorAware;
import lombok.Getter;
import lombok.Setter;
import lombok.ToString;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.validation.constraints.NotEmpty;
import java.io.Serializable;

@Setter
@Getter
@ToString
@CustomValidator
public class UserLoginReq implements Serializable, CustomValidatorAware {
    private static final long serialVersionUID = -1;

    @NotEmpty
    private String username;

    @NotEmpty
    private String password;

    private String captcha;

    @Override
    public boolean validate(HttpServletRequest request, HttpServletResponse response) {
        // TODO: custom validator
        System.out.println(request.getContentType());
        System.out.println(request.getRequestURI());
        return true;
    }
}
```

##### 2、声明注解
```java
package com.wyanlord.demo1.validator;

import javax.validation.Constraint;
import javax.validation.Payload;
import java.lang.annotation.*;

@Documented
@Target({ElementType.TYPE})
@Retention(RetentionPolicy.RUNTIME)
@Constraint( validatedBy = {CustomValidatorConstraint.class})
public @interface CustomValidator {

    String message() default "undefined message";

    Class<?>[] groups() default { };

    Class<? extends Payload>[] payload() default { };
}
```

##### 3、实现Constrait执行验证类
```java
package com.wyanlord.demo1.validator;

import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.ServletRequestAttributes;

import javax.validation.ConstraintValidator;
import javax.validation.ConstraintValidatorContext;

public class CustomValidatorConstraint implements ConstraintValidator<CustomValidator, Object> {

    @Override
    public boolean isValid(Object obj, ConstraintValidatorContext context) {
        if (!(obj instanceof CustomValidatorAware)) {
            throw new RuntimeException("Require implementing CustomValidatorAware");
        }

        ServletRequestAttributes attributes = (ServletRequestAttributes)RequestContextHolder.getRequestAttributes();
        if (attributes == null) {
            throw new RuntimeException("Current application is not a web application");
        }

        return ((CustomValidatorAware) obj).validate(attributes.getRequest(), attributes.getResponse());
    }
}
```

##### 4、声明一个接口，让requestBody实体实现validate方法
```java
package com.wyanlord.demo1.validator;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

public interface CustomValidatorAware {
    boolean validate(HttpServletRequest request, HttpServletResponse response);
}
```