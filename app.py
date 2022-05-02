from flask import Flask, render_template, url_for, request, redirect
import requests
import data as dt
app = Flask(__name__)


@app.route("/")
def index():
 return render_template('index.html', 
                        sports=dt.sports, crypto=dt.crypto, 
                        covid=dt.covid, business=dt.business)

@app.route("/searchResult", methods=['POST'])
def searchResult():
 name = request.form['search']
 return render_template('/searchResult.html', name=name)
 
if __name__ == "__main__":
 app.run(debug=True)