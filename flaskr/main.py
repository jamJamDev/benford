import os

from flask import Blueprint, flash, g, redirect, render_template, request, url_for
from flask import current_app as app
from werkzeug.utils import secure_filename

bp = Blueprint('main', __name__)
UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = {'txt'}
g.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@bp.route('/')
def index():
    return render_template('main/index.html')

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@bp.route('/', methods=['GET', 'POST'])
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
            file.save(os.path.join(g.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file',
                                    filename=filename))

    return render_template('main/index.html')