# crawler

## 爬虫测试

>sudo easy_install pip   
>sudo pip install selenium    
>sudo  pip install pyquery   
>sudo pip install requests    
>sudo pip install pymysql   

### 1. 配置yum下载源：

在目录 /etc/yum.repos.d/ 下新建文件 google-chrome.repo
> vim /etc/yum.repo.d/google-chrome.repo
> 
在该文件中添加如下内容：

>[google-chrome]  
name=google-chrome   
baseurl=http://dl.google.com/linux/chrome/rpm/stable/$basearch   
enabled=1   
gpgcheck=1   
gpgkey=https://dl-ssl.google.com/linux/linux_signing_key.pub  

### 2. 安装google chrome浏览器：

> yum -y install google-chrome-stable  
> 
PS: Google官方源可能在中国无法使用，导致安装失败或者在国内无法更新，可以添加以下参数来安装：

> yum -y install google-chrome-stable --nogpgcheck
> 
或者gpgcheck=0
这样，google chrome就可在安装成功。

### 3、安装pip
>yum install python-pip
>
失败先安装yum -y install epel-release   
升级pip到9.0.3
>python -m pip install --upgrade pip   

升级失败
删除site-packages包中的pip-9.0.3.dist-info
重新执行
>python -m pip install --upgrade pip

### 4、安装虚拟界面
>yum install Xvfb   
>pip install PyVirtualDisplay   
https://blog.csdn.net/chengly0129/article/details/72229537
https://blog.testproject.io/2018/02/20/chrome-headless-selenium-python-linux-servers/

### 5、下载驱动

> wget https://chromedriver.storage.googleapis.com/2.36/chromedriver_linux64.zip 
> 
Linux下，把下载好的文件放在 /usr/bin 目录下就可以了。


### 6、安装其他包依赖
>sudo pip install selenium   
sudo pip install pyquery   
sudo pip install requests    
sudo pip install pymysql    


### 7、问题：
以上安装执行完成后，无法启动chrome，异常time out。添加以下解决
>chrome_options.add_argument('--disable-extensions')    
chrome_options.add_argument('--disable-gpu')    
chrome_options.add_argument('--no-sandbox')    
chrome_options.add_argument('--headless')     