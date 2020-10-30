### libevent

#### 一、socket

##### 1、TCP协议的三次握手中SYN，ACK，Seq含义

关于三次握手流程

a）C端向S端发送位码SYN=1，SEQ=Cxxxx，S端发现是SYN=1位码，得知C是来请求联机的。

b）S端确认联机信息后，返回给C四条信息，SYN=1， ACK=1， ACKnumber=Cxxxx + 1，SEQ=Sxxxx。

c）C端确认SYN=1， ACK=1，校验ACKnumber正确，再次向S端发送ACK=1，ACKnumber=Sxxxx+1，成功建立联接。

其中，第一次请求联机时，C端的socket信息会被存储在S端的SYN队列中，队列长度为SYN_BACKLOG，然后等待操作系统逐个去POP出来进行ESTABLISHED给客户端

握手成功后，C端的socket信息被存储在LISTEN队列中，队列长度为LISTEN_BACKLOG，并等待应用程序的accept函数POP出来做处理

如果发生DOS攻击，导致LISTEN_BACKLOG长度不够，那么会将后续三次握手成功的socket请求drop掉，并返回给客户端refused信息

大多数情况下，如果遇到BACKLOG关键字的错误，则可以猜测出来SYN和LISTEN相关的队列的长度过小导致的

##### 2、中断

**硬中断：**

1. 硬中断是由硬件产生的，比如，像磁盘，网卡，键盘，时钟等。每个设备或设备集都有它自己的IRQ（中断请求）。基于IRQ，CPU可以将相应的请求分发到对应的硬件驱动上（注：硬件驱动通常是内核中的一个子程序，而不是一个独立的进程）。

2. 处理中断的驱动是需要运行在CPU上的，因此，当中断产生的时候，CPU会中断当前正在运行的任务，来处理中断。在有多核心的系统上，一个中断通常只能中断一颗CPU（也有一种特殊的情况，就是在大型主机上是有硬件通道的，它可以在没有主CPU的支持下，可以同时处理多个中断。）。

3. 硬中断可以直接中断CPU。它会引起内核中相关的代码被触发。对于那些需要花费一些时间去处理的进程，中断代码本身也可以被其他的硬中断中断。

4. 对于时钟中断，内核调度代码会将当前正在运行的进程挂起，从而让其他的进程来运行。它的存在是为了让调度代码（或称为调度器）可以调度多任务。

**软中断：**

1. 软中断的处理非常像硬中断。然而，它们仅仅是由当前正在运行的进程所产生的。

2. 通常，软中断是一些对I/O的请求。这些请求会调用内核中可以调度I/O发生的程序。对于某些设备，I/O请求需要被立即处理，而磁盘I/O请求通常可以排队并且可以稍后处理。根据I/O模型的不同，进程或许会被挂起直到I/O完成，此时内核调度器就会选择另一个进程去运行。I/O可以在进程之间产生并且调度过程通常和磁盘I/O的方式是相同。

3. 软中断仅与内核相联系。而内核主要负责对需要运行的任何其他的进程进行调度。一些内核允许设备驱动的一些部分存在于用户空间，并且当需要的时候内核也会调度这个进程去运行。

4. 软中断并不会直接中断CPU。也只有当前正在运行的代码（或进程）才会产生软中断。这种中断是一种需要内核为正在运行的进程去做一些事情（通常为I/O）的请求。有一个特殊的软中断是Yield调用，它的作用是请求内核调度器去查看是否有一些其他的进程可以运行。

​	***问题解答：\***

 	**1. 问：对于软中断，I/O操作是否是由内核中的I/O设备驱动程序完成？**

  答：对于I/O请求，内核会将这项工作分派给合适的内核驱动程序，这个程序会对I/O进行队列化，以可以稍后处理（通常是磁盘I/O），或如果可能可以立即执行它。通常，当对硬中断进行回应的时候，这个队列会被驱动所处理。当一个I/O请求完成的时候，下一个在队列中的I/O请求就会发送到这个设备上。

