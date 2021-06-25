# Kaggle Shortcuts

Have a Kaggle notebook which you have to run every day to update? Tired of waking up in the morning and remembering to do that? Well, you've come to the right place.

<h2> How to use this code </h2>

```kaggle.py``` contains the code for a bot allows you to:
* Run a notebook automatically (to actually run, use ```notebook.py```)

To use the bot, start by download the chrome driver <a href="https://chromedriver.chromium.org/downloads">here</a>. You can then either create a ```.env``` file using ```example.env``` as a guideline or manually change the variables (chromedriver path, kaggle username, kaggle password).

For running a notebook automatically, add the link to your notebook where ```my_notebook_link``` is.

<h2> How to schedule a task to run daily (or some other time interval) </h2>

On Windows, do the following: Open Task Scheduler -> Create Task -> Actions, New -> Change "Program Script" to the your python executable file ->  Add your python file name in "Add Arguments" -> Add the file path to your python file in "Start In" -> Change your triggers accordingly. There are different ways to use Task Scheduler, like in <a href="https://datatofish.com/python-script-windows-scheduler/">this article</a>. 

<a href="http://theautomatic.net/2020/11/18/how-to-schedule-a-python-script-on-a-mac/">This link</a> should work for mac users.

<h2> Notes </h2>

* Notebooks will only run properly if they are not on Version 0 (i.e., they've been run at least once).

If you find any issues, please submit an issue or <a href="mailto:meevanzhang@gmail.com">email me</a>.
