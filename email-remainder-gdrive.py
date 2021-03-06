import csv
import pandas as pd
import smtplib
from settings import SENDER_EMAIL, SENDER_PASS  # Email settings file (settings.py)
from datetime import date, datetime
import os
import time
import gspread
from oauth2client.service_account import ServiceAccountCredentials

email = 'admin@company.com' # This is the email that receive all notifications in our company 
now = date.today()
print('Today is ' + str(now))

# Message that will be sent via smtp
RENEW_MSG = '''
HI {},
Domain DUE to renew NEXT month.
Registrant is: {}
Due in less than 30 days.
Thanks,
COMPANY
'''

# Use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope) # YOU need a "client_secret.json" file in the same directory
client = gspread.authorize(creds)

# Find a workbook by name and open the first sheet
sheet = client.open("Hosting_Domains").sheet1 # Make sure you use the right name of your Google SpreadSheet here
list_of_hashes = sheet.get_all_values()

new_list = pd.DataFrame(list_of_hashes)
new_list.to_csv('my_csv.csv', index=False, header=False) # Creates a new csv file on my directory

with open('my_csv.csv') as csv_file: # Opens previosly created csv  
    csv_reader = csv.reader(csv_file, delimiter=',')
    next(csv_reader)

    smtp = smtplib.SMTP('mail.company.com') # You have to change it to your own email info
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    smtp.login(SENDER_EMAIL, SENDER_PASS)  # External file with mail and password in the same directory
    now = date.today()
    
    # This part may need SOME improvement
    for row in csv_reader:
        X, DOMAIN, EXPIRE, OWNER, REGISTRANT, HOSTING = row # Rows headers to iterate
        print(EXPIRE[0:7])
        ExpireDate = datetime.strptime(EXPIRE,"%Y-%m-%d")
        if (ExpireDate-datetime.now()).days < 30:  # EXPIRES next month
            msg = RENEW_MSG.format(DOMAIN, REGISTRANT)  # DOMAIN to renew & REGISTRANT
            subject = DOMAIN + ' - DUE to renew 30 days'
            print('Sent renew mail to: ' + DOMAIN)
        else:
           continue 

        email_msg = 'Subject: {} \n\n{}'.format(subject, msg)
        smtp.sendmail(SENDER_EMAIL, email, email_msg)

    smtp.quit()
