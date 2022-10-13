from flask import Blueprint, render_template, flash, request, redirect

from .handle_files import upload_file

views = Blueprint('views', __name__)


@views.route('/')
def index():
    return render_template('index.html')

@views.route('/upload/', methods=['POST', 'GET'])
def upload():
    if request.method == 'POST':

        files = request.files.getlist("file[]")

        for file in files:
            upload_file(file)

        flash('Uploaded file(s) successfully', category='success')
        return redirect(request.url)

    else:
        return render_template('upload.html')
