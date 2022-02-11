# +
from RPA.Browser.Selenium import Selenium
import time
import os
from os import replace
import pandas as pd


browser=Selenium()
url='https://heycarson.com/task-catalog-browse/task-types/development'
if not os.path.exists('Output'):
    os.makedirs('Output')
    path_dload=(((os.getcwd()).replace('\\','\\\\'))+'\\Output')

demo_link_list=[]
desc_list=[]
task_list=[]

def all_scrap():
    for z in range(1,15):
        for i in range(1,10):
            browser.open_available_browser(url)
            browser.maximize_browser_window()
            for x in range(1,z):
                time.sleep(5)
                browser.click_element('//*[@id="page-results"]/div[2]/div/a[4]')
            time.sleep(5)   
            _new_path_='//*[@id="page-results"]/div[1]/div/div['+(str(i))+']/div/div/div[1]/a'
            browser.click_element(_new_path_)
            time.sleep(5)
            print("Page:-",(str(z)),"Title:-",(str(i)),browser.get_text('//*[@id="root"]/div[4]/div/div[1]/div[2]/h1'))
            task_list.append(browser.get_text('//*[@id="root"]/div[4]/div/div[1]/div[2]/h1'))
            print("Page:-",(str(z)),"Article:-",(str(i)),browser.get_text('//*[@id="root"]/div[4]/div/div[1]/div[5]/div[2]'))
            desc_list.append(browser.get_text('//*[@id="root"]/div[4]/div/div[1]/div[5]/div[2]'))               
            ele_status=browser.get_element_status('//*[@id="root"]/div[4]/div/div[1]/div[4]/div[1]/a')
            if ele_status['visible']==True:
                browser.click_element('//*[@id="root"]/div[4]/div/div[1]/div[4]/div[1]/a')
                r=browser.get_window_handles()
                browser.switch_window(r[1])
                demo_link=browser.get_location()
                print("Demo Link:-",demo_link)
                demo_link_list.append(demo_link)
            else:
                demo_link_list.append('nan')
            browser.close_browser() 
all_scrap()    

df = pd.DataFrame({'Task Name':task_list,'Description':desc_list,'Demo Links':demo_link_list})
df.to_csv('OUTPUT.csv')


# + active=""
#
# -


