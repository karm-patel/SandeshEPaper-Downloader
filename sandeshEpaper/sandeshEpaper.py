import requests
from bs4 import BeautifulSoup
from pathlib import Path
from datetime import date 

	


class sandeshEpaper:

	@staticmethod
	def getResponse(url):
		return requests.get(url)

	@staticmethod
	def getEpaper(url,dist):

		#html content of URL
		webConetnt = sandeshEpaper.getResponse(url).content
		soap = BeautifulSoup(webConetnt)
		sections = soap.find_all("section",{"class":"col-md-4 col-sm-6 epost epost-home"})

		a_tag = "empty"
		for each in sections:
		    
		    if each.find('time').contents[0].lower() == dist.lower():
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

			name = str(dist)+"- "+str(date.today())+" by Karm"
			filename = Path(name)
			filename.write_bytes(response.content)
			print("sucessfully downloaded")
			return 0