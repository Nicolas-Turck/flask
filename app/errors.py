from flask import render_template
from app import app, db

@app.errorhandler(404)
def not_found_error(error):
    """method for return page 404.html if error in pages"""
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    """method for return page 500.html if error in pages"""
    db.session.rollback()
    return render_template('500.html'), 500