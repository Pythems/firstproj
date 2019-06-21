from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,TextAreaField
from academia_web import app,db,bcrypt,mail
from wtforms.validators import DataRequired,Length





class PostForm(FlaskForm):
	title = StringField ('Title',validators =[DataRequired()])
	content = TextAreaField('Content', validators = [DataRequired(),Length(min =2 ,max =200)])
	submit = SubmitField('Post')