​	**2. 问：软中断所经过的操作流程是比硬中断的少吗？换句话说，对于软中断就是：进程 ->内核中的设备驱动程序；对于硬中断：硬件->CPU->内核中的设备驱动程序？**

答：是的，软中断比硬中断少了一个硬件发送信号的步骤。产生软中断的进程一定是当前正在运行的进程，因此它们不会中断CPU。但是它们会中断调用代码的流程。

如果硬件需要CPU去做一些事情，那么这个硬件会使CPU中断当前正在运行的代码。而后CPU会将当前正在运行进程的当前状态放到堆栈（stack）中，以至于之后可以返回继续运行。这种中断可以停止一个正在运行的进程；可以停止正处理另一个中断的内核代码；或者可以停止空闲进程。

##### 3、select、poll和epoll的区别

a）select==>时间复杂度O(n)

它仅仅知道了，有I/O事件发生了，却并不知道是哪那几个流（可能有一个，多个，甚至全部），我们只能无差别轮询所有流，找出能读出数据，或者写入数据的流，对他们进行操作。所以**select具有O(n)的无差别轮询复杂度**，同时处理的流越多，无差别轮询时间就越长。

b）poll==>时间复杂度O(n)

poll本质上和select没有区别，它将用户传入的数组拷贝到内核空间，然后查询每个fd对应的设备状态， **但是它没有最大连接数的限制**，原因是它是基于链表来存储的.

c）epoll==>时间复杂度O(1)

**epoll可以理解为event poll**，不同于忙轮询和无差别轮询，epoll会把哪个流发生了怎样的I/O事件通知我们。所以我们说epoll实际上是**事件驱动（每个事件关联上fd）**的，此时我们对这些流的操作都是有意义的。**（复杂度降低到了O(1)）**

select，poll，epoll都是IO多路复用的机制。I/O多路复用就通过一种机制，可以监视多个描述符，一旦某个描述符就绪（一般是读就绪或者写就绪），能够通知程序进行相应的读写操作。**但select，poll，epoll本质上都是同步I/O，因为他们都需要在读写事件就绪后自己负责进行读写，也就是说这个读写过程是阻塞的**，而异步I/O则无需自己负责进行读写，异步I/O的实现会负责把数据从内核拷贝到用户空间。 

epoll跟select都能提供多路I/O复用的解决方案。在现在的Linux内核里有都能够支持，其中epoll是Linux所特有，而select则应该是POSIX所规定，一般操作系统均有实现。

**select：**

select本质上是通过设置或者检查存放fd标志位的数据结构来进行下一步处理。这样所带来的缺点是：

1、 单个进程可监视的fd数量被限制，即能监听端口的大小有限。

   一般来说这个数目和系统内存关系很大，具体数目可以cat /proc/sys/fs/file-max察看。32位机默认是1024个。64位机默认是2048.

2、 对socket进行扫描时是线性扫描，即采用轮询的方法，效率较低：

​    当套接字比较多的时候，每次select()都要通过遍历FD_SETSIZE个Socket来完成调度,不管哪个Socket是活跃的,都遍历一遍。这会浪费很多CPU时间。如果能给套接字注册某个回调函数，当他们活跃时，自动完成相关操作，那就避免了轮询，这正是epoll与kqueue做的。

3、需要维护一个用来存放大量fd的数据结构，这样会使得用户空间和内核空间在传递该结构时复制开销大

**poll：**

poll本质上和select没有区别，它将用户传入的数组拷贝到内核空间，然后查询每个fd对应的设备状态，如果设备就绪则在设备等待队列中加入一项并继续遍历，如果遍历完所有fd后没有发现就绪设备，则挂起当前进程，直到设备就绪或者主动超时，被唤醒后它又要再次遍历fd。这个过程经历了多次无谓的遍历。

**它没有最大连接数的限制**，原因是它是基于链表来存储的，但是同样有一个缺点：

