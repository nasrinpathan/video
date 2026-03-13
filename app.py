from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


ALLOWED_EXTENSIONS = ['mp4']


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/upload', methods=['post'])
def upload():
    if 'video' not in request.files:
        return "No video file found"
    video = request.files['video']
    if video.filename == "":
        return 'No video file selected'
    if video and allowed_file(video.filename):
        video.save('static/videos/' + video.filename)
        return render_template('preview.html', video_name=video.filename)
    return "invalid file type"


if __name__ == "__main__":
    app.run(debug=True)
