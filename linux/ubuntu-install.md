### Ubuntu界面安装

#### 一、美化界面

1、更换安装软件源

```shell
sudo vim /etc/apt/sources.list
```

```
deb http://mirrors.aliyun.com/ubuntu/ focal main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ focal main restricted universe multiverse

deb http://mirrors.aliyun.com/ubuntu/ focal-security main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ focal-security main restricted universe multiverse

deb http://mirrors.aliyun.com/ubuntu/ focal-updates main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ focal-updates main restricted universe multiverse

deb http://mirrors.aliyun.com/ubuntu/ focal-proposed main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ focal-proposed main restricted universe multiverse

deb http://mirrors.aliyun.com/ubuntu/ focal-backports main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ focal-backports main restricted universe multiverse
```

2、安装工具

```shell
sudo apt-get install -y gnome-tweaks gnome-shell-extensions gnome-tweak-tool chrome-gnome-shell
```

3、卸载原生的dock

```shell
sudo apt-get autoremove --purge gnome-shell-extension-ubuntu-dock -y
```

4、下载gnome-dock

```shell
# 打开firfox，安装gnome浏览器插件
https://extensions.gnome.org
# 在火狐浏览器中直接点击ON安装其他的extension工具
User Themes
Dash to Dock
system-monitor
Removable Drive Menu
TopIcons Plus
Lock Keys
Workspace Indicator
Caffeine
Bing Wallpaper Changer
OpenWeather
Coverflow Alt-Tab
Drop down terminal
```

```shell
sudo apt-get install gtk2-engines-murrine gtk2-engines-pixbuf
#https://github.com/vinceliuice/Mojave-gtk-theme
#https://github.com/vinceliuice/McMojave-circle
https://www.pling.com/s/Gnome
```

5、安装deepin-wine

```shell
sudo apt-get install fonts-droid-fallback ttf-wqy-zenhei ttf-wqy-microhei fonts-arphic-ukai fonts-arphic-uming
git clone https://gitee.com/wszqkzqk/deepin-wine-for-ubuntu.git
./install_2.8.22.sh
wget https://mirrors.aliyun.com/deepin/pool/non-free/d/deepin.com.qq.im/deepin.com.qq.im_9.1.8deepin0_i386.deb
wget https://mirrors.aliyun.com/deepin/pool/non-free/d/deepin.com.wechat/deepin.com.wechat_2.6.8.65deepin0_i386.deb
sudo dpkg -i deepin.com.qq.im_9.1.8deepin0_i386.deb
sudo dpkg -i deepin.com.wechat_2.6.8.65deepin0_i386.deb
```
或者

```
wget -O- https://deepin-wine.i-m.dev/setup.sh | sh
sudo apt-get install deepin.com.wechat
sudo apt-get install deepin.com.qq.im
```

6、安装zsh和oh-my-zsh

```shell
# 安装
sudo apt-get install zsh
chsh -s /bin/zsh
sudo vim /etc/passwd # root和myself /bin/bash->/bin/zsh
sudo apt-get install git
sh -c "$(curl -fsSL https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
sudo reboot

sudo apt-get install autojump
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git $ZSH/plugins/zsh-syntax-highlighting
git clone git://github.com/zsh-users/zsh-autosuggestions $ZSH/plugins/zsh-autosuggestions

vim ~/.zshrc # 修改plugins=(git zsh-autosuggestions) 修改主题 ZSH_THEME="ys"
echo ". /usr/share/autojump/autojump.sh" >> ~/.zshrc
echo "source $ZSH/plugins/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh" >> ~/.zshrc
echo "source $ZSH/plugins/zsh-autosuggestions/zsh-autosuggestions.zsh" >> ~/.zshrc
source ~/.zshrc
# 卸载
sudo sh -c "$(curl -fsSL https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/uninstall.sh)"
sudo vim /etc/passwd # root和myself /bin/zsh->/bin/bash
```

#### 二、安装常用软件

1、安装输入法

```shell
https://pinyin.sogou.com/linux/
sudo dpkg -i xxx.deb
sudo apt install -f
sudo dpkg -i xxx.deb
# relogin
```

2、安装wps

```shell
https://www.wps.cn/product/wpslinux
sudo dpkg -i xxx.deb
```

3、安装网易云音乐

```shell
https://music.163.com/#/download
sudo dpkg -i xxx.deb
```

4、安装typora

```shell
https://www.typora.io/#linux
https://typora.io/linux/Typora-linux-x64.tar.gz
```

5、安装sublime3

