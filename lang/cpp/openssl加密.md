### 1、MD5加密

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <openssl/md5.h>

char *md5(char *data);

int main() {
    char str[] = "123456";
    char *md5_res = md5(str);
    printf("%s", md5_res);
    free(md5_res);
    return 0;
}

char *md5(char *data) {
    unsigned char md5_data[16] = {0};

    MD5_CTX md5_ctx;
    MD5_Init(&md5_ctx);
    MD5_Update(&md5_ctx, data, strlen(data));
    MD5_Final(md5_data, &md5_ctx);

    char *result = (char *)malloc(sizeof(char) * (32 + 1));
    memset(result, 0, 33);

    char ch[2];
    for (int i = 0; i < 16; ++i) {
        sprintf(ch, "%02X", md5_data[i]);
        strncat(result, ch, 2);
    }

    return result;
}
```

