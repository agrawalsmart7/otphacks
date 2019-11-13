import sys

remoteaddr = sys.argv[1]


def blockingIP(remoteaddr):
	block_ips = []
	count = 0
	data = ""
	with open("logs.log", "r") as file:
		
		ip_lists = file.readlines()
		
		
		counts = [ip.strip("\n") for ip in ip_lists]
		countnum = counts.count(remoteaddr)
		
		
		if countnum > 200:
			block_ips.append(remoteaddr)
	
		
			
	for ip in block_ips:
		if ip == remoteaddr:
			data = "Target server blocks the IP address"
	print (data)
blockingIP(remoteaddr)		
