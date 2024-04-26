from flask import render_template, session, redirect, url_for, request, make_response, jsonify
from app import app

@app.route('/')
def index():
    return render_template('public/ask_help.html')
