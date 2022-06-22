#To import pyautogui module
import pyautogui 
 
#To import time module
import time 
 
#To take screenshot after 5 seconds
time.sleep(5) 
 
#To take screenshot 
screenshot = pyautogui.screenshot() 
 
#To save the screenshot
#This image will be saved inside this directory
screenshot.save('image.png')  
 
#Will print a message in terminal, after taken the screenshot
print('screenshot taken.') 