1、大量的fd的数组被整体复制于用户态和内核地址空间之间，而不管这样的复制是不是有意义。          

2、poll还有一个特点是“水平触发”，如果报告了fd后，没有被处理，那么下次poll时会再次报告该fd。

**epoll:**

epoll有EPOLLLT和EPOLLET两种触发模式，LT是默认的模式，ET是“高速”模式。LT模式下，只要这个fd还有数据可读，每次 epoll_wait都会返回它的事件，提醒用户程序去操作，而在ET（边缘触发）模式中，它只会提示一次，直到下次再有数据流入之前都不会再提示了，无 论fd中是否还有数据可读。所以在ET模式下，read一个fd的时候一定要把它的buffer读光，也就是说一直读到read的返回值小于请求值，或者 遇到EAGAIN错误。还有一个特点是，epoll使用“事件”的就绪通知方式，通过epoll_ctl注册fd，一旦该fd就绪，内核就会采用类似callback的回调机制来激活该fd，epoll_wait便可以收到通知。

**epoll为什么要有EPOLLET触发模式？**

如果采用EPOLLLT模式的话，系统中一旦有大量你不需要读写的就绪文件描述符，它们每次调用epoll_wait都会返回，这样会大大降低处理程序检索自己关心的就绪文件描述符的效率.。而采用EPOLLET这种边沿触发模式的话，当被监控的文件描述符上有可读写事件发生时，epoll_wait()会通知处理程序去读写。如果这次没有把数据全部读写完(如读写缓冲区太小)，那么下次调用epoll_wait()时，它不会通知你，也就是它只会通知你一次，直到该文件描述符上出现第二次可读写事件才会通知你！！！**这种模式比水平触发效率高，系统不会充斥大量你不关心的就绪文件描述符**

**epoll的优点：**

1、**没有最大并发连接的限制，能打开的FD的上限远大于1024（1G的内存上能监听约10万个端口）**；
**2、效率提升，不是轮询的方式，不会随着FD数目的增加效率下降。只有活跃可用的FD才会调用callback函数；**
**即Epoll最大的优点就在于它只管你“活跃”的连接，而跟连接总数无关，因此在实际的网络环境中，Epoll的效率就会远远高于select和poll。**

3、 内存拷贝，利用mmap()文件映射内存加速与内核空间的消息传递；即epoll使用mmap减少复制开销。

**总结：**

**select的几大缺点：**

**（1）每次调用select，都需要把fd集合从用户态拷贝到内核态，这个开销在fd很多时会很大**

**（2）同时每次调用select都需要在内核遍历传递进来的所有fd，这个开销在fd很多时也很大**

**（3）select支持的文件描述符数量太小了，默认是1024**

**2 poll实现**

　　poll的实现和select非常相似，只是描述fd集合的方式不同，poll使用pollfd结构而不是select的fd_set结构，其他的都差不多,管理多个描述符也是进行轮询，根据描述符的状态进行处理，**但是poll没有最大文件描述符数量的限制**。poll和select同样存在一个缺点就是，包含大量文件描述符的数组被整体复制于用户态和内核的地址空间之间，而不论这些文件描述符是否就绪，它的开销随着文件描述符数量的增加而线性增大。

**3、epoll**

　　epoll既然是对select和poll的改进，就应该能避免上述的三个缺点。那epoll都是怎么解决的呢？在此之前，我们先看一下epoll和select和poll的调用接口上的不同，select和poll都只提供了一个函数——select或者poll函数。而epoll提供了三个函数，epoll_create,epoll_ctl和epoll_wait，epoll_create是创建一个epoll句柄；epoll_ctl是注册要监听的事件类型；epoll_wait则是等待事件的产生。

　　对于第一个缺点，epoll的解决方案在epoll_ctl函数中。每次注册新的事件到epoll句柄中时（在epoll_ctl中指定EPOLL_CTL_ADD），会把所有的fd拷贝进内核，而不是在epoll_wait的时候重复拷贝。epoll保证了每个fd在整个过程中只会拷贝一次。

