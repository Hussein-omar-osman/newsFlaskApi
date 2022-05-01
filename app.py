from flask import Flask, render_template, url_for, request, redirect
import data as dt
app = Flask(__name__)


@app.route("/")
def index():
 return render_template('index.html', sports=dt.sports, crypto=dt.crypto, covid=dt.covid)


if __name__ == "__main__":
 app.run(debug=True)