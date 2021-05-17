# Room for all imports
from logging import debug
from flask import Flask, render_template, redirect, flash, request, send_file, url_for
import os
from werkzeug.utils import secure_filename

# Uploading Stuff
UPLOAD_FOLDER = ""
IMAGE_EXSTENSIONS = {'png', 'jpg', 'gif', 'jpeg'}



app = Flask(__name__)

app.secret_key = "57f7d2802da848fb940239329277ccb0"

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")


def allowed_file(fileName):
    return '.' in fileName and \
        fileName.rsplit('.', 1)[1].lower() in IMAGE_EXSTENSIONS
    


@app.route('/post/<username>/<postname>/')
def returnMeme(username, postname):
    nameOfPost, ExtOfPost    = os.path.splitext(postname)
    try:
        return send_file("/memes/{}/{}/{}".format(username, nameOfPost, postname), "image/{}".format(ExtOfPost))
    except FileNotFoundError:
        return 'No File Found'
@app.route("/upload")
def upload():
    return render_template("upload.html")
@app.route("/uploader/", methods = ['POST'])
def uploader():
    # Gets the username
    username = request.form["username"]
    print(username)
    # Get name of the video
    file = request.files["file"]
    
    postname = request.form['postname']
    if username and postname: # Checks for username and video
        if file.filename != '' and username != '' and postname != '': # checks that teh file names are completly blank
            # videoName, videoExt = os.path.splitext(uploadedVideo.filename) # File extensions
            fileName, fileExt = os.path.splitext(file.filename)
            # os.system('mkdir ~CODE/src/video/' + username + "/" + video + "")
            os.mkdir("/home/piderking/CODE/meme/memes/{}/{}/".format(username, postname))
            file.save("/home/piderking/CODE/meme/memes/{}/{}/{}{}".format(username, postname, postname, fileExt))
            # videoImage.save("/home/piderking/CODE/src/video/{}/{}/{}{}".format(username, video, video, fileExt))

            # data(video, username, {'Vidext': videoExt, 'ImageExt': fileExt}, {'title':time, 'desc':description})
            # uploaded_file.save("/video/" + username + "/" + video + "/" + uploaded_file.filename)
        return redirect("/")


@app.errorhandler(404)
def fof(e):
    return render_template("404.html"), 404

@app.errorhandler(500)
def serverError(e):
    return render_template("500.html")

if __name__ == "__main__":
    app.run(debug=True)

