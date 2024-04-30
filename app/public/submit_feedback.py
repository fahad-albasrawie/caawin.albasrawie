from flask import render_template, session, redirect, url_for, request, make_response, jsonify
from app import app

@app.route('/caawinaad/halcelin')
def open_submit_feedback_page():
    return render_template('caawin_templates/public/submit_feedback.html')
