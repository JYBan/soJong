import os
from flask import Flask, flash, render_template, request, url_for, redirect, send_from_directory
from werkzeug import secure_filename


UPLOAD_FOLDER = '/Users/Ban/Documents/STUDY/SoftwareCapstoneDesign/workspace/flasktest/uploads/'
ALLOWED_EXTENSIONS = set(['txt', 'csv', 'arff'])

app = Flask(__name__) 
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = 'ban'

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/uploads/<filename>')
def uploaded_file(filename):
	return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/', methods=['GET', 'POST'])
#@app.route('/<sensorList>', methods=['GET', 'POST'])
def upload_file():
	sensorList=[]
	dirs = os.listdir('/Users/Ban/Documents/STUDY/SoftwareCapstoneDesign/workspace/flasktest/uploads/')
	for file in dirs:
		if(file[0]!='.'):
			sensorList.append(file)
	if request.method =='POST':
		file = request.files['file']
		#return file.filename 
		#loggin.debug('uploading file '+file.filename)
		if file and allowed_file(file.filename):
			#content = file.read()
			#print content
			filename = secure_filename(file.filename)
			file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
			flash('File Uploaded')
			#return redirect(url_for('uploaded_file', filename=filename))
	return render_template('/index.html', sensorList=sensorList)
if __name__ == '__main__':
	app.run(debug=True)
