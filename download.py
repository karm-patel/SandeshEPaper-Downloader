import sandeshEpaper.sandeshEpaper as paper
import sys
import os

dist = sys.argv[1]
cwd = sys.argv[2]
email = int(sys.argv[3])
url = "https://sandeshepaper.in/"
print("test....")
#os.system("touch aworking.txt")
paper.getEpaper(url,dist,cwd,email)
