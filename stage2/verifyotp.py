import sys

remoteadd = sys.argv[1]

with open("logs.log", "a") as file:
	file.write(str(remoteadd)+"\n")

with open("data.txt", 'r') as file:
	print file.readline().strip("\n")

