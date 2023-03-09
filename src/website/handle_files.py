from flask import current_app, flash, redirect, request
from flask_login import current_user
from werkzeug.utils import secure_filename

from .models import File
from . import db
import os


def upload_file(f):

    '''
    Check if file is selected, 
    Upload it and it in database.
    '''

    if f.filename == '':
        flash('No selected file', category='error')
        return redirect(request.url)

    _, file_extension = os.path.splitext(f.filename)
    filename = secure_filename(f.filename)
    path = os.path.join(os.getcwd() + current_app.config['UPLOAD_FOLDER'] + current_user.username + "/")
    if not os.path.exists(path):
        os.makedirs(path)
    f.save(os.path.join(path + filename))
    file = File(file_name=filename, uploader=current_user.id, type=file_extension)
    db.session.add(file)
    db.session.commit()