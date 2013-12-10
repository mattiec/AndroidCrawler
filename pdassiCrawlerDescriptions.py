import urllib2

# Where to store the apk files
storeAPKpath = "/home/sji933/project/pdassi/descriptions/"

# Get download url
# Parameter appStoreURL is the url string of the actual app on the website
# Returns apk download url parsed in the html text of the page
def getDescription(appStoreURL):
	print appStoreURL
	try:
		response = urllib2.urlopen(appStoreURL)
		html = response.read()
		index = html.index("showDescription();\">")
		# Split from quotation mark of the apk download link
		description = html[index:].split("<a title=")[0]
		return description.replace("	", "").replace("<p>", "").replace("showDescription();\">", "")
	except:
		print "Error URL not found"
		return 0

def getDownloadURL(appStoreURL):
        try:
                response = urllib2.urlopen(appStoreURL)
                html = response.read()
                index = html.index('http://pdassi.de/util/')
                downloadURL = html[index:].split('\"')[0]
                print downloadURL
                return downloadURL
        except urllib2.HTTPError:
                print "Error URL not found"
                return 0

# Count up from 100000 to 999999 and download the HTML text 
def searchURLs():
	listOfURLs = [] 
	for i in range(121654, 999999):
		print i
		url = 'http://android.pdassi.de/' + str(i) + '/'
		downloadURL = getDownloadURL(url)
                if(downloadURL):
			fileName = downloadURL[downloadURL.index('?')+1:].split('.apk')[0]
			description = getDescription(url)
			saveDescription(description, fileName)
	print listOfURLs

# Write the apk file and store it
# Parameter url is the apk download link
# filename is what we're going to call the saved apk file
def saveDescription(contents, fileName):
	try:
		output = open(storeAPKpath + fileName + ".txt", "wb")
		output.write(contents)
		output.close()
	except:
		print "Could not download app. URL leads to 404 page."

searchURLs()
