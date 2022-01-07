from kaggle import kaggleBot
from time import sleep
import os

myUsername = os.getenv('KAGGLE_USERNAME')
myPassword = os.getenv('KAGGLE_PASSWORD')

def run(notebookLink, myUsername = myUsername, myPassword = myPassword):
    bot = kaggleBot()
    bot.start(myUsername, myPassword)
    sleep(3) # Allow the bot to start
    bot.runNotebook(notebookLink)
    sleep(5) # Allow the bot to end
    bot.end()

run('https://www.kaggle.com/ironicninja/daily-covid-19-interactive-plots')
run('https://www.kaggle.com/ironicninja/vaccination-progress-us-world')
run('https://www.kaggle.com/ironicninja/top-10-stocks-past-7-days')