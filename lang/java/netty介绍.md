### 一、NIO

NIO是一个非阻塞模式，发送或者读取数据，没有数据就什么都不做，不会阻塞线程的执行。

NIO使用一个线程管理了成千上万的socket连接请求，大大的提高了系统的并发能力。

NIO以块的方式基于管道和缓冲区处理数据，而BIO以流的方式处理数据。

Selector管理了多个Channel，每个Channel配置了一个Buffer缓冲区，每个客户端和Buffer缓冲区交互。

#### 1、Buffer - 缓冲区

本质上是一个可读写的内存块，内部使用数组实现，并包含了数组的mark，capacity，limit，position四大基本属性，使用flip()进行读写切换。

常用的方法：allocate()、put()、get()和flip()。

最常用的是ByteBuffer，因为网络传输都是以二进制字节传输的。

比较经典的是MappedByteBuffer，FileChannel.map()可以让文件的一部分空间以Buffer的形式进行操作。

#### 2、Channel - 通道

可以同时进行读写，异步读写数据，和Buffer进行双向读写操作。

Channel是一个接口，该接口实现了Closeable接口，利于try资源管理。

常用的Channel实现类：FIleChannel，ServerSocketChannel，SocketChannel

常用的读写Buffer方法：read(ByteBuffer dst)，write(ByteBuffer src)

常用的拷贝通道方法：transferFrom(ReadableChannel src)，transferTo(WritableChannel dst)

#### 3、Selector - 选择器

对应底层的操作系统的select、poll或者epoll等，通过事件来驱动，即Reactor模型。

ServerSocketChannel.open()，bind()，configuareNonBlock，register到Selector上。

通过select相关的方法，得到有事件发生的SelectionKey，反向获取注册的SocketChannel。

ServerSocketChannel通过accept获取到的SocketChannel注册到Selector中，关联上SelectionKey。

#### 4、零拷贝

从操作系统的角度看，在内核空间，只有一份数据，称为零拷贝

normal：Hard Drive -> Kernel buffer-> User buffer-> Socket buffer -> Protocaol engine，一共四次拷贝

mmap：Hard Drive -> Kernel buffer-> Socket buffer -> Protocaol engine，一共三次拷贝

sendFile：Hard Drive -> Kernel buffer -> Protocaol engine，一共两次拷贝

mmap适合小文件，sendFile适合传输大文件



### 二、Netty

是JBoss提供的一个Java开源项目，异步的、基于事件驱动的网络应用程序框架。

#### 1、Reactor线程模型

+ 单Reactor单线程，无法利用多核优势，可以开启多个进程解决
+ 单Reactor多线程，多线程Handler数据容易出现竞争，Reactor本身仍然是单线程
+ 主从Reactor多线程，主线程accept，从线程处理Handler

#### 2、Netty线程模型

BossGroup线程维护一个只关注Accept类型事件的Selector。

当接收到Accept事件后，获取到SocketChannel，封装成NIOSocketChannel，并注册到Worker线程的Selector中。

当Worker线程监听到Selector中有Read事件时，读取数据后交给线程池去处理。

线程池处理完后，向Worker线程注册Write事件，由Worker线程send数据给到客户端。



















