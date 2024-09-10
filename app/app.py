from flask import Flask, render_template, request, flash, redirect, url_for
from app.services import Auth

app = Flask(__name__)
app.config['SECRET_KEY'] = "YouDontGetTheKey"
app.config['SQLALCHEMY_DATABASE_URL'] = 'sqlite:////app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


@app.route('/')
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        pswd = request.form.get('password')

        msg, status = Auth.login(email, pswd)

        if status == 200:
            flash(message=msg)
            return redirect(url_for('index'))
        
    return render_template('login.html')


def index():
    return render_template('index.html')


@app.route('/register')
def customer_register():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        pnumber = request.form.get('pnumber')
        password = request.form.get('password')

        message, status = Auth.user_register(
            name=name, email=email, password=password,
            pnumber=pnumber
            )
        
        if status == 200:
            flash(message=f'{message} successfully registered.')
            return render_template('login.html')
        
        elif status == 400:
            flash(message=e)
        
        
    return render_template('registration.html')
    



app.run()

