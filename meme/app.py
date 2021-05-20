from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.secret_key = "f2c324e0-7f44-4e39-a6ab-d44b0f54aee0"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///meme.db'

db = SQLAlchemy(app=app)
if __name__ == "__main__":


    # Middle Wear can go here
    # Before the veiws
    from veiws import *
    
    app.run(debug=True)