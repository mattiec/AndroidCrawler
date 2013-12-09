import urllib2

# Where to store the apk files
path = "/home/sji933/project/operaRus/descriptions/"

index = 0

# Loop through pages using id number from 1 to 10032 (Number of pages)
# Opens that page number of the market
for i in range(2626, 10032):
	print "Page number: " + str(i)
	response = urllib2.urlopen("http://apps.opera.com/ru_ru/free_catalog.php?soft=bestsell&p=" + str(i))
	pageHTML = response.read()

	splitHTMLDownloadLinks = pageHTML.split("<li class=\"appItem\">")
	downloadLinks = []

	# Obtain each download link individually
	for string in splitHTMLDownloadLinks:
		downloadLink = string.split("\" class=\"appLink")[0]
		downloadLink = downloadLink[downloadLink.index("\"") + 1:]
		downloadLinks.append(downloadLink)

	downloadLinks = downloadLinks[len(downloadLinks) - 10:len(downloadLinks)]
	
	# Obtain description
	for link in downloadLinks:
		try:
			print link
			r = urllib2.urlopen(link)
			output = r.read()
			splitLink = link.split("/")
			appName = splitLink[len(splitLink) - 1].replace(".html", "")
						
			description = output.split("<article>")
		
			description = description[1].split("</article>")[0]
			description = description.replace("<h3>", "").replace("</h3>", "")
			description = description.replace("<li>", "").replace("</li>", "")
			description = description.replace("<p>", "").replace("</p>", "")
			description = description.replace("<br>", "").replace("</br>", "")			
			description = description.replace("<ol>", "").replace("</ol>", "")
			#print description	
			print appName
			app = open(path + appName + ".txt", "wb")
			app.write(description)
			app.close()

			index = index + 1
			print "App number: " + str(index)
		except:
			print "An error occurred reading the URL."
