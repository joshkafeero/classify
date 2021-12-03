from flask import render_template, url_for, flash, redirect, request, Blueprint, jsonify
from flask import current_app as app
from flask_awscognito import AWSCognitoAuthentication
from flask_login import login_user, current_user, logout_user, login_required
from project import db, bcrypt
# from project.models import User, Bplan
# from project.users.forms import (RegistrationForm, LoginForm, UpdateAccountForm,
#                                    RequestResetForm, ResetPasswordForm)
# from project.users.utils import  send_reset_email ,save_picture
# from werkzeug.urls import url_parse

users = Blueprint('users', __name__)

app.config['AWS_DEFAULT_REGION'] = 'us-east-2'
app.config['AWS_COGNITO_DOMAIN'] = 'classify.auth.us-east-2.amazoncognito.com'
app.config['AWS_COGNITO_USER_POOL_ID'] = 'us-east-2_ZLrgsYIvq'
app.config['AWS_COGNITO_USER_POOL_CLIENT_ID'] = '4cqc6b3a0bdk4dvov6isp42vp0'
app.config['AWS_COGNITO_USER_POOL_CLIENT_SECRET'] = '16r709acbm4k7tg4k8kv5gq70buk5j91bhrnvio84avchn6c8tg6'
app.config['AWS_COGNITO_REDIRECT_URL'] = 'http://localhost:5000/aws_cognito_redirect'
aws_auth = AWSCognitoAuthentication(app)

@users.route('/sign_in')
def sign_in():
    return redirect(aws_auth.get_sign_in_url())

@users.route('/aws_cognito_redirect')
def aws_cognito_redirect():
    access_token = aws_auth.get_access_token(request.args)
    return jsonify({'access_token': access_token})

@users.route('/')
@aws_auth.authentication_required
def index():
    claims = aws_auth.claims # or g.cognito_claims
    return jsonify({'claims': claims})

