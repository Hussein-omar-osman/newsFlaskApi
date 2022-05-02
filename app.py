from flask import Flask, render_template, url_for, request, redirect
import requests
import data as dt
app = Flask(__name__)


@app.route("/")
@app.route("/home")
def index():
 return render_template('index.html', 
                        sports=dt.sports, crypto=dt.crypto, 
                        covid=dt.covid, business=dt.business)

@app.route("/searchResult", methods=['POST'])
def searchResult():
 name = request.form['search'].title()
 api_key = '17e0788966b6404ab6e3a6997bfbacf2'
 res = requests.get(f'https://newsapi.org/v2/everything?q={name}&apiKey={api_key}').json()
 return render_template('/searchResult.html', name=name, datas=res)
 
if __name__ == "__main__":
 app.run(debug=True)