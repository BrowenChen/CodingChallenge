# For samir
import webbrowser
rom pattern.web import URL
#open up the url's
def scoreSheet():
	for x in range(65, 80):
		scoreUrl = "http://openeducationchallenge.eu/sites/default/files/Phase3Results/OECPhase3Results_" + str(x) + ".pdf"
		webbrowser.open_new_tab(scoreUrl)


#Now download and store them into samples/ folder

def store():
	scoreUrl = "http://openeducationchallenge.eu/sites/default/files/Phase3Results/OECPhase3Results_72.pdf"

	url = URL(scoreUrl)
	f = open("OED" + str(num) + '.pdf', 'wb')
	f.write(url.download(cached=False))
	f.close()
	print("Finished downloading")
	#

#Parse the data

def parse():
	#
