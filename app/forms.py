from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired
from flask_wtf.file import FileField, FileAllowed, FileRequired


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])


class UploadForm(FlaskForm):
    # Create a file upload form using Flask-WTF. The form should have a file field and a submit button
    file = FileField("Image", validators=[
        FileRequired(),
    FileAllowed(['jpg', 'png'], 'Images only!')
    ])
    submit = SubmitField("Upload")      
