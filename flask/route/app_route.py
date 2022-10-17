from flask import Blueprint, render_template, request
from werkzeug.utils import secure_filename

app_route = Blueprint('first_route', __name__)

@app_route.route("/upload")
def render_file():
    return render_template('upload.html')

@app_route.route('/fileUpload', methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save(secure_filename(f.filename))
        return 'uploads 디렉토리 -> 파일 업로드 성공!'
