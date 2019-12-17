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
        
       def home(self):
        driver = self.driver
        driver.get("https://www.instagram.com/")
        time.sleep(35)

    def prfile(self):
        driver = self.driver
        driver.get("https://www.instagram.com/fayas_akram/")
        time.sleep(20)

    def nav_user(self, user):
        """
        Navigates to a users profile page
        Args:
            user:str: Username of the user to navigate to the profile page of
        """
        driver = self.driver
        driver.get("https://www.instagram.com/" + user + "/")
        time.sleep(2)

    def like_photo(self, hashtag):
        driver = self.driver
        driver.get("https://www.instagram.com/explore/tags/" + hashtag + "/")
        time.sleep(12)
        # gathering photos
        pic_hrefs = []
        for i in range(1, 4):
            try:
                driver.execute_script("window.scrollTo(0, (document.body.scrollHeight)/2);")
                time.sleep(2)
                # get tags
                hrefs_in_view = driver.find_elements_by_tag_name('a')
                # finding relevant hrefs
                hrefs_in_view = [elem.get_attribute('href') for elem in hrefs_in_view
                                 if '.com/p/' in elem.get_attribute('href')]
                # building list of unique photos
                [pic_hrefs.append(href) for href in hrefs_in_view if href not in pic_hrefs]
                print("Check: pic href length " + str(len(pic_hrefs)))

            except Exception:
                continue

        # Liking photos
        unique_photos = len(pic_hrefs)
        # reverse array to like
        #pic_hrefs.reverse()
        # shuffle array to like
        random.shuffle(pic_hrefs)
        lk = 0
        for pic_href in pic_hrefs:
            print("Check: getting photo to like")
            print("links " + pic_href)
            time.sleep(random.randint(2, 8))
            lk = lk + 1
            driver.get(pic_href)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(random.randint(2, 10))
            liked = unique_photos - 1
            pro = driver.find_element_by_xpath('//a[@class="FPmhX notranslate  nJAzx"]')
            # get user names that liked
            b = pro.get_attribute('title')
            print("User Profile Name " + b)
            #rd = range(2, 5)
            if lk <=4:
                #pro.click()
                self.nav_user(b)
                time.sleep(2)
                self.finduserpics(random.randint(2, 4))
                print("User Profile Liked " + b)
            if liked == 14:
                break
            try:
                like_button = lambda: driver.find_element_by_xpath('//span[@aria-label="Like"]').click()
                like_button().click()
            except Exception as e:
                time.sleep(2)
            unique_photos -= 1

    def like_latest_posts(self, user, n_posts, like=True):
        """
        Likes a number of a users latest posts, specified by n_posts.
        Args:
            user:str: User whose posts to like or unlike
            n_posts:int: Number of most recent posts to like or unlike
            like:bool: If True, likes recent posts, else if False, unlikes recent posts
        TODO: Currently maxes out around 15.
        """

        action = 'Like' if like else 'Unlike'

        self.nav_user(user)
        # self.driver.get(self.nav_user_url.format(user))

        imgs = []
        imgs.extend(self.driver.find_elements_by_class_name('_9AhH0'))

        for img in imgs[:n_posts]:
            img.click()
            time.sleep(1)
            try:
                self.driver.find_element_by_xpath('//span[@aria-label="Like"]').click()
            except Exception as e:
                print(e)

    def finduserpics(self, n_posts):
        love = 0
        imgs = []
        imgs.extend(self.driver.find_elements_by_class_name('_9AhH0'))

        for img in imgs[:n_posts]:
            img.click()
            time.sleep(random.randint(4, 7))
            self.driver.find_element_by_xpath('//span[@aria-label="Like"]').click()
            random.randint(2, 4)
            while love !=n_posts:
                time.sleep(2)
                love = love + 1
                arrow = self.driver.find_element_by_xpath('//a[@class="HBoOv coreSpriteRightPaginationArrow"]')
                arrow.click()
                time.sleep(random.randint(4, 8))
                try:
                    self.driver.find_element_by_xpath('//span[@aria-label="Like"]').click()
                except Exception as e:
                    print(e)
            break
        
        
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