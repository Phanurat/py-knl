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
import time
import random
from driver_win import driver
from api.__get_link__ import get_random_link
from api.__get_comment__ import get_random_comment
from reaction.__like_post__ import like_post
from reaction.__love_post__ import love_post
from reaction.__care_post__ import care_post
from reaction.__haha_post__ import haha_post
from reaction.__wow_post__ import wow_post
from reaction.__sad_post__ import sad_post
from reaction.__angry_post__ import angry_post

def link_comment():
    post_url = random.choice(get_random_link())
    driver.get(post_url)
    time.sleep(5)

    reaction_random = ["like", "love", "care", "haha", "wow", "sad", "angry", "not_reaction"]

    selected_reaction = random.choice(reaction_random)

    if selected_reaction == "like":
        like_post()
    elif selected_reaction == "love":
        love_post()
    elif selected_reaction == "care":
        care_post()
    elif selected_reaction == "haha":
        haha_post()
    elif selected_reaction == "wow":
        wow_post()
    elif selected_reaction == "sad":
        sad_post()
    elif selected_reaction == "angry":
        angry_post()

    time.sleep(5)

    try:
        xpaths = [
            '//div[@aria-label="Write a comment"]',
            '//div[@aria-label="Write a comment..."]',
            '//div[contains(@aria-label, "Write a comment")]',
            '//div[@role="textbox"]',
        ]
        comment_input = None
        
        for xpath in xpaths:
            try:
                comment_input = driver.find_element(By.XPATH, xpath)
                if comment_input:
                    break
            except:
                continue
        
        if not comment_input:
            raise Exception("No Comment")

        comment_input.click()
        time.sleep(2)
        
        # Random comment list
        comment_text = random.choice(selected_comment = get_random_comment)

        for char in comment_text:
            comment_input.send_keys(char)
            time.sleep(0.5)
        comment_input.send_keys(Keys.ENTER)

        print(f"Add comment '{comment_text}' Done!")

    except Exception as e:
        print(f"Can't Comment: {str(e)}")
        return
    
    print("Comment it Work!")
