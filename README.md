# Mooc-comment-monitoring
monitoring the update of course comments

## 功能：
* 监控mooc固定课程页面的评论区更新
* 每隔三小时刷新一次界面
* 信息更新之后通过邮件通知相应的用户
* 根据页面显示日期，循环通知不同的用户

## 安装：
* python 3.6
* ubuntu 18.04
* google chrome 70.0
* chromedriver v2.42
* Xvfb

## 说明：
1. 下载代码到本地
```sh
git clone https://github.com/guanhuazhan/Mooc-comment-monitoring.git
```
2. 安装chrome 70.0
```sh
sudo apt-get install libxss1 libappindicator1 libindicator7
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo dpkg -i google-chrome*.deb
```
安装后确认/usr/bin目录下是否有google-chrome文件

3. 安装chromedriver

点击链接下载linux v2.42版chromedriver [chromedriver下载链接](http://chromedriver.storage.googleapis.com/index.html)

安装chromedriver
```sh
unzip chromedriver_linux64.zip
chmod +x chromedriver
sudo mv -f chromedriver /usr/local/share/chromedriver
sudo ln -s /usr/local/share/chromedriver /usr/local/bin/chromedriver
sudo ln -s /usr/local/share/chromedriver /usr/bin/chromedriver
```
安装后确认/usr/bin目录下是否有chromedriver文件

4. 字符界面运行
```sh
sudo apt-get -y install xvfb gtk2-engines-pixbuf
sudo apt-get -y install xfonts-cyrillic xfonts-100dpi xfonts-75dpi xfonts-base xfonts-scalable
Xvfb -ac :99 -screen 0 1280x1024x16 & export DISPLAY=:99
```
5. 下载相关包

    缺啥下啥:blush:




