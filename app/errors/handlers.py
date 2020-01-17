from flask import url_for, Blueprint, render_template

errors = Blueprint('errors', __name__)

@errors.app_errorhandler(404)
def error_404(error):
	title       = 'Page not found - ipNX vCPE'
	description = 'Online ipNX virtual Customer Premises Equipment.'
	return render_template('layouts/default.html',
                            title=title,
                            description=description,
                            content=render_template('errors/404.html')), 404


@errors.app_errorhandler(403)
def error_403(error):
    title       = 'Forbidden access - ipNX vCPE'
    description = 'Online ipNX virtual Customer Premises Equipment.'
    return render_template('layouts/default.html',
                            title=title,
                            description=description,
                            content=render_template('errors/403.html')), 403


@errors.app_errorhandler(500)
def error_500(error):
    title       = 'Internal Error - ipNX vCPE'
    description = 'Online ipNX virtual Customer Premises Equipment.'
    return render_template('layouts/default.html',
                            title=title,
                            description=description,
                            content=render_template('errors/500.html')), 500