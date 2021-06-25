# Kaggle Shortcut

```kaggle.py``` contains the code for a bot allows you to:
* Run a notebook automatically

To use the bot, start by download the chrome driver <a href="https://chromedriver.chromium.org/downloads">here</a> and then changing ```my_webdriver_filepath``` in line 9 to your chrome driver's file path. Then, go to the bottom of the file and type in your kaggle username and password where ```my_username``` and ```my_password``` are located, respectively.

For running a notebook automatically, add the link to your notebook where ```my_notebook_link``` is.

As for scheduling your bot to run daily, if you are on Windows, then do the following: Open Task Scheduler -> Create Task -> Actions, New -> Change "Program Script" to the your python executable file ->  Add your python file name in "Add Arguments" -> Add the file path to your python file in "Start In" -> Change your triggers accordingly. There are different ways to use Task Scheduler, like in <a href="https://datatofish.com/python-script-windows-scheduler/">this article</a>. <a href="http://theautomatic.net/2020/11/18/how-to-schedule-a-python-script-on-a-mac/">This link</a> should work for mac users.
