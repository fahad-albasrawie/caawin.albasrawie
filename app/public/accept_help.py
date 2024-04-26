from flask import render_template, session, redirect, url_for, request, make_response, jsonify
from app import app

@app.route('/oggolow')
def open_accept_help_page():
    return render_template('public/accept_help.html')
