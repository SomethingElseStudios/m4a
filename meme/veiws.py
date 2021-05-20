from flask import Flask, render_template, redirect, flash, request, send_file, url_for
from logging import debug
from werkzeug.utils import secure_filename
from app import app 
import os
from models import User, addUser #, check_user
from models import Posts, addPost
IMAGE_EXSTENSIONS = {'.png', '.jpg', '.gif', '.jpeg'}


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")
    

@app.route("/signup")
def auth():
    if request.method == 'POST':
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")
        if len(email) < 4:
            flash("Password Must Be Longer than 3 Characters")
        elif len(username) < 4:
            flash('username must be longer than 3 chracters')
        else:
            # new_User = models.User(email=email, password=password, username=username) 
            return redirect("/login")
    return render_template("signup.html")

@app.route("/login")
def login():
    if request.method == "POST":
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")
        return "Null" 
    return render_template("login.html")

@app.route('/post/<username>/<postname>/')
def returnMeme(username, postname):
    nameOfPost, ExtOfPost    = os.path.splitext(postname)

    try:
        return send_file("/memes/{}/{}/{}".format(username, nameOfPost, postname), "image/{}".format(ExtOfPost))
    except FileNotFoundError:
        return 'No File Found'

# Login Here


# Uploader 
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
            print(fileExt)
            # os.system('mkdir ~CODE/src/video/' + username + "/" + video + "")
            if fileExt in IMAGE_EXSTENSIONS:
                print("In Images \n\n\n")
                if  not os.path.isdir(f"/home/piderking/CODE/meme/memes/{username}/"):
                    print("deprecated don't do this step when user creation has been made")
                    # print(" in"+ f"/home/piderking/CODE/meme/memes/{username}/")
                    os.mkdir(f"/home/piderking/CODE/meme/memes/{username}/") # remove this on sign up
                    # This is for when a user needs to sign in, your dir only works when you create an account
                if  os.path.isdir(f"/home/piderking/CODE/meme/memes/{username}/"):
                    print(username)
                    # check for dir
                    if  not os.path.isdir(f"/home/piderking/CODE/meme/memes/{username}/{postname}"):
                        print(" in " + f"/home/piderking/CODE/meme/memes/{username}/")
                        print(postname)
                        os.mkdir("/home/piderking/CODE/meme/memes/{}/{}/".format(username, postname))
                        file.save("/home/piderking/CODE/meme/memes/{}/{}/{}{}".format(username, postname, postname, fileExt))
                else:
                    return "Error"
            # videoImage.save("/home/piderking/CODE/src/video/{}/{}/{}{}".format(username, video, video, fileExt))
            if fileExt not in IMAGE_EXSTENSIONS:
                flash("Not in File Extsension")
                return "Error"
            # data(video, username, {'Vidext': videoExt, 'ImageExt': fileExt}, {'title':time, 'desc':description})
            # uploaded_file.save("/video/" + username + "/" + video + "/" + uploaded_file.filename)
        return redirect("/")


@app.errorhandler(404)
def fof(e):
    return render_template("404.html"), 404

@app.errorhandler(500)
def serverError(e):
    return render_template("500.html")
