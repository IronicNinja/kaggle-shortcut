from selenium import webdriver
from time import sleep
import time
import os
from dotenv import load_dotenv
import chromedriver_autoinstaller

load_dotenv()

class kaggleBot():
    def __init__(self):
        chromedriver_autoinstaller.install()
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--no-sandbox')
        self.driver = webdriver.Chrome(options=chrome_options)

    def fTry(self, path, elementType = "xpath", debug = True, stop = 0.5):
        c = 2
        sleep(stop)
        while True:
            try:
                if elementType.lower() == "xpath":
                    pathOutput = self.driver.find_element_by_xpath(path)
                elif elementType.lower() == "class":
                    pathOutput = self.driver.find_element_by_class_name(path)
                else:
                    raise Exception("elementType variable must be defined differently.")
                return pathOutput
            except Exception as e:
                if debug:
                    print(f"Initiating try #{c}. The error was: {e}")
                c += 1
                sleep(stop)

    def start(self, username, password):
        start = time.time()
        self.driver.get('https://www.kaggle.com/')
        self.fTry('//*[@id="site-container"]/div/div[1]/div[2]/div[2]/div[1]/a/button').click() # Login
        self.fTry('//*[@id="site-container"]/div[1]/div/form/div[2]/div/div[2]/a/li/div/span').click() # With email
        sleep(2)
        self.driver.find_elements_by_class_name('mdc-text-field__input')[0].send_keys(username) # Username
        sleep(1)
        self.driver.find_elements_by_class_name('mdc-text-field__input')[1].send_keys(password) # Password
        self.fTry('//*[@id="site-container"]/div[1]/div/form/div[2]/div[3]/button').click() # Login
        print(f"Bot started in {time.time()-start} seconds!")

    def runNotebook(self, notebookLink):
        start = time.time()
        self.driver.get(notebookLink)
        self.fTry('//*[@id="site-content"]/div[3]/div[2]/div[1]/div/a/button').click() # Edit
        self.fTry('//*[@id="site-content"]/div[2]/div[1]/div[2]/div[4]/div[1]/button', stop = 10).click() # Save Version
        self.fTry('//*[@id="site-content"]/div[2]/div[4]/div[1]/div/div[2]/button[1]').click() # Save
        print(f"Notebook has begun running. It took {time.time()-start} seconds.")

    def end(self):
        self.driver.quit()