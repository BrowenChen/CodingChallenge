# For samir
import webbrowser
from pattern.web import URL


from bs4 import BeautifulSoup, SoupStrainer
import urllib2

slideLinks = []




def getLinks():
	url = 'http://www-inst.cs.berkeley.edu/~cs161/sp14/slides/'
	data = urllib2.urlopen(url).read()

	page = BeautifulSoup(data,'html.parser')

	for link in page.findAll('a'):
	       l = link.get('href')
	       if (l[0:1].isdigit()):
				# print("true")
				print l 
				slideLinks.append(l)


getLinks()


#open up the url's
def scoreSheet():
	for x in range(65, 80):
		scoreUrl = "http://openeducationchallenge.eu/sites/default/files/Phase3Results/OECPhase3Results_" + str(x) + ".pdf"
		webbrowser.open_new_tab(scoreUrl)


#Now download and store them into samples/ folder

def store(destUrl, destName):
	# scoreUrl = "http://openeducationchallenge.eu/sites/default/files/Phase3Results/OECPhase3Results_72.pdf"
	scoreUrl = destUrl

	url = URL(scoreUrl)
	f = open(destUrl[-8:], 'wb')

	print(url)
	f.write(url.download())
	print("downloading")
	f.close()
	print("Finished downloading")
	#

#Parse the data

store("http://openeducationchallenge.eu/sites/default/files/Phase3Results/OECPhase3Results_72.pdf", "OED" + "32" + '.pdf')

# for slides in slideLinks:
#		destUrl = "http://www-inst.cs.berkeley.edu/~cs161/sp14/slides/" + slides
#		print(destUrl)
#		store(destUrl, slides)
store("http://www-inst.cs.berkeley.edu/~cs161/sp14/slides/1.24.Safety.pdf", "safety.pdf")
# for slides in slideLinks:
	

#	store(destUrl, slides)


