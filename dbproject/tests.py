from django.test import LiveServerTestCase

from selenium import webdriver
import time


class Hosttest(LiveServerTestCase):
    
    def test_home_page(self):
        executable_path = 'C:\Users\ludob\source\repos\IT6037_DataAccess-Management\dbproject\chromedriver.exe'
        print('EXECUTABLE PATH:')
        print(executable_path)

        options = webdriver.ChromeOptions() 
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        
        
        driver = webdriver.Chrome(options=options, executable_path=executable_path)
        url = self.live_server_url
        driver.get(url)

        time.sleep(5)

        assert driver.page_source.find('Kia Ora!')

        #assert " Home " in driver.title

    def test_home_page2(self):
        driver = webdriver.Chrome()
        options = webdriver.ChromeOptions() 
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        driver = webdriver.Chrome(options=options, executable_path='C:\Users\ludob\source\repos\IT6037_DataAccess-Management\dbproject\chromedriver.exe')
    
        url = self.live_server_url

        driver.get(url)

        time.sleep(5)

        assert driver.page_source.find('Kia Ora!')

        #assert " Home " in driver.title
