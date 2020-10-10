#### 一、iconv编译

下载地址

```
https://www.gnu.org/software/libiconv
```

修改lib目录下的relocatable.c，随便写一个目录

```
const char *orig_installdir = "/usr/local/libiconv";
```

将默认的mingw32-make.exe拷贝一份为make.exe

```
./configure && make && make install
```

在Git目录下就能找到编译好的文件

```
D:\AppData\Git\usr\local
```

#### 二、使用示例

CMakelists.txt如下

```
cmake_minimum_required(VERSION 3.15)
project(demo1)

set(CMAKE_CXX_STANDARD 11)

set(OPT_DIR C:/Qt/Qt5.14.2/Tools/mingw730_64/opt)

include_directories(${OPT_DIR}/include)
link_directories(${OPT_DIR}/lib)

set(LIBS iconv charset)

aux_source_directory(. SOURCE_FILES)
add_executable(${PROJECT_NAME} ${SOURCE_FILES})
target_link_libraries(${PROJECT_NAME} ${LIBS})
```

main文件如下

```
#include <cstdio>
#include <iconv.h>
#include <cstring>

bool convert(const char *from, const char *to, char *in, size_t *inLen, char *out, size_t *outLen) {
    iconv_t hIcv;
    size_t iRet = -1;

    if ((hIcv = iconv_open(to, from)) != NULL) {
        iRet = iconv(hIcv, &in, inLen, &out, outLen);
        iconv_close(hIcv);
    }

    return iRet >= 0;
}

int main() {
    char out[16] = {0};
    char in[] = u8"中国人";
    size_t outLen = sizeof(out);
    size_t inLen = strlen(in);

    if (convert("UTF-8", "GBK//IGNORE", in, &inLen, out, &outLen)) {
        fprintf(stdout, "%s\n", out);
    } else {
        fprintf(stderr, "convert failed\n");
    }

    return 0;
}
```



