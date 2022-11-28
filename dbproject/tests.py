from django.test import LiveServerTestCase
from django.core.management import call_command

from selenium import webdriver
import time



class Hosttest(LiveServerTestCase):
    
    def test_home_page(self):
        executable_path = r"C:\Users\ludob\source\repos\IT6037_DataAccess-Management\dbproject\chromedriver.exe"
        print('EXECUTABLE PATH:')
        print(executable_path)
        call_command("migrate")

        options = webdriver.ChromeOptions() 
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        
        
        driver = webdriver.Chrome(options=options, executable_path=executable_path)
        url = self.live_server_url
        driver.get(url)

        time.sleep(5)

        assert driver.page_source.find('Kia Ora!')

        #assert " Home " in driver.title

    def test_home_page2(self):
        executable_path = r"C:\Users\ludob\source\repos\IT6037_DataAccess-Management\dbproject\chromedriver.exe"
        driver = webdriver.Chrome()
        options = webdriver.ChromeOptions() 
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        driver = webdriver.Chrome(options=options, executable_path=executable_path)
    
        url = self.live_server_url

        driver.get(url)

        time.sleep(5)

        assert driver.page_source.find('Mia Ora!')

        #assert " Home " in driver.title
