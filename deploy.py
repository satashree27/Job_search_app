from flask import Flask, render_template, url_for, request, session, redirect
from werkzeug.security import generate_password_hash, check_password_hash
import pymongo

app = Flask(__name__)
app.secret_key = 'mysecret'

mongo = pymongo.MongoClient("localhost", 27017)

users = mongo.db.users
emp = mongo.db.emp

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        users = mongo.db.users
        existing_user = users.find_one({'name': request.form['username']})
        if existing_user is None:
            hashpass = generate_password_hash(request.form['password'], method='sha256')
            users.insert({'name': request.form['username'], 'password': hashpass})
            session['username'] = request.form['username']
            return redirect(url_for('index'))
        return redirect(url_for('register'))
    return render_template('register.html')


@app.route('/register_emp', methods=['POST', 'GET'])
def register_emp():
    if request.method == 'POST':
        users = mongo.db.emp
        existing_user = users.find_one({'name': request.form['username']})
        if existing_user is None:
            hashpass = generate_password_hash(request.form['password'], method='sha256')
            users.insert({'name': request.form['username'], 'password': hashpass})
            session['username'] = request.form['username']
            return redirect(url_for('index'))
        return redirect(url_for('register_emp'))
    return render_template('register_emp.html')

@app.route('/login')
def login():
    if 'username' in session:
        #return 'You are logged in as  :' + session['username']
        return render_template('dashboard.html')
    test = True
    return render_template('login.html', test = test)


@app.route('/login_check', methods=['POST'])
def login_check():
    users = mongo.db.users
    login_user = users.find_one({'name': request.form['username']})

    if login_user:
        if check_password_hash(login_user['password'], request.form['password']):
            session['username'] = request.form['username']
            return redirect(url_for('login'))
    test = False
    return render_template('login.html', test=test)

@app.route('/login_emp')
def login_emp():
    if 'username' in session:
        #return 'You are logged in as  :' + session['username']
        return render_template('dashboard_emp.html')
    test = True
    return render_template('login_emp.html', test = test)


@app.route('/login_check_emp', methods=['POST'])
def login_check_emp():
    emp = mongo.db.emp
    login_user = emp.find_one({'name': request.form['username']})

    if login_user:
        if check_password_hash(login_user['password'], request.form['password']):
            session['username'] = request.form['username']
            return redirect(url_for('login_emp'))
    test = False
    return render_template('login_emp.html', test=test)

@app.route('/plumber')
def plumber():
    return render_template('plumber.html')

@app.route('/mechanic')
def mechanic():
    return render_template('mechanic.html')

@app.route('/carpenter')
def carpenter():
    return render_template('carpenter.html')

@app.route('/applied')
def applied():
    return render_template('applied.html')

@app.route('/post_new')
def post_new():
    return render_template('new_job.html')

@app.route('/job_posted')
def job_posted():
    return render_template('job_posted.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.secret_key = 'mysecret'
    app.run(debug = True)

