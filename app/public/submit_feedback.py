from flask import render_template, session, redirect, url_for, request, make_response, jsonify
from app import app

@app.route('/halcelin')
def open_submit_feedback_page():
    return render_template('public/submit_feedback.html')