```ini
# Package Control.sublime-settings
"channels":
[
	"http://cst.stu.126.net/u/json/cms/channel_v3.json"
]
# 注册码
—– BEGIN LICENSE —–
Michael Barnes
Single User License
EA7E-821385
8A353C41 872A0D5C DF9B2950 AFF6F667
C458EA6D 8EA3C286 98D1D650 131A97AB
AA919AEC EF20E143 B361B1E7 4C8B7F04
B085E65E 2F5F5360 8489D422 FB8FC1AA
93F6323C FD7F7544 3F39C318 D95E6480
FCCC7561 8A4A1741 68FA4223 ADCEDE07
200C25BE DBBC4855 C4CFB774 C5EC138C
0FEC1CEF D9DCECEC D3A5DAD1 01316C36
—— END LICENSE ——
# 中文输入
git clone https://github.com/lyfeyaj/sublime-text-imfix
sudo ./sublime-imfix
```

6、安装截图工具

```shell
sudo apt install flameshot
flameshot gui
# 可手动添加快捷键
```

7、安装录屏工具

```shell
sudo add-apt-repository ppa:maarten-baert/simplescreenrecorder
sudo apt-get update
sudo apt-get install simplescreenrecorder
```

8、图像编辑工具

```shell
sudo apt install gimp
```



#### 三、配置

1、vim配置

```shell
https://github.com/sickill/vim-monokai 
mv vim-monokai/colors ~/.vim/
git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim
```

```shell
# 安装字体
git clone https://github.com/powerline/fonts ~/.vim/bundle/vim-airline-fonts
./install.sh
```

```xml
set nocompatible
filetype off   

set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()

Plugin 'VundleVim/Vundle.vim'
Plugin 'tpope/vim-fugitive'
Plugin 'tpope/vim-rails.git'
Plugin 'bling/vim-airline'
Plugin 'Lokaltog/vim-easymotion'
Plugin 'rstacruz/sparkup', {'rtp': 'vim/'}
Plugin 'L9'
Plugin 'FuzzyFinder'

call vundle#end()
filetype plugin indent on

syntax enable
colorscheme monokai
set t_Co=256
set laststatus=2
if !exists('g:airline_symbols')
	let g:airline_symbols = {}
endif
let g:airline_symbols.space = "\ua0"
let g:airline_exclude_filename = []
let g:Powerline_symbols='fancy'
let g:airline_powerline_fonts=0
let Powerline_symbols='fancy'
let g:bufferline_echo=0
let g:airline_powerline_fonts = 1 
let g:airline_section_b = '%{strftime("%c")}'
let g:airline_section_y = 'BN: %{bufnr("%")}'
let g:airline#extensions#tavline#enabled = 1
```



#### 四、安装c语言编译环境

```
sudo apt install libssl-dev

wget https://cmake.org/files/v3.15/cmake-3.15.3.tar.gz
tar -xf cmake-3.15.3.tar.gz
cd cmake-3.15.3
./configure
make
sudo make install
sudo ln -s /usr/local/bin/cmake /usr/bin/cmake
```

```cpp
sudo apt install texinfo

wget https://ftp.gnu.org/gnu/termcap/termcap-1.3.1.tar.gz
tar -xf termcap-1.3.1.tar.gz
cd termcap-1.3.1
./configure
make
sudo make install

wget http://mirrors.ustc.edu.cn/gnu/gdb/gdb-10.1.tar.gz
tar -xf gdb-10.1.tar.gz
cd gdb-10.1
./configure
make
sudo make install
sudo ln -s /usr/local/bin/gdb /usr/bin/gdb
```

#### 五、安装常用的软件

1、安装docker

```shell
sudo apt-get remove docker docker-engine docker-ce docker.io
sudo apt-get update
sudo apt-get install -y apt-transport-https ca-certificates curl software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
sudo apt-get update
sudo apt-cache madison docker-ce
sudo apt-get install docker-ce=<VERSION>

sudo systemctl status docker
sudo systemctl start docker
sudo docker run hello-world

#vim /etc/docker/daemon.json
{
  "registry-mirrors": ["https://ohbxz313.mirror.aliyuncs.com"],
  "insecure-registries": []
}

sudo gpasswd -a ${USER} docker
sudo service docker restart
sudo chmod a+rw /var/run/docker.sock

sudo curl -L "https://github.com/docker/compose/releases/download/1.24.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```

2、安装alphine

```shell
docker pull alpine:3.10
// 更新apline为国内源
sed -i 's/dl-cdn.alpinelinux.org/mirrors.aliyun.com/g' /etc/apk/repositories
```

3、安装openresty

