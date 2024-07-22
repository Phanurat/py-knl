from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from driver_win import driver
#emo love
def haha_post():
    try:
        print("Trying to haha a post...")
        # เลื่อนเมาส์ไปที่ปุ่มไลค์เพื่อให้ตัวเลือก reaction แสดงขึ้นมา
        haha_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@aria-label='Like']"))
        )
        actions = ActionChains(driver)
        actions.move_to_element(haha_button).perform()
        time.sleep(2)  # รอให้ตัวเลือก reaction แสดงขึ้นมา

        # รอให้ปุ่ม Haha แสดงขึ้นมาและคลิก
        haha_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@aria-label='Haha']"))
        )
        haha_button.click()
        print("Haha the post.")
    except Exception as e:
        print(f"Error haha post: {str(e)}")



