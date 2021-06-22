# importing modules for the script
import easygui
import time

# taking input using dailog box
text = easygui.enterbox("What shall I remind")

# taking input for time after which user want to be reminded
wait_time = easygui.enterbox("In how many minutes?")

# typcasting locat_time into float
wait_time = float(wait_time)

# converting time into minutes
wait_time = wait_time * 60

# making program wait for wait_time or putting program into sleep for given time
time.sleep(wait_time)

# showing dialogBox about reminder
easygui.msgbox(text, title="Reminder" )
