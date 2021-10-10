
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from fake_useragent import UserAgent
from selenium.webdriver.chrome.options import Options
import os

import shutil

#from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys

from bs4 import BeautifulSoup

import subprocess
import time



class hkexscraping:

    def __init__(self):
        
        '''
        options = Options()
        options.headless = True 
        profile = webdriver.FirefoxProfile()
        profile.set_preference('browser.download.folderList', 2) # custom location
        profile.set_preference('browser.download.manager.showWhenStarting', False)
        profile.set_preference('browser.download.dir', '/home/Desktop/stock')
        profile.set_preference("browser.helperApps.neverAsk.saveToDisk","application/octet-stream")
        self.driver = webdriver.Firefox(firefox_profile = profile ,executable_path = './geckodriver')

        '''
        '''
        chrome_options = Options()
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox") # linux only
        chrome_options.add_argument("--headless")
        '''

        self.driver = webdriver.Chrome(executable_path = './chromedriver')
        
        
        self.page_html = ''
        self.current_url = None
        self.soup = None

    def driveInit(self,name):
        self.driver.get(name)

    def get_html(self):
        self.page_html = self.driver.page_source

    def tosoup(self):
        self.get_html()
        self.soup = BeautifulSoup(self.page_html, "html.parser")
        

    def explict_wait_click(self,xpath):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH,xpath))
            )
        except:
            self.driver.quit()
        element.click()

    def data_page(self):
        #key_ratio
        self.explict_wait_click('/html/body/div/div/div/div[2]/div[3]/main/div[2]/div/div/div[1]/sal-components/section/div/div/div/sal-components-quote/div/div[2]/div/div[2]/div/div[2]/div/sal-components-segment-band/div/div/mwc-tabs/div/mds-button-group/div/slot/div/mds-button[2]/label/input')
        #full_key_ratio
        self.explict_wait_click('/html/body/div/div/div/div[2]/div[3]/main/div[2]/div/div/div[1]/sal-components/section/div/div/div/sal-components-quote/div/div[2]/div/div[2]/div/div[2]/div[2]/sal-components-key-stats/div/div[2]/div/div/a')
        
        self.driver.switch_to.window(self.driver.window_handles[1]) # change to pop up window

        self.explict_wait_click('//*[@id="financials"]/div[2]/div/a/div')




class fileManager:

    def __init__(self,start = None,end = None):

        self.start_dir = start
        self.end_dir = end
        print(os.getcwd())
        print(os.chdir('/home/nasvirat'))
        print(os.getcwd())
    




    def iterateChangeloc(self,source,destination):

        for filename in os.listdir(source):
            if filename.endswith('.csv'):
                print(filename)
                shutil.move(os.getcwd() +'/Downloads/' + filename,os.getcwd() + '/'+ destination + '/' + filename)




def tocode(number): 
    
    if number < 10:
        return '0000' + str(number)
    if number > 9 and number < 100:
        return '000' + str(number)
    if number >99 and number < 1000:
        return '00' + str(number)
    if number > 999 and number <10000:
        return '0' + str(number)


if __name__ == "__main__":

    for i in range(10,11):
        bot = hkexscraping()
        bot.driveInit('https://www.morningstar.com/stocks/xhkg/' + tocode(i) +'/quote')
        bot.data_page()
        time.sleep(3)
        bot.driver.quit()
        del bot

    filebot = fileManager()

    filebot.iterateChangeloc('Downloads','Desktop/global_stock/hkex/data')




