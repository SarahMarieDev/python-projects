import os
import smtplib
import pandas
import random
import datetime as dt
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_email(recipient_email, message):
    my_email = "sarahschlueter99@gmail.com"
    password = "jeuykbiqygmdjtyb"

    msg = MIMEMultipart()
    msg['From'] = my_email
    msg['To'] = recipient_email
    msg['Subject'] = "Happy Birthday!"

    body = message
    msg.attach(MIMEText(body, 'plain'))

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
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
        first_name = row['name'].split()[0]   
        with open(f"letter_templates/{letter_template}") as file:
            message = file.read().replace("[NAME]", first_name)
            send_email(row.email, message)