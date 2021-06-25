from kaggle import kaggleBot
from time import sleep
import os

def run(username, password, notebookLink):
    bot = kaggleBot()
    bot.start(username, password)
    sleep(3) # Allow the bot to start
    bot.runNotebook(notebookLink)
    sleep(5) # Allow the bot to end
    bot.end()

run(os.getenv('KAGGLE_USERNAME'), os.getenv('KAGGLE_PASSWORD'), 'https://www.kaggle.com/ironicninja/bomb-party-dictionary-analysis')