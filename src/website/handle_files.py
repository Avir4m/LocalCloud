from flask import current_app, flash, redirect, request
from werkzeug.utils import secure_filename
import os


def upload_file(f):
    print(f.filename)
    if f.filename == '':
                flash('No selected file', category='error')
                return redirect(request.url)

    filename = secure_filename(f.filename)
    f.save(os.path.join(os.getcwd() + current_app.config['UPLOAD_FOLDER'] + filename))