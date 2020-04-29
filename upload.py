import os
from flask import Flask, flash, request, redirect, url_for , render_template , session
from flask import send_from_directory
from werkzeug.utils import secure_filename
from flask import current_app as app
import editor


UPLOAD_FOLDER = "/user_upload"
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg' , 'html'}


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            print(filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            session['filename'] = filename
            return redirect(url_for('uploaded_file'))
    return render_template('upload_file.html')


def uploaded_file():
    return redirect(url_for('main'))