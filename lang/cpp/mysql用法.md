#### 一、安装mysql

下载地址

```
https://dev.mysql.com/downloads/mysql/
```

分为安装版和解压缩版

- 离线安装版：[mysql-installer-community.msi](http://coderyyn.cn/DataBase/mysql-installer-community-8.0.13.0.msi)
- 解压缩版：[mysql-8.0.13-winx64.zip](http://coderyyn.cn/DataBase/mysql-8.0.13-winx64.zip)

根据libmysql.dll生成libmysql.a

```
gendef libmysql.dll
dlltool -D libmysql.dll -d libmysql.def -l libmysql.a
```

#### 二、使用mysql

```cpp
#include <mysql/mysql.h>
#include <cstdio>

int main() {
    MYSQL mysql;
    MYSQL_RES *res;
    MYSQL_FIELD *field;
    MYSQL_ROW row;
    int ret;

    mysql_init(&mysql);

    if (!mysql_real_connect(&mysql, "localhost", "root", "root", "demo", 0, NULL, 0)) {
        printf("Failed to connect to Mysql!\n");
        return -1;
    } else {
        printf("Connected to Mysql successfully!\n");
    }

    ret = mysql_query(&mysql, "select username, age from user");
    if (ret != 0) {
        printf("query failed\n");
        return -1;
    }

    res = mysql_store_result(&mysql);
    if (res) {
        int column = mysql_num_fields(res);

        while ((field = mysql_fetch_field(res)) != NULL) {
            printf("%25s |", field->name);
        }

        printf("\n");

        while ((row = mysql_fetch_row(res)) != NULL) {
            for (int i = 0; i < column; i++) {
                printf("%25s |", row[i]);
            }

            printf("\n");
        }

        mysql_free_result(res);
    }

    mysql_close(&mysql);

    return 0;
}
```