```
docker pull openresty/openresty:alpine

mkdir -p /opt/docker/nginx/conf.d /opt/docker/nginx/logs

docker run --name tmp-nginx -d openresty/openresty:alpine
docker cp tmp-nginx:/usr/local/openresty/nginx/conf/nginx.conf /opt/docker/nginx/nginx.conf
docker cp tmp-nginx:/etc/nginx/conf.d/default.conf /opt/docker/nginx/conf.d/www.conf
docker rm -f tmp-nginx

version: "3" 
services:
  nginx:
    container_name: nginx
    image: openresty/openresty:alpine
    restart: always
    ports:
      - 80:80
    volumes:
      - /opt/docker/html:/var/www/html
      - /opt/docker/nginx/nginx.conf:/usr/local/openresty/nginx/conf/nginx.conf
      - /opt/docker/nginx/conf.d:/etc/nginx/conf.d
      - /opt/docker/nginx/logs:/usr/local/openresty/nginx/logs
    working_dir: /var/www/html
```

4、安装crontab

```shell
docker run -dit --name cront-task alpine:3.10 /usr/sbin/crond -f -L /var/log/crond.log
```

5、安装redis

```shell
version: '3'
services:
  redis:
    container_name: redis
    image: redis:5.0.10-alpine3.12
    restart: always
    volumes:
      - /opt/docker/redis:/data
    ports:
      - 6379:6379
```

6、安装mysql

```shell
version: '3'
services:
  mysql:
    container_name: mysql
    image: mysql:8.0.23
    command: --default-authentication-plugin=mysql_native_password
    restart: always
    volumes:
      - /opt/docker/mysql/data:/var/lib/mysql
	  - /opt/docker/mysql/conf:/etc/mysql/conf.d
	  - /opt/docker/mysql/logs:/logs
	environment:
      - MYSQL_ROOT_PASSWORD=root
    ports:
      - 3306:3306
```

7、安装zookeeper+kafka

```shell
version: '3'
services:
  zookeeper:
    image: wurstmeister/zookeeper:latest
    ports:
     - 2181:2181
    environment:
      - ALLOW_ANONYMOUS_LOGIN=yes
  zookeeper-ui:
    container_name: zookeeper-ui
    image: juris/zkui:latest
    restart: always
    environment:
      - ZK_SERVER=zookeeper:2181
    links:
      - zookeeper
    depends_on:
      - zookeeper
    ports:
      - 9090:9090
  kafka:
    image: wurstmeister/kafka:latest
    ports:
      - 9092:9092
    environment:
      - KAFKA_ZOOKEEPER_CONNECT=zookeeper:2181
      - KAFKA_ADVERTISED_HOST_NAME=192.168.200.128
      - KAFKA_ADVERTISED_PORT=9092
    links:
      - zookeeper
    depends_on:
      - zookeeper
    volumes:
      - /opt/docker/kafka/etc/localtime:/etc/localtime
  kafka-manager:
    container_name: kafka-manager
    image: sheepkiller/kafka-manager:latest
    restart: always
    environment:
      - ZK_HOSTS=zookeeper:2181
      - APPLICATION_SECRET=123456
    links:
      - zookeeper
    depends_on:
      - zookeeper
    ports:
      - 9000:9000
```

8、安装rabbitMQ

```shell
version: '3' 

services:
  rabbitmq:
    container_name: rabbitmq
    image: rabbitmq:3.8.11-alpine
    restart: always
    volumes:
        - /opt/docker/rabbitmq:/var/lib/rabbitmq
    environment:
      - RABBITMQ_DEFAULT_USER=admin
      - RABBITMQ_DEFAULT_PASS=admin
    ports:
      - 5672:5672
      - 15672:15672
```

9、安装ELK+Kibana

> grep vm.max_map_count /etc/sysctl.conf
>
> vm.max_map_count=262144
>
> sysctl -w vm.max_map_count=262144

```
version: '3' 

services:
  elasticsearch:
    container_name: elasticsearch
    image: elasticsearch:7.1.1
    restart: always
    volumes:
      - /opt/docker/elasticsearch/data:/usr/share/elasticsearch/data
    environment:
      - ES_JAVA_OPTS=-Xms512m -Xmx512m
      - discovery.type=single-node
    ports:
      - 9200:9200
      - 9300:9300
  kibana:
    container_name: kibana
    image: kibana:7.1.1
    restart: always
    environment:
      - ELASTICSEARCH_URL:elasticsearch:9200
    links:
      - elasticsearch
    depends_on:
      - elasticsearch
    ports:
      - 5601:5601
```









