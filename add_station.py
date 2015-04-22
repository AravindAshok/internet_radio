#This is to add the internet radio streams,
#the links to which are present in list.txt.
import os

f = file('link.txt','r')
for line in f:
	os.system("mpc add "+str(line))
os.system("mpc playlist")
f.close()
