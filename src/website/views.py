from flask import Blueprint, render_template, flash, request, redirect
from flask_login import login_required

from .handle_files import upload_file

views = Blueprint('views', __name__)


@views.route('/')
def index():
    return render_template('index.html')

@login_required
@views.route('/upload/', methods=['POST', 'GET'])
def upload():
    if request.method == 'POST':

        files = request.files.getlist("file[]") # Get all files from request

        for file in files:
            upload_file(file)
        
    
        flash('Uploaded file(s) successfully', category='success')
        return redirect(request.url)

    else:
        return render_template('upload.html')
