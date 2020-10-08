#### 一、注释

单行注释：#注释内容

多行注释：可以使用括号来实现多行注释，\#[[多行注释]]

#### 二、变量

```xml
set(var 123)
message("var = ${var}")
```

#### 三、列表

```
set(list 1 2 3 4 5)
set(list "1;2;3;4;5")
message("list = ${list}")
```

#### 四、流程控制 - 操作符

+ 一元：`EXIST`，`COMMAND`，`DEFINED`
+ 二元：`EQUAL`，`LESS`，`LESS_EQAUL`，`GREATER`，`GREATER_EQAUL`，`STREQUAL`，`STRLESS`，`STRLESS_EQAUL`，`STRGREATER`，`STRGREATER_EQAUL`，`MATCHES`
+ 三元：`NOT`，`AND`，`OR`

#### 五、流程控制 - 布尔常量

+ true：`1`，`ON`，`YES`，`TRUE`，`Y`，非`0`值
+ false：`0`，`OFF`，`NO`，`FALSE`，`N`，`IGNORE`，`NOTFOUND`，空字符串，以`-NOTFOUND`结尾的字符串

#### 六、流程控制  - 条件与循环命令

break() 命令可以跳出整个循环， continue() 可以跳出当前循环

```
if (表达式)
    COMMAND(ARGS...)
elseif(表达式)
    COMMAND(ARGS...)
else(表达式)
    COMMAND(ARGS...)
endif(表达式)

while(表达式)
    COMMAND(ARGS...)
endwhile(表达式)

foreach(循环变量 参数1 参数2... 参数N)
     COMMAND(ARGS...)
endforeach(循环变量)

foreach(item RANGE start stop step)
    message("item = ${item}")
endforeach(item)

foreach(循环遍历 IN LISTS 列表)
     COMMAND(ARGS...)
endforeach(循环变量)
```

#### 七、自定义函数与宏

宏可以避免作用域的问题

```
function(<name>[arg1 [arg3 [arg3...]]])
     COMMAND(ARGS...)
endfunction(<name>)

macro(<name>[arg1 [arg3 [arg3...]]])
     COMMAND(ARGS...)
endmacro(<name>)
```

#### 八、预定义变量

| 变量名                                                     | 描述                                                    |
| ---------------------------------------------------------- | ------------------------------------------------------- |
| PROJECT_NAME                                               | 项目名称                                                |
| PROJECT_SOURCE_DIR                                         | 项目根目录                                              |
| PROJECT_BINARY_DIR                                         | 运行`cmake`命令的目录,通常是${PROJECT_SOURCE_DIR}/build |
| CMAKE_INCLUDE_PATH                                         | 环境变量                                                |
| CMAKE_LIBRARY_PATH                                         | 环境变量                                                |
| CMAKE_INCLUDE_CURRENT_DIR                                  | 设置工程包含当前目录ON                                  |
| CMAKE_CURRENT_SOURCE_DIR                                   | 当前处理的CMakeLists.txt所在的路径                      |
| CMAKE_CURRENT_BINARY_DIR                                   | target编译目录                                          |
| CMAKE_CURRENT_LIST_FILE                                    | 输出调用这个变量的CMakeLists.txt的完整路径              |
| CMAKE_CURRENT_LIST_LINE                                    | 输出这个变量所在的行                                    |
| CMAKE_MODULE_PATH                                          | 定义自己的cmake模块所在的路径                           |
| EXECUTABLE_OUTPUT_PATH                                     | 重新定义目标二进制可执行文件的存放位置                  |
| LIBRARY_OUTPUT_PATH                                        | 重新定义目标链接库文件的存放位置                        |
| CMAKE_ALLOW_LOOSE_LOOP_CONSTRUCTS                          | 用来控制IF ELSE语句的书写方式                           |
| CMAKE_RUNTIME_OUTPUT_DIRECTORY_DEBUG                       | Debug版本可执行文件的输出目录                           |
| CMAKE_RUNTIME_OUTPUT_DIRECTORY_RELEASE                     | Release版本可执行文件的输出目录                         |
| CMAKE_ARCHIVE_OUTPUT_DIRECTORY_DEBUG                       | Debug版本库文件的输出目录                               |
| CMAKE_ARCHIVE_OUTPUT_DIRECTORY_RELEASE                     | Release版本库文件的输出目录                             |
| CMAKE_DEBUG_POSTFIX                                        | Debug版本下库文件的后缀名                               |
| CMAKE_RELEASE_POSTFIX                                      | Release版本下库文件的后缀名                             |
| set_target_properties(exe PROPERTIES DEBUG_POSTFIX "_d")   | Debug版本下可执行文件的后缀名                           |
| set_target_properties(exe PROPERTIES RELEASE_POSTFIX "_r") | Release版本下可执行文件的后缀名                         |

#### 九、常用命令

| 命令名                                                  | 描述                                 |
| ------------------------------------------------------- | ------------------------------------ |
| project(Main)                                           | 指定项目名称，可以带C指明是C语言项目 |
| cmake_minimum_required(VERSION 3.1.5)                   | 指定需要cmake的最低版本              |
| aux_source_directory(. DIR_SRCS)                        | 将所有源文件名称保存在变量列表中     |
| add_library(Lib [SHARED] ${DIR_SRCS})                   | 将源文件编译为库文件，默认STATIC     |
| add_executable(Exe ${DIR_SRCS})                         | 将源文件编译为可执行文件             |
| add_dependencies(Exe Lib)                               | 指定Exe依赖Lib库文件                 |
| add_subdirectory(Lib_DIR Bin_DIR)                       | 添加项目子目录                       |
| target_link_libraries(Exe Lib)                          | 将三方库文件链接到可执行文件中       |
| set(USE_STATIC YES)                                     | 设置变量的内容，可以加CACHE          |
| unset(USE_STATIC)                                       | 删除变量的内容                       |
| message("use static ${USE_STATIC}")                     | 打印字符串内容                       |
| include_directories(/usr/share/include)                 | 添加三方库头文件扫描目录             |
| link_directories(/usr/share/lib)                        | 添加三方库文件扫描目录               |
| find_path(var1 name1 path1 path2 ...)                   | 从多个路径下查找name1                |
| find_library(var1 name1 path1 path2 ...)                | 从多个路径下查找name1库文件          |
| add_definitions(-D CURL_STATICLIB -DUNICODE -D_UNICODE) | 定义预处理宏                         |
| file(GLOB\|GLOB_RECURSE all_files file1 file2 ...)      | 将所有文件保存在变量中               |
|                                                         |                                      |
|                                                         |                                      |

