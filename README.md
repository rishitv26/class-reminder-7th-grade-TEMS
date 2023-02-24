# class-reminder-7th-grade-TEMS
A little reminder which will run in the background to remind you about anything you would like to do if your a TEMS 7th grader student.


## How to calibrate to your needs:

Please enter in your email id in the first line of the credentials/cred.txt file, the enter your password for your gmail account right under it. Then, make a note in your google keep application called "TODO DURING ADVISORY", and get its id which is usually the gibberish after https://keep.google.com/u/2/#NOTE/(where the id is)/. Take that id and add it right under the password. Your calibration is complete :)

Note: If you virtual envoirment is not a virtualenv envoirment, you will have to install _**gkeepapi**_ and _**plyer**_ modules.

## How to get it working:

you must have:
- Pycharm
- Python
- Your own Gmail account (on google)

installed on your computer before running the procedure. 

First, please run the file by CLICKING on the file itself, not the .bat file, so this way you can install the neccessary modules for the app.
On Initial startup, you must know you venv file's site packages absolute path which the app will prompt you on initial setup. It usually is the 
current path of venv folder/Lib/site-packages. You will have to rerun the file afterwards to get it to start up. Note that it will throw some errors 
after saying "SHUTTING APP DOWN... (please reopen to use)", which is not a problem, just ignore them.

If you want it to run in the background, please click on the .bat file to do so, to close it, go to the task manager and kill the python app task.

## How to use it:

It will prompt you to plan your TODO note, which needs to be done in a specific structure.
it goes like this:

WORK: (some float)m

for example:

JAN_WORK: 15m

note that you must translate your time you want to comeplete in in minutes.
it will then loop through all your tasks and remind you after the givin time.
