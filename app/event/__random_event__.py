from typing import KeysView
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime
import time
import random
import requests
import threading
from driver_win.driver import driver
#from __read_story__ import read_story
from reaction.__like_post__ import like_post
from __like_comment__ import link_comment
from __notify__ import notify
from __open_chat__ import open_chat_meessage

def event_random():
    print("Event Random")

    list_event = ["story", "like_post", "like_comment", "notify", "open_chat", "time_line"]

    random_event = random.choice(list_event)

    if random_event == "story":
        #read_story()
        print('story')
    
    elif random_event == "like_post":
        like_post()
        print('like_post')
    
    elif random_event == "like_comment":
        link_comment()
        print('like_comment')
    
    elif random_event == "notify":
        notify()
        print('notify')
    
    elif random_event == "open_chat":
        open_chat_meessage()
        print('Open Chat Open with Comming Soon!')
    
    elif random_event == "time_line":
        scroll_random = random.uniform(4, 6)
        print("Timeline Scroll Monitor!!")
        for _ in range(int(scroll_random)):
            driver.execute_script("window.scrollBy(0, 180);")
            time.sleep(15)
    
    print("---------------3 sec-----------------")
    time.sleep(20)