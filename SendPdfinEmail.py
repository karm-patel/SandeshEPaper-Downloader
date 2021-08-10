## credits: http://linuxcursor.com/python-programming/06-how-to-send-pdf-ppt-attachment-with-html-body-in-python-script
from socket import gethostname
from datetime import date
#import email
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import json
import sys

def send_email_pdf_figs(sender_email, sender_email_password,destination_email,
                        path_to_pdf, subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    server.login(sender_email, sender_email_password)
    # Craft message (obj)
    msg = MIMEMultipart()

    message = f'{message}\nSend from Hostname: {gethostname()}'
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = destination_email
    # Insert the text to the msg going by e-mail
    msg.attach(MIMEText(message, "plain"))
    # Attach the pdf to the msg going by e-mail
    # with open(path_to_pdf, "rb") as f:
    #     #attach = email.mime.application.MIMEApplication(f.read(),_subtype="pdf")
    #     attach = MIMEApplication(f.read(),_subtype="pdf")
    # attach.add_header('Content-Disposition','attachment',filename=str(path_to_pdf))
    # msg.attach(attach)
    # send msg
    server.send_message(msg)

dist = str(sys.argv[1])
sender = str(sys.argv[2])
password = str(sys.argv[3])
reciver = str(sys.argv[4])

pdf_path = name = str(dist)+"- "+str(date.today())+" Sandesh.pdf"
subject = "Sandesh-E-Paper"
mesage = "https://epaper-sandesh-pdf.s3.amazonaws.com/pdf/2021-08/1628537621.pdf"
destination = "karmasmart216@gmail.com"
send_email_pdf_figs(sender,password,reciver, pdf_path,subject,mesage)

#patelkarm077@gmail.com