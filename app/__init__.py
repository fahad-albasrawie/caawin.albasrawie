from flask import Flask
from datetime import timedelta

app = Flask(__name__)

from app.public import accept_help, accept_help_model, ask_help, ask_help_model, submit_feedback_model, submit_feedback
from app.admin import dashboard, dashboard_model, login

app.config["SECRET_KEY"] = "caawin.albasrawie"
# app.permanent_session_lifetime = timedelta(minutes=2)
app.permanent_session_lifetime = timedelta(days=365)