　　对于第二个缺点，epoll的解决方案不像select或poll一样每次都把current轮流加入fd对应的设备等待队列中，而只在epoll_ctl时把current挂一遍（这一遍必不可少）并为每个fd指定一个回调函数，当设备就绪，唤醒等待队列上的等待者时，就会调用这个回调函数，而这个回调函数会把就绪的fd加入一个就绪链表）。epoll_wait的工作实际上就是在这个就绪链表中查看有没有就绪的fd（利用schedule_timeout()实现睡一会，判断一会的效果，和select实现中的第7步是类似的）。

　　对于第三个缺点，epoll没有这个限制，它所支持的FD上限是最大可以打开文件的数目，这个数字一般远大于2048,举个例子,在1GB内存的机器上大约是10万左右，具体数目可以cat /proc/sys/fs/file-max察看,一般来说这个数目和系统内存关系很大。

**总结：**

（1）select，poll实现需要自己不断轮询所有fd集合，直到设备就绪，期间可能要睡眠和唤醒多次交替。而epoll其实也需要调用epoll_wait不断轮询就绪链表，期间也可能多次睡眠和唤醒交替，但是它是设备就绪时，调用回调函数，把就绪fd放入就绪链表中，并唤醒在epoll_wait中进入睡眠的进程。虽然都要睡眠和交替，但是select和poll在“醒着”的时候要遍历整个fd集合，而epoll在“醒着”的时候只要判断一下就绪链表是否为空就行了，这节省了大量的CPU时间。这就是回调机制带来的性能提升。

（2）select，poll每次调用都要把fd集合从用户态往内核态拷贝一次，并且要把current往设备等待队列中挂一次，而epoll只要一次拷贝，而且把current往等待队列上挂也只挂一次（在epoll_wait的开始，注意这里的等待队列并不是设备等待队列，只是一个epoll内部定义的等待队列）。这也能节省不少的开销。 

```cpp
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <unistd.h>
#include <sys/socket.h>
#include <netinet/in.h>

#define POOL_SIZE 16

int main() {
    int ret, listen_fd, max_fd;
    int conn_pool[POOL_SIZE];
    memset(conn_pool, -1, CONN_SIZE * sizeof(int));
    fd_set read_set;
    timeval tv = {3, 0};
    char bufRecv[100];

    // create listen socket fd
    listen_fd = socket(AF_INET, SOCK_STREAM, 0);
    assert(-1 != listen_fd);
    max_fd = listen_fd;
    conn_pool[0] = listen_fd;

    // create socket addr
    struct sockaddr_in sock_addr;
    sock_addr.sin_family = AF_INET;
    sock_addr.sin_addr.s_addr = INADDR_ANY;
    sock_addr.sin_port = htons(8000);

    // bind and listen
    ret = bind(listen_fd, (sockaddr *) &sock_addr, sizeof(sock_addr));
    assert(-1 != ret);
    ret = listen(listen_fd, 16);
    assert(-1 != ret);

    // success start socket
    printf("start socket successfully, listen on %d\n", ntohs(sock_addr.sin_port));

    while (true) {
        // fill all fds to read set
        FD_ZERO(&read_set);
        for (int i = 0; i < POOL_SIZE; ++i) {
            if (conn_pool[i] != -1) {
                FD_SET(conn_pool[i], &read_set);
            }
        }

        // select timeout
        tv.tv_sec = 3;
        tv.tv_usec = 0;

        // select util 3 seconds
        ret = select(max_fd + 1, &read_set, NULL, NULL, &tv);
        assert(-1 != ret);

        // timeout
        if (ret == 0) continue;

        for (int i = 0; i < POOL_SIZE; ++i) {
            int fd = conn_pool[i];
            if (FD_ISSET(fd, &read_set)) {
                if (fd == listen_fd) {
                    // start to accept a client socket
                    struct sockaddr_in sock_addr_client;
                    socklen_t len = sizeof(sock_addr_client);
                    int client_fd = accept(listen_fd, (sockaddr *) &sock_addr_client, &len);
                    assert(-1 != client_fd);

                    // fill the client socket to read set and conn pool
                    FD_SET(client_fd, &read_set);
                    for (int j = 0; j < POOL_SIZE; ++j) {
                        if (conn_pool[j] == -1) {
                            conn_pool[j] = client_fd;
                            break;
                        }
                    }

                    // reset max fd
                    max_fd = max_fd > client_fd ? max_fd : client_fd;
                } else {
                    // read buffer from fd
                    ret = recv(fd, bufRecv, sizeof(bufRecv), 0);
                    assert(-1 != ret);

                    if (ret == 0) {
                        // remove the fd from conn pool
                        for (int j = 0; j < POOL_SIZE; ++j) {
                            if (conn_pool[j] == fd) {
                                conn_pool[j] = -1;
                                break;
                            }
                        }

                        // clear fd from read set
                        FD_CLR(fd, &read_set);

                        printf("client quit!\n");
                    } else {
                        // print recv message and send ok to client
                        bufRecv[ret - 1] = '\0';
                        printf("recv message: %s\n", bufRecv);
                        send(fd, "ok\n", 3, 0);
                    }
                }
            }
        }
    }
}
```



