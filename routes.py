import secrets
import os
from PIL import Image
from flask import abort, render_template, url_for, flash, redirect,request,Flask
from academia_web import app,db,bcrypt,mail
from academia_web.forms import RegistrationForm, LoginForm, UpdateAccountForm, PostForm, RequestResetForm, ResetPasswordForm 
from academia_web.models import User,Post
from flask_login import login_user,current_user,logout_user,login_required
from flask_mail import Message

app = Flask(__name__)

app.config['SECRET_KEY'] = 'e80df805b29ab44e417bf515b666e418'