# Excel_Heroku_Telegram_V2.0 [Improved Version of sqnexcel-Telegram-Bot-to-Heroku-V1.0]
Sending Excel data from a intranet computer to Telegram on Internet Computer
------------------------------------------------------
Reason for Creating Bot: Imagine a workplace with daily programme details stored in an intranet excel file. Everyday, individuals will manually grab particular details from the excel file, and type them into telegram to send to the main telegram group chat via the internet. This app aims to kick start a telegram bot that automates the process of grabbing certain details from the daily programme intranet excel file and uploading them to telegram via internet.

What is done by human?
- Run Sender side code
- Run Receiver side code
- Use barcode scanner(currently computer camera*2), scan QR codes from intranet excel to internet
- Login to Heroku Account when prompted by terminal*1
------------------------------------------------------
What folders are present?

Sender side:
- main.py: generate QR code from intranet excel. QR code found in excel.
- sqnexcel.xlsx => the prove of concept copy of real daily programme excel folder. It extracts details from a 'daily programme' called 'sheet 2' to form the foundations for a telegram message.

Receiver side:
- main.py: Use barcode scanner (currently computer camera) to get data from intranet excel QR code, automatically sends data to Telegram on internet.

Initial Heroku Documents [First set of documents to be pushed to Heroku]:
- main.py: Link Heroku to Telegram bot. Remember to insert token from BotFather into main.py at Line 6, TOKEN =
- Procfile and Requirements.txt are essential for Heroku to work.
- csv files are initial set of files. These will be automatically wiped clean and data replaced when Receiver side code is run.
------------------------------------------------------

How to use the application:

- Download all the files in git repository
- Set up telegram bot via BotFather in telegram. Insert token from BotFather into Initial Heroku Documents main.py at Line 6, TOKEN =
- Set up Heroku account at https://signup.heroku.com/
- Create a new Heroku app
- Download the Heroku Command Line Interface(CLI) at https://devcenter.heroku.com/articles/heroku-cli#download-and-install
- "pip install pyTelegramBotAPI && pip install flask". (Also: Pip install for other missing python libraries for sender/receiver side code)
- "heroku login" => follow pop up, login to your Heroku Account

Deploying Initial Heroku Documents to Heroku:
- Open Terminal
- Go to Heroku app 'Deploy' page and follow steps. Deploy initial heroku documents to Heroku.

Sender and Receiver side:
- Sender code should be stored in intranet computer in same folder as excel sheet in question. Except sheet 2, all other tabs in sqnexcel.xlsx should be integrated into excel sheet in question.
- Receiver side folder place in internet computer to receive barcode scans. Change line 95,96,97 'squadronexcel' to name of your Heroku app

Controlling Heroku from Terminal:
- To check free dyno quota remaining, type "heroku ps"
- To assign dyno to Telegram bot, type "heroku ps:scale web=1"
- To remove dyno assigned to Telegram bot, type "heroku ps:scale web=0"

------------------------------------------------------
Improvements from Version 1.0:
- Account for transfer of data from intranet to internet computer
- V1.0 runs on Replit. V2.0 is shown to run on Macbook, expected to run on Windows, Linux.

Drawbacks of this Telegram Bot:
- *1 Unable to automate step to login to Heroku at terminal. Do write to me on how to improve this step! :)
- *2 Current code uses computer camera and isnt configured for barcode scanner. Feel free to write to me on how to code for barcode scanner! :)
- Lack of security features. Do write to me on how to improve on security features! :)

Future improvements:
- Run python code in computer background. No need for user to open terminal and run code.
- Automatically login to Heroku. [considering using 'webbrowser' python library]
- Code for barcode scanner and not computer camera to gather QR code input.
