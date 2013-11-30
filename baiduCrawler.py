import urllib2

#returns an array of the download url and the app description
def getDownloadURLAndDescription(appStoreURL):
	try:
		response = urllib2.urlopen(appStoreURL)
		html = response.read()
		index = html.index('download_url=\"')
		downloadURL = html[index:].split('\"')[1]
		print downloadURL
		print html[html.index('description'):].split('\"')[2]
		return [downloadURL, html[html.index('description')].split('\"')[0]]
	except urllib2.HTTPError:
		print "Error URL not found"
		return 0

#crawls the app store and downloads the apps
def crawlAndDownload():
	for i in range(4505253, 4505254):
		print i
		url = 'http://as.baidu.com/a/item?docid=' + str(i) + '/'
		downloadURL = getDownloadURLAndDescription(url)
		if(downloadURL):
			downloadURLLink = downloadURL[0].replace(' ', '%20')
			fileName = downloadURLLink.split('/')[-1].split('.')[0]
			print fileName
			downloadApp(downloadURLLink, fileName)
			downloadAppDescription(downloadURL[1], fileName)

#downloads the app description
def downloadAppDescription(contents, fileName):
	output = open(fileName + '.txt', 'wb')
	output.write(contents)
	output.close()

#download the app given the url
def downloadApp(url, fileName):
	file = urllib2.urlopen(url)
	output = open(fileName + '.apk', 'wb')
	output.write(file.read())
	output.close()

crawlAndDownload()
