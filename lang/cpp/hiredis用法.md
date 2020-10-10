#### 一、下载源码编译

```
https://github.com/redis/hiredis
```

执行cmake，然后编译

```
cmake -G "MinGW Makefiles"
mingw32-make
```

#### 二、使用方式

```cpp
#include "hiredis/hiredis.h"

int main() {
    redisContext *conn;
    redisReply *reply;

    conn = redisConnect("127.0.0.1", 6379);
    if (conn == NULL || conn->err) {
        if (conn) {
            printf("Error: %s\n", conn->errstr);
            // handle error
        } else {
            printf("Can't allocate redis context\n");
        }
    }

    reply = (redisReply *)redisCommand(conn, "SET a 2");
    printf("set a result: %s\n", reply->str);
    freeReplyObject(reply);

    reply = (redisReply *)redisCommand(conn, "GET a");
    printf("get a result: %s\n", reply->str);
    freeReplyObject(reply);

    redisFree(conn);

    return 0;
}
```



