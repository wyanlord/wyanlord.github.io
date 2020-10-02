

##### 一、cmake文件

```cpp
cmake_minimum_required(VERSION 3.13)
project(qtdemo1)

set(CMAKE_CXX_STANDARD 14)

set(CMAKE_INCLUDE_CURRENT_DIR ON)

set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTOUIC ON)
set(CMAKE_AUTORCC ON)

set(CMAKE_PREFIX_PATH D:/AppData/Qt/5.8/mingw53_32)

set(CMAKE_BUILD_TYPE Release)

find_package(Qt5Core)
find_package(Qt5Widgets)
find_package(Qt5Gui)

set(UI_FILES)
set(RC_FILES)
set(QRC_FILES)

set(SOURCE_FILES main.cpp mainwindow.cpp mainwindow.h)

add_executable(qtdemo1 WIN32 ${SOURCE_FILES} ${UI_FILES} ${RC_FILES} ${QRC_FILES})

target_link_libraries(qtdemo1 Qt5::Widgets Qt5::Core Qt5::Gui)
```

##### 二、main文件
```cpp
#include "mainwindow.h"
#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    MainWindow w;
    w.show();

    return a.exec();
}
```

##### 三、mainwindow文件
```cpp
#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>

namespace Ui {
    class MainWindow;
}

class MainWindow : public QMainWindow {
Q_OBJECT

public:
    explicit MainWindow(QWidget *parent = nullptr);

    ~ MainWindow() override;

private:
    Ui::MainWindow *ui;
};

#endif // MAINWINDOW_H
```

```cpp
#include "mainwindow.h"
#include "ui_mainwindow.h"

MainWindow::MainWindow(QWidget *parent) : QMainWindow(parent), ui(new Ui::MainWindow) {
    ui->setupUi(this);
}

MainWindow::~MainWindow() {
    delete ui;
}
```

##### 四、新建QMainWindow类型的ui文件及槽函数

```cpp
private slots:
    void on_pushButton_clicked();

void MainWindow::on_pushButton_clicked() {
    QMessageBox::information(this, "title", "content", QMessageBox::YesAll);
}
```



##### 五、新建windows系统的菜单右键

​    1、Win+R 运行regedit，打开注册表。

​    2、新建目录 HKEY_CLASSES_ROOT\*\shell\DeployQt\command。

​    3、设置默认值为：D:\AppData\Qt\Qt5.14.2\5.14.2\mingw73_32\bin\windeployqt.exe "%1" --dir=output --no-translations --no-opengl-sw --no-system-d3d-compiler --release --no-compiler-runtime

