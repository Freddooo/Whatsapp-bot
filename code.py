#import to get the webserver running
from selenium import webdriver
#import this for next stage, can be deleted now
from datetime import datetime
#import this to create the pauses
import time
#get the website
driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com')
#information necessary 
name = input("Who do you want to send it to?\n")
msg = input("What is the message?\n")
count = int(input("How many times do you want to send the message?\n"))
pause = int(input("After how many messages do you want a short pause?\n"))
length = int(input("How long is the pause?\n"))
#before you press enter here, make sure 
input("ready?")

#this finds the user you want to send it to and clicks on that name
user  = driver.find_element_by_xpath("//span[@title = '{}']".format(name))
user.click()
# You might need to change the name, 
# but for me this is the name for the text box
# This finds the text box so we can use it to send the message
text_box = driver.find_element_by_class_name('_3uMse')

x = 0
for i in range(1,count + 1):
    #This does not work, but it will make the code send the message till it gets a response
    #now = datetime.now()
    #tijd = now.strftime("%H:%M")
    #this pastes the message to the text box
    text_box.send_keys(msg)
    # You might need to change the name 
    # but for me this is the name for the send button
    # This finds the send button
    button = driver.find_element_by_class_name('_1U1xa')
    # The message will be send now
    button.click()
    # To make it a little less harmful for the reciever, you can add a pause per a certain amount of messages
    if i %pause == 0:
        time.sleep(length)
