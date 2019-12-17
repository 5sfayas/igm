from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
import sys
import os




class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')

    def closeBrowser(self):
        self.driver.close()

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com/")
        time.sleep(2)
        login_button = driver.find_element_by_xpath("//a[@href='/accounts/login/?source=auth_switcher']")
        login_button.click()
        time.sleep(2)
        user_name_elem = driver.find_element_by_xpath("//input[@name='username']")
        user_name_elem.clear()
        user_name_elem.send_keys(self.username)
        passworword_elem = driver.find_element_by_xpath("//input[@name='password']")
        passworword_elem.clear()
        passworword_elem.send_keys(self.password)
        passworword_elem.send_keys(Keys.RETURN)
        time.sleep(20)
        
        
if __name__ == "__main__":
    username = "you user name"
    password = "your password"

    ig = InstagramBot(username, password)
    ig.login()
    time.sleep(random.randint(20, 35))
    ig.prfile()

    hashtags = ['bnw', 'naturelovers', 'travelgram']
    tag = 0
    #random.shuffle(hashtags)
    for hashtags in hashtags:
        ig.like_photo(hashtags)
        ig.home()  
        ig.prfile()
    ig.closeBrowser()
    
    
    # os.system("shutdown /s /t 1")
    sys.exit()