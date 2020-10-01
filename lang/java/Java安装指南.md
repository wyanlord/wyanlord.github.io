### 一、Java和maven下载地址

```
https://github.com/frekele/oracle-java/releases
http://maven.apache.org/download.cgi
```

### 二、Java配置信息

```
export JAVA_HOME=/opt/jdk1.8.0
export CLASSPATH=.:$JAVA_HOME/lib/dt.jar:$JAVA_HOME/lib/tools.jar
export PATH=$JAVA_HOME/bin:/opt/maven/bin
```

### 三、maven配置信息

```
<mirror>                                                                
    <id>alimaven</id>
    <name>aliyun maven</name>
    <url>http://maven.aliyun.com/nexus/content/groups/public/</url>
    <mirrorOf>*</mirrorOf>         
</mirror>
```

### 四、docker镜像

```
docker pull openjdk:8-jdk-alpine3.9
```

### 五、maven三方库搜索

```
https://mvnrepository.com
```

### 六、常用的三方库配置

1、必备的基础包

```xml
<!--https://www.jianshu.com/p/1886903ed14c-->
<!--https://mvnrepository.com/artifact/org.apache.commons/commons-lang3-->
<dependency>
    <groupId>org.apache.commons</groupId>
    <artifactId>commons-lang3</artifactId>
    <version>3.11</version>
</dependency>

<!--https://blog.csdn.net/sinat_34093604/article/details/79551924-->
<!--https://mvnrepository.com/artifact/org.apache.commons/commons-collections4-->
<dependency>
    <groupId>org.apache.commons</groupId>
    <artifactId>commons-collections4</artifactId>
    <version>4.4</version>
</dependency>

<!--https://mvnrepository.com/artifact/commons-beanutils/commons-beanutils-->
<dependency>
    <groupId>commons-beanutils</groupId>
    <artifactId>commons-beanutils</artifactId>
    <version>1.9.4</version>
</dependency>

<!--https://www.cnblogs.com/leeego-123/p/11393394.html-->
<!--https://mvnrepository.com/artifact/com.google.guava/guava-->
<dependency>
    <groupId>com.google.guava</groupId>
    <artifactId>guava</artifactId>
    <version>29.0-jre</version>
</dependency>

<!-- https://mvnrepository.com/artifact/org.projectlombok/lombok -->
<dependency>
    <groupId>org.projectlombok</groupId>
    <artifactId>lombok</artifactId>
    <version>1.18.12</version>
    <scope>provided</scope>
</dependency>

<!--https://blog.csdn.net/qq122516902/article/details/87259752-->
<!-- https://mvnrepository.com/artifact/org.mapstruct/mapstruct -->
<dependency>
    <groupId>org.mapstruct</groupId>
    <artifactId>mapstruct</artifactId>
    <version>1.3.1.Final</version>
</dependency>

<!-- https://mvnrepository.com/artifact/org.mapstruct/mapstruct-processor -->
<dependency>
    <groupId>org.mapstruct</groupId>
    <artifactId>mapstruct-processor</artifactId>
    <version>1.3.1.Final</version>
</dependency>

<!--https://www.cnblogs.com/guoguochong/p/12886303.html-->
<!-- https://mvnrepository.com/artifact/javax.validation/validation-api -->
<dependency>
    <groupId>javax.validation</groupId>
    <artifactId>validation-api</artifactId>
    <version>2.0.1.Final</version>
</dependency>

<!-- https://mvnrepository.com/artifact/cn.hutool/hutool-all -->
<dependency>
    <groupId>cn.hutool</groupId>
    <artifactId>hutool-all</artifactId>
    <version>5.4.2</version>
</dependency>


```

2、图形验证码

```xml
<!--https://github.com/whvcse/EasyCaptcha-->
<!--https://mvnrepository.com/artifact/com.github.whvcse/easy-captcha-->
<dependency>
  <groupId>com.github.whvcse</groupId>
  <artifactId>easy-captcha</artifactId>
  <version>1.6.2</version>
</dependency>
```

3、操作excel表格

```xml
<!--https://blog.csdn.net/vbirdbest/article/details/72870714-->
<!--https://mvnrepository.com/artifact/org.apache.poi/poi-->
<dependency>
    <groupId>org.apache.poi</groupId>
    <artifactId>poi</artifactId>
    <version>4.1.2</version>
</dependency>
```



----------------------

