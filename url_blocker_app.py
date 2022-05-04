# %WARNING this program will edit hosts file in your PC% 
# PATH of hosts file:-
# Windows OS:
#   C:\Windows\System32\drivers\etc\hosts
# Linux and Mac OS:
#   /etc/hosts

# importing libraries
import time, platform
from datetime import datetime as dt, time as tm

# defining constants and variables
HOST_PATH = (
    r'C:\Windows\System32\drivers\etc\hosts'
    if platform.uname() == "Windows"
    else "/etc/hosts"
)
# HOST_TEMP = r'give\full\path\to\dummy\hosts\file'
REDIRECT = '127.0.0.1'

website_list=["www.facebook.com","facebook.com","www.youtube.com", "www.instagram.com"]

while True:
    if tm(10,0) < dt.now().time() < tm(19,0):
        print("Working hours...")
        with open(HOST_PATH,'r+') as file:
            content=file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(REDIRECT+" "+ website+"\n")
    else:
        with open(HOST_PATH,'r+') as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
        print("Fun hours...")
    time.sleep(60)


# use HOST_TEMP if you are not confident enough to execute this code

# to run as background process 
# STEP 1: locate pythonw.exe in the python installation directory
# STEP 2: change extension of this program file as .pyw
# STEP 3: execute the file with admin permission

## to execute this file as process everytime on startup in windows:
# STEP 1: open task scheduler
# STEP 2: click on create task
# STEP 3: under General tab; fill out task name, file location, check "Run with highest privileges" and select configure for your windows version
# STEP 4: under Triggers tab; click new then for begin the task select "At startup" and click OK
# STEP 5: under Actions tab; select action as "Start a program" and enter path for this program file and click OK
# STEP 6: under Conditions tab; uncheck "Start the task only if the computer is on AC power"
# STEP 7: click OK

## to execute this file as process everytime on startup in Mac or Linux:
# STEP 1: in terminal type; sudo crontab -e
# STEP 2: add this line at end; @reboot python <absolute path to your program file>
# STEP 3: save and exit crontab