from sys import argv

#inputs
file_name = "URLlist.txt"
fileOpen = open(file_name)
write_file = "FirstParty.txt"
file_text = ""
tempStr=""
#count is optional. I use it to know the script is running
count=1
url_found=""

print "\r\nStarting process... \r\n\r\n"

#remove the comments on the print to get feedback
for line in fileOpen:
	print count
	count=count+1
	url_found = line
	if url_found.find("domain-x") != -1:
		file_text= file_text+url_found
		#print "found " + url_found
	#else:
		#print "not found " + url_found

#print file_text

writeResult = open(write_file, 'w')
writeResult.truncate()
writeResult.write(file_text)
writeResult.close()

