import os
from flask import Blueprint, abort, current_app, render_template, flash, request, redirect, send_file, url_for
from flask_login import login_required, current_user

from .handle_files import upload_file
from .models import File

views = Blueprint('views', __name__)


@views.route('/')
def index():
    return render_template('index.html')


@views.route('/upload/', methods=['POST', 'GET'])
@login_required
def upload():
    if request.method == 'POST':

        files = request.files.getlist("file[]") # Get all files from request

        for file in files:
            upload_file(file)
        
    
        flash('Uploaded file(s) successfully', category='success')
        return redirect(url_for('views.myfiles'))

    else:
        return render_template('upload.html')



@views.route('/my-files/')
@login_required
def myfiles():
    files = File.query.filter_by(uploader=current_user.id).all()
    return render_template('myfiles.html', files=files)


@views.route('/preview/<file_id>')
@login_required
def preview(file_id):
    file = File.query.filter_by(id=file_id).first()
    if current_user.id == file.user.id:
        path = os.path.join(os.getcwd() + current_app.config['UPLOAD_FOLDER'] + current_user.username + "/" + file.file_name)
        return send_file(path)
    else:
        abort(403)