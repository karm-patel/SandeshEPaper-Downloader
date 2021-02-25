import sandeshEpaper.sandeshEpaper as paper

print("Welcome in Sandesh-E-paper Downloader")
print("select any district from below:")
with open("dist_list.txt","r") as fp:
	L = fp.readlines()
	for each in L:
		print(each,end=" ")
dist = input()
url = "https://sandeshepaper.in/"
paper.getEpaper(url,dist)