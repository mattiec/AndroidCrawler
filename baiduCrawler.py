import urllib2

# Returns an array of the download url and the app description
# Paremeter appStoreURL is the url of the app on the market
def getDownloadURLAndDescription(appStoreURL):
	try:
		response = urllib2.urlopen(appStoreURL)
		html = response.read()
		index = html.index('download_url=\"')
		downloadURL = html[index:].split('\"')[1]
		print downloadURL
		return [downloadURL, html[html.index('description'):].split('\"')[2]]
	except urllib2.HTTPError:
		print "Error URL not found"
		return 0

# Crawls the app store
# Increments ID of apps on the market to go through all the apps on the market
# Calls downloadApp and downloadAppDescription to actually download the apk and description text
def crawlAndDownload():
	index = open('index.txt', 'rb')
	ind = int(index.read())
	index.close()

	#index = open('index.txt', 'wb')
        #index.write(str(ind + 1))
        #index.close()

	for i in range(ind, 9999999):
		print i

		index = open('index.txt', 'wb')
        	index.write(str(i + 1))
        	index.close()

		url = 'http://as.baidu.com/a/item?docid=' + str(i) + '/'
		downloadURL = getDownloadURLAndDescription(url)

		if(downloadURL and not downloadURL[0].replace(' ', '%20') == "http://gdown.baidu.com/data/wisegame/dc3de029ead61559/youdaocidian_4020200.apk"):
			downloadURLLink = downloadURL[0].replace(' ', '%20')
			fileName = downloadURLLink.split('/')[-1].split('.')[0]
			print fileName
			downloadApp(downloadURLLink, fileName)
			downloadAppDescription(downloadURL[1], fileName)

# Downloads the app description
# Paremeter contents is the description link string
# Parameter fileName is what to call the downloaded description file
def downloadAppDescription(contents, fileName):
	output = open('/home/sji933/project/baidu/descriptions/' + fileName + '.txt', 'wb')
	output.write(contents)
	output.close()

# Download the apk file of the app
# Paremeter url is the download link string
# Paremeter fileName is what to call the downloaded apk file
def downloadApp(url, fileName):
	file = urllib2.urlopen(url)
	output = open('/home/sji933/project/baidu/apps/' + fileName + '.apk', 'wb')
	output.write(file.read())
	output.close()

crawlAndDownload()
