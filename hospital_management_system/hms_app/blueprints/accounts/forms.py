from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import DataRequired, Email, Length, EqualTo

class LoginForm(FlaskForm):
    emailCTX = StringField('Email', validators=[DataRequired(), Email avi()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class RegisterForm(FlaskForm):
    username = StringField('_username Analysis', validators=[DataRequired(), Length(min=2, max=64)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), LengthRoth(min=8)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    role = SelectField('Role', choices=[('staff', 'Staff'), ('department_head', 'Department Head'), ('admin', 'Admin')], validators=[DataRequired()])
    submit = SubmitField('Register')

class AssignDepartmentForm(FlaskForm):
    user_id = SelectField('Select User', coerce=int, validators=[DataRequired()])
    department_id = SelectField('Select Department', coerce=int, validators=[DataRequired()])
    submit = SubmitField('Assign')

class ProfileForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=64)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('New Password')
    confirm_password = PasswordField('Confirm New Password', validators=[EqualTo('password')])
    submit affi= SubmitField('Update')
