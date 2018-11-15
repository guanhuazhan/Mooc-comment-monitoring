# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from bs4 import BeautifulSoup
from email.header import Header
from email.mime.text import MIMEText
import smtplib
import time
import datetime
import os
import sys

url_now = 'http://www.icourse163.org/learn/HDU-1002598057?tid=1003257006#/learn/forumindex'
desired_capabilities = DesiredCapabilities.CHROME  # 修改页面加载策略
desired_capabilities["pageLoadStrategy"] = "none"  # 注释这两行会导致最后输出结果的延迟，即等待页面加载完成再输出

def get_receiver(date):
    week_day_dict = {
            0 : '1577016476@qq.com',
            1 : '1210281651@qq.com',
            2 : '842622641@qq.com',
            3 : '1799297035@qq.com',
            4 : '765748675@qq.com',
            5 : '592234752@qq.com',
            6 : '137088099@qq.com',}
    day = date.weekday()
    return week_day_dict[day]
     
def get_webInfo(url):
    #broswer = webdriver.Chrome(executable_path = "./drive/chromedriver.exe")
    broswer = webdriver.Chrome(executable_path = '/usr/local/bin/chromedriver')
    broswer.get(url)
    wait = WebDriverWait(broswer, 10)
    element = wait.until(EC.presence_of_element_located((By.XPATH, "//p[@class='f-fc9 f-pa reply']")))
    html_text = broswer.page_source
    broswer.quit()
    soup = BeautifulSoup(html_text, 'html.parser')
    li = soup.find('li',class_= 'u-forumli first')
    a = li.find('a')
    react = li.find('span',class_ = 'lb10 f-fc9')
    react_time = react.get_text(strip=True)
    year = react_time[1:5]
    month = react_time[6:8]
    day = react_time[9:11]
    today = year+'-'+month+'-'+day
    #p = li.find('p',class_='f-fc9 f-pa reply')
    #p_text = p.get_text(strip=True)[3]
    info_text = a.get_text(strip=True)
    info_link = url[:-18]+a.get('href') 
#        print(info_text)
#        print(url[:-18]+info_link)
#        print('\n')
    return info_text+'\n'+info_link+'\n'+today+'\n'

def send_email(title, article, receiver):
    host = 'smtp.zdq.space'
    user = 'hua@zdq.space'
    password = 'zgh324#@$'
    sender = user
    coding = 'utf8'
    
    message = MIMEText(article, 'plain', coding)
    message['From'] = Header(sender, coding)
    message['To'] = Header(receiver, coding)
    message['subject'] = Header(title, coding)
    try:
        mail_client = smtplib.SMTP_SSL(host, 465)
        mail_client.connect(host)
        mail_client.login(user, password)
        mail_client.sendmail(sender, receiver, message.as_string())
        mail_client.close()
        print('邮件已成功发送给：'+receiver)
    except Exception as e:
        print(e)
        
tmp = {'history':None}
def check():
    if(tmp['history']):
        history = tmp['history']
        now = get_webInfo(url_now)
        tmp['history'] = now
    else:
        tmp['history'] = get_webInfo(url_now)
        history = tmp['history']
        now = tmp['history']
    print(history)
    print(now)
    result = ''
    if history == now:
        pass
    else:
        print('发现更新')
        result += '--------------------------------------\n'
        result += now
        result += '--------------------------------------\n'
        
    if result != '':
        t = now.strip('\n')[-10:]
        t = datetime.datetime.strptime(t,'%Y-%m-%d')
        print('更新内容如下：'+result)
        send_email('快去mooc答题！！！',result,get_receiver(t))
   
def DeltaSeconds():
    SECONDS_PER_DAY = 24 * 60 * 60
    from datetime import datetime, timedelta
    curTime = datetime.now()
    period = timedelta(days = 0,hours = 6,minutes = 0,seconds = 0)
    desTime = curTime + period
    #desTime = curTime.replace(hour=20, minute=32, second=1, microsecond=0) 
    delta = desTime - curTime
    print(delta)
    skipSeconds = delta.total_seconds() % SECONDS_PER_DAY
    print("Must sleep %d seconds" % skipSeconds)
    return skipSeconds

#schedule.every().day.at("19:25").do(check)              
while True:
    check()
    print('\n休息！')
    s = DeltaSeconds()
    time.sleep(s)
    print('继续工作！！！')