```c
#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <unistd.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <poll.h>

#define POOL_SIZE 16

int main() {
    int ret, listen_fd;
    struct pollfd *conn_pool;
    char bufRecv[100];

    // create listen socket fd
    listen_fd = socket(AF_INET, SOCK_STREAM, 0);
    assert(-1 != listen_fd);

    // create socket addr
    struct sockaddr_in sock_addr;
    sock_addr.sin_family = AF_INET;
    sock_addr.sin_addr.s_addr = INADDR_ANY;
    sock_addr.sin_port = htons(8000);

    // bind and listen
    ret = bind(listen_fd, (sockaddr *) &sock_addr, sizeof(sock_addr));
    assert(-1 != ret);
    ret = listen(listen_fd, 16);
    assert(-1 != ret);

    // success start socket
    printf("start socket successfully, listen on %d\n", ntohs(sock_addr.sin_port));

    // init pool fds
    conn_pool = (struct pollfd *) malloc(sizeof(struct pollfd) * POOL_SIZE);
    for (int i = 0; i < POOL_SIZE; ++i) {
        conn_pool[i].fd = -1;
        conn_pool[i].events = 0;
        conn_pool[i].revents = 0;
    }
    conn_pool[0].fd = listen_fd;
    conn_pool[0].events |= POLLIN;

    while (true) {
        // poll util 3 seconds
        ret = poll(conn_pool, POOL_SIZE, 3);
        assert(-1 != ret);

        // timeout
        if (ret == 0) continue;

        for (int i = 0; i < POOL_SIZE; ++i) {
            if (conn_pool[i].fd == -1) continue;

            int fd = conn_pool[i].fd;

            if (fd == listen_fd && conn_pool[i].revents & POLLIN) {
                // start to accept a client socket
                struct sockaddr_in sock_addr_client;
                socklen_t len = sizeof(sock_addr_client);
                int client_fd = accept(listen_fd, (sockaddr *) &sock_addr_client, &len);
                assert(-1 != client_fd);

                // fill the client socket to conn pool
                for (int j = 0; j < POOL_SIZE; ++j) {
                    if (conn_pool[j].fd == -1) {
                        conn_pool[j].fd = client_fd;
                        conn_pool[j].events |= POLLIN;
                        conn_pool[j].events |= POLLRDHUP;
                        break;
                    }
                }

                // reset events
                conn_pool[i].revents = 0;
            } else if (conn_pool[i].revents & POLLRDHUP) {
                // remove the fd from conn pool
                conn_pool[i].fd = -1;
                conn_pool[i].events = 0;
                conn_pool[i].revents = 0;

                printf("client quit!\n");
            } else if (conn_pool[i].revents & POLLIN) {
                // read buffer from fd
                ret = recv(fd, bufRecv, sizeof(bufRecv), 0);
                assert(-1 != ret);

                if (ret > 0) {
                    // print recv message and send ok to client
                    bufRecv[ret - 1] = '\0';
                    printf("recv message: %s\n", bufRecv);
                    send(fd, "ok\n", 3, 0);

                    // reset events
                    conn_pool[i].revents = 0;
                }
            }
        }
    }
}
```



