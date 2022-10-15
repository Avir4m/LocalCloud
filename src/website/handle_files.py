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

    print(os.getcwd() + current_app.config['UPLOAD_FOLDER'])

    if f.filename == '':
        flash('No selected file', category='error')
        return redirect(request.url)

    
    filename = secure_filename(f.filename)
    f.save(os.path.join(os.getcwd() + current_app.config['UPLOAD_FOLDER'] + filename))

    file = File(file_name=filename, uploader=current_user.id)
    db.session.add(file)
    db.session.commit()