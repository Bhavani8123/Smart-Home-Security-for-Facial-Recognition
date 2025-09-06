import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


port = 587  # For starttls
smtp_server = "smtp.gmail.com"
sender_email = "suhaak123@gmail.com"
receiver_email = "suhaak123@gmail.com"
password ="ztfu wqgd ergb quox" #input("Type your password and press enter:")
message = """\
Subject: Hi there
<h1>Hello</h1>
This message is sent from Python."""

html = """\
<html>
  <head></head>
  <body>
    <p>Hi!<br>
       How are you?<br>
       Here is the <a href="http://www.python.org">link</a> you wanted.

       <img src='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSBJBwDlNrMq5Wj_l-vGaNPgVONr-Zvoh_kZQ&s'/>
    </p>
  </body>
</html>
"""

part2 = MIMEText(html, 'html')



msg = MIMEMultipart('alternative')
msg['Subject'] = "Link"
msg['From'] = sender_email
msg['To'] = receiver_email

msg.attach(part2)


#ztfu wqgd ergb quox

context = ssl.create_default_context()
with smtplib.SMTP(smtp_server, port) as server:
    server.ehlo()  # Can be omitted
    server.starttls(context=context)
    server.ehlo()  # Can be omitted
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, msg.as_string())