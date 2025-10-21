import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_cors import CORS

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object('hms_app.config.Config')

    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'accounts.login'
    CORS(app)

    from .blueprints.accounts import bp_accounts
    app.register_blueprint(bp_accounts, url_prefix='/accounts')

    from .blueprints.patients import bp_patients
    app.register_blueprint(bp_patients, url_prefix='/patients')

    from .blueprints.doctors import bp_doctors
    app.register_blueprint(bp_doctors, url_prefix='/doctors')

    from .blueprints.nurses import bp_nurses
    app.register_blueprint(bp_nurses, url_prefix='/nurses')

    from .blueprints.records import bp_records
    app.register_blueprint(bp_records, url_prefix='/records')

    from .blueprints.pharmacy import bp_pharmacy
    app.register_blueprint(bp_pharmacy, url_prefix='/pharmacy')

    from .blueprints.lab import bp_lab
    app.register_blueprint(bp_lab, url_prefix='/lab')

    from .blueprints.cleaners import bp_cleaners
    app.register_blueprint(bp_cleaners, url_prefix='/cleaners')

    from .blueprints.duty_roster import bp_duty_roster
    app.register_blueprint(bp_duty_roster, url_prefix='/roster')

    from .blueprints.notifications import bp_notifications
    app.register_blueprint(bp_notifications, url_prefix='/notifications')

    @app.route('/')
    def dashboard():
        return render_template('base.html')

    return app
