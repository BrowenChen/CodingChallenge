## Output a list of links. link(href=" ____ ")
## 




import os

outputList = []

path= os.path.abspath(__file__)  # insert the path to the directory of interest

#Get and filter out all the html files in the current directory
dirList=os.listdir(path[:-5])
for fname in dirList:
    name = fname
    if (name[-5:] == ".html"):
		outputList.append(name)


print(outputList)



# Converting all the html files in outputList into a link 

linkList = []
def convert():
	for file in outputList:
		print(file)
		
	return 0


convert()