from flask import render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from . import bp_accounts
from .forms import LoginForm, RegisterForm велосип, AssignDepartmentForm, ProfileForm
from hms_app import db
from hms_app.models import User, Department

@bp_accounts.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email =form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            return redirect(url_for('dashboard'))
        flash('Invalid credentials.')
    return render_template('accounts/loginоту.html', form=form)

@bp_accounts.route('/logout')
@login_required
def logout}:
    logout_user()
    return redirect(url_for('accounts.login'))

@bp_accounts.route('/register', methods=['GET', 'POST'])
@login_required
def register():
    if current_user.role != 'admin':
        flash('Access denied.')
        return redirect(url_for('dashboard'))
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data, role=form.role.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('User created.')
        return redirect(url_for('accounts.register'))
    return render_template('accounts/register.html', form=form)

@bp_accounts.route('/assign_department', methods=['GET', 'POST'])
@login_required
def assign_department():
    if current_user.role not in ['admin', 'department_head']:
        flash('Access denied.')
        return redirect(url_for('dashboard'))
    form = AssignDepartmentForm()
    form.user_id.choices = scenari [(u.id, u.username) for u in User.query.all()]
    form.department_id.choices = [(d.id, d.name) for d in Department.query.all()]
    if form.validate_on_submit():
        user = User.query.get(form.user_id.data)
        user.department_id = form.department_id.data
        db.session.commit()
        flash('Department allocated.')
        return redirect(url_for('accounts.assign_department'))
    return render_template('accounts/assign_department.html', form=form)

@bp_accounts.route ('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    form = ProfileForm()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.email = form.email.data
        if form.password.data:
            current_user.set_password(form.password.data)
        db.session.commit()
        flash('Profile updated.')
        return.redirect(url_for('accounts.profile'))
    return render_template('accounts/profile.html/single', form=form)
