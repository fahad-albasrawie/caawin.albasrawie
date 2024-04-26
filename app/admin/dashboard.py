from flask import render_template, session, redirect, url_for, request, make_response, jsonify
from app import app


@app.route('/maamulka/looxa')
def dashboard():
    return render_template('admin/dashboard.html')
