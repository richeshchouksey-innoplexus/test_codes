
# coding: utf-8

# In[28]:

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import os
import time
import urllib
#from pymongo import MongoClient


# In[ ]:

# conn = MongoClient('localhost')
# db = conn.linkedin
# top_links = db.top_links
# sub_links = db.sub_links


'''
things not done
    1. session module
    
'''


# In[ ]:

driver = webdriver.Firefox()
driver.get("https://www.facebook.com/directory")


# # giving a-z and 0-25 toplinks
# 
# if(driver.title !="Security Check Required"):
#     for i in driver.find_elements_by_xpath("/html/body/div/div[2]/div[1]/div/div[4]/a"):
#         top_links.insert_one({'name':'i.text', 'link':'i.get_attribute('href')', 'visit':'False'})
# 
#     for i in driver.find_elements_by_xpath("/html/body/div/div[2]/div[1]/div/div[6]/a"):
#         top_links.insert_one({'name':'i.text', 'link':'i.get_attribute('href')', 'visit':'False'})
#      #mark A as TRUE initially

# In[ ]:

# TEST BLOCK
# storing href in list

top_links = []
if(driver.title !="Security Check Required"):
    for i in driver.find_elements_by_xpath("/html/body/div/div[2]/div[1]/div/div[4]/a"):
        top_links.append(i.get_attribute('href'))

    for i in driver.find_elements_by_xpath("/html/body/div/div[2]/div[1]/div/div[6]/a"):
        top_links.append(i.get_attribute('href'))
        
#     for i in top_links:
#         print i 
    


# In[ ]:

# TEST BLOCK
# directory for non server testing 

link_data = []
if(driver.title !="Security Check Required"):
    for i in driver.find_elements_by_xpath("/html/body/div/div[2]/div[1]/div/div[4]/a"):
        links_info = {}
        links_info['top_link'] = i.get_attribute('href')
        links_info['name'] = i.text
        links_info['visited'] = 'False'
        link_data.append(links_info)
    for i in driver.find_elements_by_xpath("/html/body/div/div[2]/div[1]/div/div[6]/a"):
        links_info = {}
        links_info['top_link'] = i.get_attribute('href')
        links_info['name'] = i.text
        links_info['visited'] = 'False'
        link_data.append(links_info)
    


# In[ ]:

# TEST BLOCK

for item in link_data:
    if item['top_link'] == 'https://www.facebook.com/directory/people/23':
        print item['name']


# In[ ]:

# TEST BLOCK

for i in link_data:
    while i['visited']=='False':
        k=0
        for j in driver.find_elements_by_xpath("/html/body/div/div[2]/div[1]/div[2]/div/div[2]/ul"):
            print k
            k=k+1
                


# In[ ]:

# server block

while top_links.find({'done':'False'},no_cursor_timeout=True):
    for b in top_links.find({'done':'False'},no_cursor_timeout=True):
        
# yet to work on try catch
#         while True:
#             try:
#                 driver.get(b['link'], verify=False, timeout=5)
#                 break
#             except Exception, e:
#                 pass
#         soup = bs(resp.content, 'lxml')
        while True:
            try:
                wait = WebDriverWait(driver, 10)
                wait.until(EC.presence_of_element_located(b['link']))
                break
            except Exception, e:
                pass
            
# done part
        for lis in driver.find_elements_by_xpath("/html/body/div/div[2]/div[1]/div[2]/div/div[2]/ul/li"):
            if '/directory/' in lis.find_element_by_tag_name("a").get_attribute("href"):
                top_links.insert_one({'name':lis.text,'link':lis.find_element_by_tag_name("a").get_attribute("href"), 'visit':'False'})
            else:
                sub_links.insert_one({'name':lis.text,'link':lis.find_element_by_tag_name("a").get_attribute("href")})
            
        top_links.update_one({'_id':b['_id']},{'$set':{'done':'True'}})
        


# In[ ]:

# testing block

for lis in driver.find_elements_by_xpath("/html/body/div/div[2]/div[1]/div[2]/div/div[2]/ul/li"):
    if '/directory/' in lis.find_element_by_tag_name("a").get_attribute("href"):
        links_info = {}
        links_info['top_link'] = lis.find_element_by_tag_name("a").get_attribute("href")
        links_info['name'] = lis.text
        links_info['visited'] = 'False'
        link_data.append(links_info)
# for i in link_data:
#     print i

