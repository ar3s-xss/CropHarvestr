from flask import Flask, request, redirect, url_for, session, render_template
import Crops
import time


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form['email']
        password = request.form['password']
        potatoes = Crops.Crops(username, password)
        potatoes.cropHarvesting()
        return redirect(url_for('success'))

    return render_template('index.html')


@app.route('/success')
def success():
    return render_template('success.html')