```cpp
#include <cstdio>
#include <cassert>
#include <unistd.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <sys/epoll.h>
#include <fcntl.h>

#define POOL_SIZE 16

int main() {
    int ret, listen_fd, epoll_fd;
    struct epoll_event ev, events[POOL_SIZE];
    char bufRecv[100];

    // create listen socket fd
    listen_fd = socket(AF_INET, SOCK_STREAM, 0);
    assert(-1 != listen_fd);

    // create socket addr
    struct sockaddr_in sock_addr;
    sock_addr.sin_family = AF_INET;
    sock_addr.sin_addr.s_addr = INADDR_ANY;
    sock_addr.sin_port = htons(8000);

    // bind and listen
    ret = bind(listen_fd, (sockaddr *) &sock_addr, sizeof(sock_addr));
    assert(-1 != ret);
    ret = listen(listen_fd, 16);
    assert(-1 != ret);

    // success start socket
    printf("start socket successfully, listen on %d\n", ntohs(sock_addr.sin_port));

    // init epoll, add listen fd to epoll
    epoll_fd = epoll_create(10000);

    ret = fcntl(listen_fd, F_SETFL, fcntl(listen_fd, F_GETFD, 0)|O_NONBLOCK);
    assert(-1 != ret);

    ev.events = EPOLLIN;
    ev.data.fd = listen_fd;
    epoll_ctl(epoll_fd, EPOLL_CTL_ADD, listen_fd, &ev);

    while (true) {
        // poll util 3 seconds
        ret = epoll_wait(epoll_fd, events, POOL_SIZE, 3);
        assert(-1 != ret);

        // timeout
        if (ret == 0) continue;

        for (int i = 0; i < ret; ++i) {
            int fd = events[i].data.fd;

            if (fd == listen_fd && events[i].events & EPOLLIN) {
                // start to accept a client socket
                struct sockaddr_in sock_addr_client;
                socklen_t len = sizeof(sock_addr_client);
                int client_fd = accept(listen_fd, (sockaddr *) &sock_addr_client, &len);
                assert(-1 != client_fd);

                // set non block
                ret = fcntl(client_fd, F_SETFL, fcntl(client_fd, F_GETFD, 0)|O_NONBLOCK);
                assert(-1 != ret);

                ev.events = EPOLLIN | EPOLLET;
                ev.data.fd = client_fd;

                epoll_ctl(epoll_fd, EPOLL_CTL_ADD, client_fd, &ev);
            } else if (events[i].events & EPOLLIN) {
                // read buffer from fd
                ret = recv(fd, bufRecv, sizeof(bufRecv), 0);
                assert(-1 != ret);

                if (ret == 0) {
                    epoll_ctl(epoll_fd, EPOLL_CTL_DEL, fd, NULL);
                    close(fd);

                    printf("client quit!\n");
                } else {
                    // print recv message and send ok to client
                    bufRecv[ret - 1] = '\0';
                    printf("recv message: %s\n", bufRecv);
                    send(fd, "ok\n", 3, 0);
                }
            }
        }
    }
}
```



#### 二、libevent编译

```cmd
export CFLAGS=-I/usr/xxx/include
export LDFLAGS=-L/usr/xxx/lib
./configuare
make
make install
```

#### 三、使用示例

