import smtplib
import random
import datetime as dt
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_email(quote):
    my_email = "sarah_schlueter73@yahoo.com"
    password = "vnlj qern quhq zzhy"

    msg = MIMEMultipart()
    msg['From'] = my_email
    msg['To'] = "sarahschlueter99@gmail.com"
    msg['Subject'] = "Monday Motivation"

    body = quote
    msg.attach(MIMEText(body, 'plain'))

    with smtplib.SMTP("smtp.mail.yahoo.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="sarahschlueter99@gmail.com",
            msg=msg.as_string()
        )


with open("quotes.txt", "r") as file:
    lines = file.readlines()
    random_line = random.choice(lines)

day_of_week = dt.datetime.now().weekday()
if day_of_week == 6:
    send_email(random_line)
