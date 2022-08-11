from flask import Blueprint, render_template, abort, redirect


views = Blueprint('views', __name__)


@views.route('')
def index():
    return render_template('index.html')