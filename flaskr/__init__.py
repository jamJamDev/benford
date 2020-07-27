import os

from flask import Flask, render_template, request, flash, redirect, url_for
from werkzeug.utils import secure_filename

from .helpers import benford, files

ALLOWED_EXTENSIONS = {'txt'}
UPLOAD_FOLDER = './flaskr/uploads'

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Home Page
    @app.route('/')
    def index():
        return render_template('main/index.html')

    @app.route('/result', methods=['GET', 'POST'])
    def result():
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
            if file and files.allowed_file(file.filename, ALLOWED_EXTENSIONS):
                filename = secure_filename(file.filename)
                #filename = file.filename
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

                # Parse File Contents for Variables
                benford_census_data = benford.get_benford_data_from_file(UPLOAD_FOLDER, file)
                num_data_points = benford_census_data[0]
                benford_count = benford_census_data[1]

                # Keeping on hand for potential future features
                # census_data = benford_census_data[2]
                # column_names = benford_census_data[3]

                # Calculate percent of leading number frequency
                benford_percents = benford.calc_percents(num_data_points, benford_count)
                # return redirect(url_for('uploaded_file', filename=filename))

                # Validate Benford's Assertion
                is_valid = benford.validate_benfords_law(benford_percents)
                return render_template('main/results.html', is_valid = is_valid, data=benford_percents, chart_title="Benford's Law", y_label='Frequency %', x_label='Leading Digit')
            else:
                return render_template('main/index.html', error_message='Incorrect file type, only accepting .txt files at the moment.')
    @app.route('/uploaded_file')
    def uploaded_file():
        return 'uploaded'

    @app.errorhandler(404)
    def not_found(e):
        return render_template("404.html")

    return app