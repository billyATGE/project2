from flask import Flask, request, send_from_directory, render_template, url_for
from flask_pymongo import PyMongo

#################################################
# Flask Routes
# Create an instance of Flask
app = Flask(__name__)

# Route to render index.html template 
@app.route('/index', methods=['GET', 'POST'])
def home(): 
    return render_template('index.html')

@app.route("/map", methods=['GET', 'POST'])
def map():  
    return render_template("map.html")

if __name__ == '__main__':
    app.run()