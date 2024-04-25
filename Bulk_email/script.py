import pandas as pd
import smtplib

# Sender details
SenderEmail = "Your email"
Password = "Your Password"

# Email access
e = pd.read_excel("Leads_email.xlsx")
emails = e['Emails'].values

#server setup and security
server = smtplib.SMTP("smtpout.secureserver.net", 465)
server.starttls()
server.login(SenderEmail, Password)
msg = f"Hello, This is a test Message"
subject = "Python Testing"
body = "Subject: {}\n\n".format(subject,msg)
for email in emails:
    server.sendmail(SenderEmail, Password, body)
server.quit()

