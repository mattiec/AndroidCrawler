import urllib2

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

def searchURLs():
	listOfURLs = [] 
	for i in range(0, 999999):
		url = 'http://android.pdassi.de/' + str(i) + '/'
		downloadURL = getDownloadURL(url)
		if(downloadURL):
			downloadURL = downloadURL.replace(' ', '%20').replace('amp;', '')
			fileName = downloadURL[downloadURL.index('?')+1:].split('.apk')[0]
			listOfURLs.append(downloadURL)
			downloadApp(downloadURL, fileName)

	print listOfURLs

def downloadApp(url, fileName):
	file = urllib2.urlopen(url)
	output = open(fileName + '.apk', 'wb')
	output.write(file.read())
	output.close()


searchURLs()