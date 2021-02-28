import os
cwd = os.getcwd()
os.system("sudo -H pip3 install -r requirements.txt")
os.system("sudo apt install cron")
dists = []
with open("dist_list.txt","r") as fp:
	L = fp.readlines()
	for each in L:
		dists.append(each.strip())
		#print(each,end=" ")

print(dists)
print("######### \nselect any district from above:\n")
while True:
	dist = input()
	if dist in dists:
		break
	print("enter valid district")

print("enter shedule time for which you want to download Sandesh daily!")
flg = 0
while flg==0:
	try:
		hours = int(input("enter hours(0-23):"))
		flg=1
	except:
		print("Incorrect range of hours")

flg=0
while flg==0:
	try:
		minitues = int(input("enter minitues(0-59):"))
		flg=1
	except:
		print("Incorrect range of minitues")

timeString = str(minitues)+" "+str(hours)+" * * *"
#timeString = "* * * * *"
display = " DISPLAY=:0.0\n"
command = " $(which python3) "+str(cwd)+"/download.py "+str(dist)+" "+str(cwd)+" >> ~/cron.log 2>&1\n"
try:
	with open("cronCommand.txt","x") as f:
		#f.write(timeString+display)
		f.write(timeString+command)
		#f.write(str(timeString)+" touch "+str(cwd)+"/new.txt\n")
except FileExistsError:
	print("in....")
	with open("cronCommand.txt","w") as f:
		#f.write(timeString+display)
		f.write(timeString+command)
		# f.write(str(timeString)+" touch "+str(cwd)+"/new.txt\n")

os.system("crontab cronCommand.txt")


