from selenium import webdriver
import time
#addyour username and password here
username = 'your@gmail.com'
password = 'password123'

#the name of your institution
url = 'https://www.yourinstitution.com/login'

from selenium.webdriver.chrome.options import Options

options = webdriver.ChromeOptions()
options.add_argument("C:/Users//acer/AppData/Local/Google/Chrome/User Data/Default")
driver = webdriver.Chrome(executable_path=r'C:/Users/acer/Downloads/chromedriver', chrome_options=options)
driver.get(url)

#the email password element may differ check by using developer tools
driver.find_element_by_id('email').send_keys(username)
driver.find_element_by_id('password').send_keys(password)

time.sleep(2)
#previous comment here too
driver.find_element_by_css_selector('button[type=submit]').click()

time.sleep(2)
#here again
driver.find_element_by_link_text('Join Now').click()
#activates the built-in xbox game bar recorder
import pyautogui
pyautogui.keyDown('win')
pyautogui.keyDown('alt')
pyautogui.keyDown('r')
pyautogui.keyUp('win')
pyautogui.keyUp('alt')
pyautogui.keyUp('r')
