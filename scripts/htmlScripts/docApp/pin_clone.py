# import IPython 

import os


from flask import Flask
from flask.ext.restless import APIManager
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, Text

app = Flask(__name__, static_url_path='')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pin.db'
db = SQLAlchemy(app)









#FileScript ==================


outputList = []
path= os.path.abspath(__file__)  # insert the path to the directory of interest

#Get and filter out all the html files in the current directory

#12 is the name of the python file
dirList=os.listdir(path[:-12])
for fname in dirList:
    name = fname
    if (name[-5:] == ".html"):
		outputList.append(path[:-12]+name)


print(outputList)


#FILE SCRIPT ==================












class Pin(db.Model):
    id = Column(Integer, primary_key=True)
    title = Column(Text, unique=False)
    image = Column(Text, unique=False)

#Todo DB
class Task(db.Model):
	id = Column(Integer, primary_key=True)
	title = Column(Text, unique=False)
	description = Column(Text, unique=False)


db.create_all()
api_manager = APIManager(app, flask_sqlalchemy_db=db)
api_manager.create_api(Pin, methods=['GET', 'POST', 'DELETE', 'PUT'])

@app.route('/')
def index():
    return app.send_static_file("index.html")


@app.route('/docs')
def docs():
	outPutString = ""
	htmlList= [] 

	for file in outputList:

		#Formatted for html
		outPutString = outPutString + "<a href='/'>" +  file + "</a> <br>"
		htmlList.append(file)

	print(outPutString)
	print(htmlList)
	return 	"<h2> Docs from current directory</h2> <br>" + outPutString + " <br> <h3> Listed Here </h3>"


if __name__ == '__main__':
#    IPython.embed()
    app.run()
