import urllib2

# Where to store the apk files
path = "/home/sji933/project/operaRus/apps/"

index = 0

# Loop through pages using id number from 1 to 10032 (Number of pages)
for i in range(3280, 10032):
	print "Page number: " + str(i)
	# Open up that page of the website
	response = urllib2.urlopen("http://apps.opera.com/ru_ru/free_catalog.php?soft=bestsell&p=" + str(i))
	pageHTML = response.read()

	# Splitting the download links on the page
	splitHTMLDownloadLinks = pageHTML.split("http://apps.opera.com/ru_ru/download_0/")
	downloadLinks = []

	for string in splitHTMLDownloadLinks:
		downloadLink = "http://apps.opera.com/ru_ru/download_0/" + string.split("apk")[0] + "apk"
		downloadLinks.append(downloadLink)

	downloadLinks = downloadLinks[len(downloadLinks) - 10:len(downloadLinks)]
	# Saving each download link individually
	for link in downloadLinks:
		print link
		try:
			r = urllib2.urlopen(link)
			output = r.read()
			# Checks to see if it is an html page or an apk file
			htmlRedirect = output.find("DOCTYPE html")
			otherHTMLRedirect = output.find("<html")
			appNotFound = output.find("<!doctype html>")
			
			if htmlRedirect < 0 and appNotFound < 0 and otherHTMLRedirect:
				splitLink = link.split("/")
				appName = splitLink[len(splitLink) - 1]
				
				print appName
				app = open(path + appName, "wb")
				app.write(output)
				app.close()

				index = index + 1
				print "App number: " + str(index)
			else:
				print "Warning: Invalid app download link. This app link redirected to an HTML page."
		except:
			print "An error occurred reading the URL."
