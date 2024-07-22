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
from driver_win import driver

#function notify check
def notify():
    print("Check Notifications!")
    #driver.get('https://www.facebook.com/notifications')
    #time.sleep(5)
    try:
        new_notification = driver.find_element(By.XPATH, '//div[contains(@aria-label, "Notifications") and contains(@aria-label, "unread")]')
        if new_notification.is_displayed():
            print("You have new notifications!")
            driver.get('https://www.facebook.com/notifications')
            time.sleep(5)
        else:
            print("No new notifications.")
    
    except Exception as e:
        print("No new notifications.")
        return
#function first post like