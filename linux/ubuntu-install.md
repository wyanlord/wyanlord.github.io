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











