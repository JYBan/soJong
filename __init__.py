import os
from flask import Flask, flash, render_template, request, url_for, redirect, send_from_directory
from werkzeug import secure_filename

 
UPLOAD_FOLDER = '/Users/Ban/Documents/STUDY/SoftwareCapstoneDesign/workspace/flasktest/soJong/uploads/'
ALLOWED_EXTENSIONS = set(['txt', 'csv', 'arff'])

app = Flask(__name__) 
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = 'ban'



def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

# MAIN PAGE : SETTING
@app.route('/', methods=['GET', 'POST'])
def upload_file():

	# upload file
	if request.method =='POST':
		file = request.files['file']
		if file and allowed_file(file.filename):
			filename = secure_filename(file.filename)
			file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
			flash('File Uploaded')

	# get file list
	sensorList=[]
	dirs = os.listdir('/Users/Ban/Documents/STUDY/SoftwareCapstoneDesign/workspace/flasktest/soJong/uploads/')
	for file in dirs:
		if file[0]!='.':
			sensorList.append(file)

	return render_template('setting.html', sensorList=sensorList)



# SHOW RESULT
@app.route('/result', methods=['POST'])
def show_result():
	if request.method == 'POST':
		algo = request.form.getlist('algoCheck')
		# algo : two of u'hoeffdling', u'sgd' and u'naive' are in list. algo[0] = orange, algo[1] = gray
		sensor = request.form.get('sensorCheck')
		# sensor : It's not a list.
 		return render_template('showResult.html');
 	return render_template('error.html'), 404




@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html'), 404

if __name__ == '__main__':
	app.run(debug=True)
