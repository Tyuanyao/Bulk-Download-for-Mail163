# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import  WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import urllib.request
import re
import numpy as np
import time
import win32api
import win32con


def mattachs(upper,lower):
    pattern = r'(\d*)年(\d*)月(\d*)日'
    page = 1
    
    while 1:
    
        print('page', page)    
        mail_list = driver.find_elements_by_xpath("//*[@class='eO0']")    
        date = [each.get_attribute('title').split()[0] for each in mail_list]    
        date = [int(re.search(pattern,str).group(1))*1e4+int(re.search(pattern,str).group(2))*1e2
            +int(re.search(pattern,str).group(3)) for str in date]
        #    print(date)
    
        #Time range
        index = list(np.where((np.array(date)>=lower)*(np.array(date)<=upper)==1)[0])  
        #    print(index)
         
        if len(index)==0 and date[0]>upper:
            driver.find_element_by_xpath("//span[contains(text(),'下一页')]").click()
            page = page+1
            continue
        elif len(index)==0:
            break    
        # print(index)
    
        num = 0  #record the number of homework
    
        at_list_last = []    
    
        for ind in index:
            num = num+1
    #        print(num)
    
            mail=mail_list[ind]
            mail.click()  #click one email
    #        print('')
            time.sleep(1)    
    
            at_list = driver.find_elements_by_xpath("//*[@class='nui-txt-normal']")
            
            #the number of the attachments in this email
            add = len(at_list)-len(at_list_last)
            
                
            #download all the attachment if there is one
            if add and at_list[-1].text[0].isdigit():
                attach_num = int(at_list[-1].text[0])
                print("number of attachments: " , attach_num)
    
                #all the names of the attachments 
                names = driver.find_elements_by_xpath("//*[@class='dh0']")
                #all the links of the attachments 
                attach_urls = driver.find_elements_by_xpath("//*[@class='bU1']/a[@target='downloadFrame']")
                at_list_last = at_list
    
                for i in range(attach_num):
    
                    aurl = attach_urls[-i-1].get_attribute('href')
                    driver.get(aurl)
                    # print(aurl)
                    
                    name = names[-i-1].text
    
                    print(name + "downloaded")
            elif add and not(at_list[-1].text[0].isdigit()):
                at_list_last = at_list
                print("no attachment")
            else:
                print("no attachment")
    
            #返回
            back = driver.find_elements_by_xpath("//span[contains(text(),'返回')]")
            back[-1].click()
    
    
    
        driver.find_element_by_xpath("//span[contains(text(),'下一页')]").click()
        page = page+1
    
    print('finished')                       
    
if __name__ == '__main__':   
    
    #the path of your chromedriver
    chromedriver = "C:/Users/54312/AppData/Local/Google/Chrome/Application/chromedriver.exe"
    os.environ["webdriver.chrome.driver"] = chromedriver
    driver = webdriver.Chrome(chromedriver)
    driver.get("http://mail.163.com/")
    time.sleep(5)
    
    # switch to the interface of logging in  by account and password instead of QR code 
    driver.find_element(By.XPATH,"//*[@id='switchAccountLogin']").click()
    driver.switch_to.frame(driver.find_element_by_xpath("//*[@id='loginDiv']//iframe"))
    
    # locate in the account-box
    inputText=driver.find_element(By.XPATH,"//*[@id='account-box']//div[2]//input")
    
    inputText.send_keys("youracountname")
    
    password=driver.find_element(By.XPATH,"//*[@id='login-form']//div//div[3]//div[2]//input[2]") #定位到密码框
    password.send_keys("yourpassword") 
    
    password.send_keys(Keys.ENTER) 
    
    time.sleep(5)
    
    driver.find_element(By.XPATH,"//*[@title='收件箱']").click()
    
    time.sleep(5)
    
    
    ##set the time range
    lower = 20190628      #from
    upper = int(time.strftime("%Y%m%d", time.localtime()))  #to ,set now
    #upper = int(20181231)

    mattachs(upper,lower)
    

