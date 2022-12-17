#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import sys
from selenium.webdriver.common.by import By
from time import sleep
from selenium import webdriver

os.path.dirname(sys.executable)
driver = webdriver.Chrome()


# In[2]:


import logging
import datetime
file = datetime.datetime.now()
file = "./logs/" + str(file).replace(" ", "_").replace(".","_").replace(":","_") + ".log" 
logging.basicConfig(filename=file, filemode='w', format='%(asctime)s - %(levelname)s - %(message)s',datefmt='%d-%b-%y %H:%M:%S')

# In[3]:


with open('credentials.txt') as f:
    roll_no = f.readline().strip();
    pwd = f.readline().strip();


# In[4]:


subj = []
with open('subjects.txt') as f:
    for subject in f.readlines():
        subj.append(subject.strip())


# In[5]:


with open('param.txt') as f:
    outer_loop_range = int(f.readline().strip())
    inner_loop_range = int(f.readline().strip())
    logs = int(f.readline().strip())


# In[ ]:



for j in range(outer_loop_range):
    try:
        driver.get('https://cumsdtu.in/registration_student/login/login.jsp?courseRegistration')
        user= driver.find_element(By.XPATH,"//input[@name='userName']")
        user.send_keys(roll_no)
        passw= driver.find_element(By.XPATH,"//input[@name='password']")
        passw.send_keys(pwd)
        login= driver.find_element(By.XPATH,"//input[@value='Log In']")
        login.click()
        sleep(4)
        try:
            note= driver.find_element(By.XPATH,"//*[contains(text(),' Course Registration is not open. Kindly visit later on.')]")
            logging.error('REG NOT OPEN')
            sleep(1)
        except:
            try:
                subj_elems = []
                save_btn = driver.find_element(By.XPATH,"//button[@class='narrow mat-button mat-save']")
                for subject in subj:
                    temp = driver.find_element(By.XPATH,"//*[contains(text(),'"+ subject+" Cr:4.0')]")
                    subj_elems.append(temp)
                for i in range(inner_loop_range):
                    try:
                        if(len(subj_elems) == 0):
                            quit()
                        for elem in subj_elems:
                            elem.click()
                            save_btn.click()
                            sleep(0.4)
                    except:
                      logging.error("Error while registering subject.")
            except:
                logging.error("Invalid subject codes. Try editing the subjects.txt file")
    except:
              logging.error("LOGIN ISSUE")


# In[ ]:




