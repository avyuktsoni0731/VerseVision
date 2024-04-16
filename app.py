from flask import Flask, render_template, request, session
import os
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = os.path.join('static')
# # Define allowed files
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.secret_key = 'avyuktsoni0731'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/',  methods=("POST", "GET"))
def uploadFile():
    if request.method == 'POST':
        # Upload file flask
        uploaded_img = request.files['uploaded-file']
        # Extracting uploaded data file name
        img_filename = secure_filename(uploaded_img.filename)
        # Upload file to database (defined uploaded folder in static path)
        uploaded_img.save(os.path.join(app.config['UPLOAD_FOLDER'], img_filename))
        # Storing uploaded file path in flask session
        session['uploaded_img_file_path'] = os.path.join(app.config['UPLOAD_FOLDER'], img_filename)
 
        return render_template('index2.html')

@app.route('/show_image')
def displayImage():
    # Retrieving uploaded file path from session
    img_file_path = session.get('uploaded_img_file_path', None)
    # Display image in Flask application web page
    return render_template('uploaded.html', user_image = img_file_path)


if __name__ == '__main__':
    app.run(debug=True)
