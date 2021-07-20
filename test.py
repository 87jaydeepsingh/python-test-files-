from flask import Flask, render_template, request
from pymysql import *
import os
from werkzeug import secure_filename
list=[]
app = Flask(__name__)

@app.route('/')
def fetch():
	dir_path = os.path.dirname(os.path.realpath(__file__)) 
	for root, dirs, files in os.walk("F:\\"): 
		for file in files:  
			if file.endswith('.html'): 
				list.append(root+'/'+str(file))
			if file.endswith('.py'): 
				list.append(root+'/'+str(file))
			if file.endswith('.mp3'): 
				list.append(root+'/'+str(file))
			if file.endswith('.mp4'): 
				list.append(root+'/'+str(file))
			if file.endswith('.pptx'): 
				list.append(root+'/'+str(file))
			if file.endswith('.docx'): 
				list.append(root+'/'+str(file))
	return render_template('test.html',rows=list)
        
@app.route('/execute',methods = ['POST', 'GET'])
def execute():
	if request.method == 'POST':
		file = request.form['sel']
		os.startfile(file)
		return render_template('test.html',rows=list,test="Done")

@app.route('/shut',methods = ['POST', 'GET'])
def shutdown():
        os.system('shutdown /p /f')

if __name__ == '__main__':
	app.run(host='192.168.43.179',port='1234')
