import random
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'nlerjglsr'


@app.route('/')
def load():
    session['secret_number'] = random.randint(1, 100)
    session['guess'] = None
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():
    print(request.form['guess'])
    session['guess'] = int(request.form['guess'])
    return redirect('/playing')

@app.route('/playing')
def play():
    return render_template('index.html')

if __name__ =="__main__":
    app.run(debug=True)