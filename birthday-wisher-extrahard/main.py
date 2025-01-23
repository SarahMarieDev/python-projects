##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.
import os
import smtplib
import pandas
import random
import datetime as dt
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_email(recipient_email, letter):
    my_email = "sarah_schlueter73@yahoo.com"
    password = "vnlj qern quhq zzhy"

    msg = MIMEMultipart()
    msg['From'] = my_email
    msg['To'] = recipient_email
    msg['Subject'] = "Happy Birthday!"

    body = letter
    msg.attach(MIMEText(body, 'plain'))

    with smtplib.SMTP("smtp.mail.yahoo.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=recipient_email,
            msg=msg.as_string()
        )


today = dt.datetime.now().month, dt.datetime.now().day
letter_template = random.choice([x for x in os.listdir("letter_templates")])

csv_data = pandas.read_csv("birthdays.csv")
for index, row in csv_data.iterrows():
     if (row.month, row.day) == today:
         print(row)