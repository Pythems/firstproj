from flask import render_template, url_for, flash, redirect,request
from academia_web import app,db,bcrypt
from academia_web.forms import RegistrationForm, LoginForm,UpdateAccountForm
from academia_web.models import User,Post
from flask_login import login_user,current_user,logout_user,login_required

posts= [ 
    {
        'title':'Time management',
        'date_posted': 'April 15th 2018',
        'content':'As a student, understanding the art and crafts of time management is an essential tools that is inevitably needed to...',
        'author':'OLUWAKANMI Samuel oluwatemilorun'
    },
    {
        'title':'Relationship',
        'date_posted': 'April 15th 2018',
        'content':"Live isn't meant to be lived, in isolation ...",
        'author':'OLUWAKANMI Samuel oluwatemilorun'
    },
    {
        'title':'Vision',
        'date_posted': 'April 15th 2018',
        'content':'Vision, the ability to see beyond the present and project, into the future...',
        'author':'OLUWAKANMI Samuel oluwatemilorun'
    }
    
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')




@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password= bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data,email=form.email.data,password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {form.username.data}!,you may login now', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='RegistrationFormister', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username = form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user,remember=form.remember.data)
            next_page = request.args.get('next')
            flash(f'Welcome {form.username.data} , You have been logged in !','success')
            return redirect (next_page) if next_page else redirect(url_for('account'))
            
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route("/account")
@login_required
def account():
    form=UpdateAccountForm()
    image_file =url_for('static', filename = 'Profile_Pics/' + current_user.image_file)
    return render_template('account.html', title='Account', image_file = image_file, form=form)