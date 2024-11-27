from flask import Flask, request, redirect, url_for, session, render_template
import Crops
import time


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        defval = 0
        username = request.form.get('username', defval)
        password = request.form.get('password', defval)
        potatoes = Crops.Crops(username, password)
        if username == '' and password == '':
            return redirect(url_for('failed'))

        else:
            potatoes.cropHarvesting()
            return redirect(url_for('success'))

    return render_template('index.html')


@app.route('/success')
def success():
    return render_template('success.html')

#
#   @app.route('/failed')
#   def failed():
#    return '''
#      <h1>Login failed!!!</h1>
#      <p><b>Returning to main page</b><span id="dots"></span></p>
#     <style src='style.css'>
#     <script>let dotC=0;const dots=3;const dotsEle = document.getElementById('dots');function apndDots(){dotC++;dotsEle.textContent +='.';if (dotC >= dots){dotC = 0;dotsEle.textContent='';}}setInterval(apndDots, 250);setTimeout(function(){window.location.href = '/';},3000);</script>
#        '''
