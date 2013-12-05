import cookielib
import urllib
import urllib2

#login to the store with the login credentials 
cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
opener.addheaders = [('User-agent', 'Chrome')]
urllib2.install_opener(opener)
authentication_url = "http://blapkmarket.cz/en/login/?do=loginForm-submit"
payload = {"username": "mattiec", "password": "password"}
data = urllib.urlencode(payload)
req = urllib2.Request(authentication_url, data)
resp = urllib2.urlopen(req)
contents = resp.read()

#download path
path = "/home/sji933/project/blapkmarket/apps/"

#used to search keywords in the app store
keyword = "the"
#used to search by category in the app store
category = 0
#used to search number of items per page
itemsPerPage = 1000
#string of all the app downlaod links
outputString = ""

#loop through the 12 pages of apps that they store has
for page in range(1, 12):
	#req = urllib2.Request("http://blapkmarket.cz/en/?appList-goto=" + str(page) + "&search=" + keyword + "&appList-itemsPerPage=100&do=appList-page", data)
	print "Page number: " + str(page)
	#request for the page with the page number
	#gets 1000 apps per page
	req = urllib2.Request("http://blapkmarket.cz/en/?appList-goto=" + str(page) + "&appList-category=" + str(category) + "&appList-itemsPerPage=" + str(itemsPerPage) + "&do=appList-page")
	resp = urllib2.urlopen(req)
	#the contents of the page with all the urls
	contents = resp.read()
	#split the app links into download link list
	listOfApps = contents.split("title=\"Download\" href=\"")
	listOfAppNames = contents.split("title=\"\"></td>")
	#print listOfAppNames
	for i in range(1, len(listOfApps)):
		downloadURL = "http://blapkmarket.cz" + listOfApps[i].split("\"")[0].replace("amp;", "")
		appName = listOfAppNames[i].split("<td class=\"cell_text\">")[1].split("</td>")[0]
		
		#print the app name and the downloadURL
		print appName
		print downloadURL
		
		outputString = outputString + appName + "\n"
		
		try:		
			#download the application	
			fileRequest = urllib2.Request(downloadURL, data)
			file = urllib2.urlopen(fileRequest)			
			output = open(path + appName + ".apk", "wb")
			output.write(file.read())
			output.close()
		except:
			print "Warning the file name was no good and so this application was skipped it."

output = open("listOfApps.txt", "wb")
output.write(outputString)
output.close()
