# Alarm clock
import time
import random
import webbrowser
import os
import datetime


#function which takes the user input
def takeinput():
    timeformat = "%H:%M"
    while True:
        try:
            Alarm_Time = input("Please enter the time to play the Alarm. It should be in HH:MM format: ")
            validtime = datetime.datetime.strptime(Alarm_Time, timeformat)
        except:
            print("Looks like you didnt enter in the correct format. Please enter again")
            continue
        else:
            return Alarm_Time
            print('The time is set at: '+ Alarm_Time)
            break


#The input time is stored in the Alarm variable
Alarm = takeinput()


#defining the time variable
Time = time.strftime("%H:%M")


#Opening Text File which has the youtube links
with open("links.txt") as f:
    #take a url from the file and store it in link variable
    link = f.readlines()


#This loop checks the time for every 5 seconds
while  Time != Alarm:
    print("The time is " + Time)
    #defining the time variable
    Time = time.strftime("%H:%M")
    #This command prints the time for every 5 seconds in the command line
    time.sleep(5)


#This gets executed when the alarm time reaches and the link is opened in the webbrowser
if Time == Alarm:
    print("Its time to wake up!!!")
    #Chooses a random link from the link variable and stores in the random_video variable
    random_video = random.choice(link)
    #Opens the random_video link in the default webbrowser
    webbrowser.open(random_video)
