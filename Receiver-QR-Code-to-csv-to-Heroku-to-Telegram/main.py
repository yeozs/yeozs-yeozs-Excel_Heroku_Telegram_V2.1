import csv
import cv2 #pip install opencv-python
import time
from pymongo import MongoClient #pip install pymongo
import os
import os.path
import telebot
from flask import Flask, request

#------------------------------------------------------------- 
#Below take in QR Code input from Camera

def video_reader_once():
    cam = cv2.VideoCapture(0)
    cam.set(3,640)
    cam.set(4,480)
    
    detector = cv2.QRCodeDetector()
    while True:
        _, img = cam.read()
        data, bbox, _ = detector.detectAndDecode(img)    #detect and decode
        if data:
            print("Login QR Code detected-->\n", data)
            f = open('database.csv','w+') #wipe previous csv file data
            f.close()
            with open('database.csv', 'a') as csvfile:
                #open 'database.csv' and add
              fieldNames = ['default']
              writer = csv.DictWriter(csvfile, fieldnames=fieldNames,escapechar=" " ,quoting=csv.QUOTE_NONE)
              writer.writerow({'default': data})
            break
        cv2.imshow("img", img)    
        if cv2.waitKey(1) == ord("Q"):
            break
    cam.release()
    cv2.destroyAllWindows()
    return data

#--------------------------------------------------
# here onwards is splitting data into respective files. 
def scan_database_to_respective_csv():
  def open_databasecsv_writeto_telegramcsv():
    with open('database.csv') as g:
      #print(g.read()) => do not print, else file read already!
      fieldNames = ['default']
      writer = csv.DictWriter(sqnexcel, fieldnames=fieldNames, escapechar=" " ,quoting=csv.QUOTE_NONE)
      writer.writerow({'default': g.read()})
      g.close()
      
  with open('database.csv') as f:
    first_line = f.readline()
    print(first_line)

    if first_line.startswith("Programme"):
      with open('sqnexcel.csv','w+') as sqnexcel:
        f.close()
        open_databasecsv_writeto_telegramcsv()

    elif first_line.startswith("PROG"):
      with open('126sqnexcel.csv','w+') as sqnexcel:
        f.close()
        open_databasecsv_writeto_telegramcsv()

    elif first_line.startswith("SAR"):
      with open('sarprogramme.csv','w+') as sqnexcel:
        f.close()
        open_databasecsv_writeto_telegramcsv()

    elif first_line.startswith("Good"):
      with open('flyingprogramme.csv','w+') as sqnexcel:
        f.close()
        open_databasecsv_writeto_telegramcsv()

#------------------------------    
#From here, functions defined. Time for real code running.
video_reader_once()
scan_database_to_respective_csv()

ans = input("\n\nAre all barcodes scanned? \n[If no, press Enter]\n[If yes, press 'y' and Enter]")
  
while ans.lower() != 'y':
  video_reader_once()
  scan_database_to_respective_csv()
  ans = input("\n\nAre all barcodes scanned? \n[If no, press Enter]\n[If yes, press 'y' and Enter]")

if(ans.lower() == 'y'):
  print('\n\nSending to Heroku......')
  os.remove('database.csv') 


#----------------------------------------
#OS system running after Heroku Login

os.system('heroku login -i') 
os.system('heroku git:clone -a squadronexcel') #items from Heroku cloned and new git file 'squadronexcel' created.
os.system('mv 126sqnexcel.csv flyingprogramme.csv sqnexcel.csv sarprogramme.csv Procfile requirements.txt squadronexcel')
os.chdir('squadronexcel')
print("Current working directory: {0}".format(os.getcwd()))
os.system('git init')
os.system('git status')
os.system('git add .')
os.system('git status')
os.system('git commit -am "make it better"')
os.system('git status')
os.system('git push heroku master')
os.system('heroku ps:scale web=1')
os.system('heroku ps')

#can heroku ps:scale web=0 at certain time everyday to save heroku space