```ini
cmake_minimum_required(VERSION 3.15)
project(libevdemo)

set(CMAKE_CXX_STANDARD 17)

include_directories(D:/MyCode/libs/libevent/include)
link_directories(D:/MyCode/libs/libevent/lib)

add_executable(libevdemo main.cpp)
target_link_libraries(libevdemo event ws2_32)
```



```cpp
#include <cstdio>
#include <winsock2.h>
#include <event2/event.h>
#include <event2/bufferevent.h>
#include <ctime>
#include <cassert>

# define LISTEN_PORT 9999
# define LISTEN_BACKLOG 32

void do_accept(evutil_socket_t listener, short event, void *arg);

void read_cb(struct bufferevent *bev, void *arg);

void error_cb(struct bufferevent *bev, short event, void *arg);

void write_cb(struct bufferevent *bev, void *arg);

int main(int argc, char *argv[]) {
    int ret;

    // init windows wsa
    WSAData data;
    ret = WSAStartup(MAKEWORD(2, 2), &data);
    assert(ret == 0);

    // create socket listener
    evutil_socket_t listener;
    listener = socket(AF_INET, SOCK_STREAM, 0);
    assert(listener > 0);
    evutil_make_listen_socket_reuseable(listener);

    // create socket addr
    struct sockaddr_in sin;
    sin.sin_family = AF_INET;
    sin.sin_addr.s_addr = 0;
    sin.sin_port = htons(LISTEN_PORT);

    // bind socket with socket addr
    if (bind(listener, (struct sockaddr *) &sin, sizeof(sin)) < 0) {
        perror("bind");
        return 1;
    }

    // listen some port
    if (listen(listener, LISTEN_BACKLOG) < 0) {
        perror("listen");
        return 1;
    }

    printf("Listening...\n");

    evutil_make_socket_nonblocking(listener);

    struct event_base *base = event_base_new();
    assert(base != NULL);
    struct event *listen_event;
    listen_event = event_new(base, listener, EV_READ | EV_PERSIST, do_accept, (void *) base);
    event_add(listen_event, NULL);
    event_base_dispatch(base);

    printf("The End.");
    return 0;
}

void do_accept(evutil_socket_t listener, short event, void *arg) {
    struct event_base *base = (struct event_base *) arg;
    evutil_socket_t fd;
    struct sockaddr_in sin;
    socklen_t slen = sizeof(sin);
    fd = accept(listener, (struct sockaddr *) &sin, &slen);
    if (fd < 0) {
        perror("accept");
        return;
    }

    printf("ACCEPT: fd = %u\n", fd);

    struct bufferevent *bev = bufferevent_socket_new(base, fd, BEV_OPT_CLOSE_ON_FREE);
    bufferevent_setcb(bev, read_cb, NULL, error_cb, arg);
    bufferevent_enable(bev, EV_READ | EV_WRITE | EV_PERSIST);
}

void read_cb(struct bufferevent *bev, void *arg) {
# define MAX_LINE    256
    char line[MAX_LINE + 1];
    int n;
    evutil_socket_t fd = bufferevent_getfd(bev);

    while (n = bufferevent_read(bev, line, MAX_LINE), n > 0) {
        line[n] = '\0';
        printf("fd=%u, read line: %s\n", fd, line);

        bufferevent_write(bev, line, n);
    }
}

void write_cb(struct bufferevent *bev, void *arg) {}

void error_cb(struct bufferevent *bev, short event, void *arg) {
    evutil_socket_t fd = bufferevent_getfd(bev);
    printf("fd = %u, ", fd);
    if (event & BEV_EVENT_TIMEOUT) {
        printf("Timed out\n"); // if bufferevent_set_timeouts() called
    } else if (event & BEV_EVENT_EOF) {
        printf("connection closed\n");
    } else if (event & BEV_EVENT_ERROR) {
        printf("some other error\n");
    }
    bufferevent_free(bev);
}
```



