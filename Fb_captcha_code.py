
# fb crawling module 1

# 

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pycurl
from StringIO import StringIO
import urllib

driver = webdriver.Firefox()
driver.get("https://www.facebook.com/directory")


# check if security page found

if(driver.title =="Security Check Required"):
    print("Captcha entry is required")
    driver.find_element_by_xpath("/html/body/div/div[2]/div[1]/div/form/div/div[3]/a[2]").click()    
    


#download mp3 file from extracted url

captcha_audio_href = driver.find_element_by_xpath("/html/body/div/div[2]/div[1]/div/form/div/div[5]/div/a").get_attribute("href")


urllib.urlretrieve (captcha_audio_href, "audio.mp3")








