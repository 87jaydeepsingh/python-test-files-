from flask import Flask, render_template, request
from pymysql import *
import os
from werkzeug import secure_filename
list=[]
app = Flask(__name__)
@app.route('/')
def new_student():
	dir_path = os.path.dirname(os.path.realpath(__file__)) 
	for root, dirs, files in os.walk("F:\\"): 
		for file in files:  
			if file.endswith('.html'): 
				list.append(root+'/'+str(file))
			if file.endswith('.py'): 
				list.append(root+'/'+str(file))
	return render_template('form.html',rows=list)

@app.route('/shutdown',methods = ['POST', 'GET'])
def shut():
        os.system('shutdown /p /f')
        
@app.route('/data',methods = ['POST', 'GET'])
def addrec():
	if request.method == 'POST':
		nm = request.form['Time']
		city = request.form['sel']
		f = request.files['file']
		f.save(secure_filename(f.filename))
        filename = secure_filename(f.filename)
        new_path = os.path.basename(filename)
                new="E:/Python Projects"+"/"+new_path
		os.startfile(new)
		return render_template('form.html',test="Done")
if __name__ == '__main__':
	app.run(host='192.168.43.179',port='1234')
