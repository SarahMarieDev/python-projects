import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

my_email = "sarah_schlueter73@yahoo.com"
password = "vnlj qern quhq zzhy"

msg = MIMEMultipart()
msg['From'] = my_email
msg['To'] = "sarahschlueter99@gmail.com"
msg['Subject'] = "Hello"

body = "This is the message body."
msg.attach(MIMEText(body, 'plain'))

with smtplib.SMTP("smtp.mail.yahoo.com", 587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="sarahschlueter99@gmail.com",
        msg=msg.as_string()
    )

