import requests
from bs4 import BeautifulSoup
from plyer import notification
from pathlib import Path
from datetime import date 
import os
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

	


class sandeshEpaper:

	@staticmethod
	def getResponse(url):
		return requests.get(url)

	@staticmethod
	def notify(dist):
		title = 'Hey buddy!'
		message= 'Your sandesh-E-paper of '+str(dist)+" downloaded!"
		notification.notify(title= title,
                    message= message,
                    app_icon = "/home/kinetic/Downloads/IMG_3984-min-compressed (1).jpg",
                    timeout= 10,
                    toast=False)
	@staticmethod
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

	@staticmethod
	def getEpaper(url,dist,cwd,email):
		#print("dist",dist)

		#html content of URL
		
		webConetnt = sandeshEpaper.getResponse(url).content
		if webConetnt:
			#print(webConetnt)
			soap = BeautifulSoup(webConetnt)
			sections = soap.find_all("section",{"class":"col-md-4 col-sm-6 epost epost-home"})

			a_tag = "empty"
			#print(sections)
			for each in sections:
			    print(each.find('time').contents)
			    if each.find('time').contents[0].lower().strip() == str(dist).lower():
			        a_tag = each.find("a")
			        print(a_tag)
			        break
			if a_tag == "empty":
				print("please enter valid district")
			else:

				next_address = a_tag.attrs['href']
				uniq_number = next_address.split("/")[-2]
				print(uniq_number)
				download_url = url+"download/"+uniq_number
				nextpage_conetnt = sandeshEpaper.getResponse(download_url).content

				print(download_url)
				soap = BeautifulSoup(nextpage_conetnt)

				a_tags = soap.find_all("a",style="text-decoration: none;")
				for i in a_tags:
				    if i.contents[0] == "Download Full Newspaper":
				        pdf_url = i.attrs["href"]
				        print(pdf_url)

				name = str(dist)+"- "+str(date.today())+" Sandesh.pdf"
				print(str(cwd))
				if email:
					with open(str(cwd)+"/mailinfo.txt","r") as fp:
						sender = fp.readline().strip()
						password = fp.readline().strip()
						reciver = fp.readline().strip()
					sandeshEpaper.send_email_pdf_figs(sender, password,reciver,name,name,pdf_url)

				print("downloading...")
				response = sandeshEpaper.getResponse(pdf_url)
				#response = "buffer testing"

				filename = str(cwd)+"/"+name
				filename = Path(filename)
				filename.write_bytes(response.content)
				print("sucessfully downloaded")
				#sandeshEpaper.notify(dist)
		else:
			print("webConetnt is empty")
			return 0
		
		

	
