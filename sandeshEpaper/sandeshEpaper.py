import requests
from bs4 import BeautifulSoup
from plyer import notification
from pathlib import Path
from datetime import date 
import os
	


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
	def getEpaper(url,dist,cwd):
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

				print("downloading...")
				response = sandeshEpaper.getResponse(pdf_url)

				name = str(dist)+"- "+str(date.today())+" Sandesh.pdf"
				filename = Path(str(cwd)+"/"+name)
				filename.write_bytes(response.content)
				print("sucessfully downloaded")
				#sandeshEpaper.notify(dist)
		else:
			print("webConetnt is empty")
			return 0