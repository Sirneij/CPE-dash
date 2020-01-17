from flask import url_for, render_template, request, Blueprint, Response, jsonify
from flask_login import current_user, login_required
from app.models import User
import os, shutil, re, cgi, json, random, time
from datetime import datetime
main = Blueprint('main', __name__)


# authenticate user
@main.route('/index.html')
@login_required
def index():
    
    content = None
    
    try:
        # try to match the pages defined in -> themes/light-bootstrap/pages/
        return render_template('layouts/default.html',
                                content=render_template( 'pages/index.html') )
    except:
        abort(404)
    
# Used only for static export
@main.route('/wifi.html')
@login_required
def wifi():

    # custommize your page title / description here
    title = 'wifi settings - ipNX vCPE'
    description = 'Online ipNX virtual Customer Premises Equipment.'

    # try to match the pages defined in -> pages/
    return render_template('layouts/default.html',
                            content=render_template( 'pages/wifi.html') )


# Used only for static export
@main.route('/DNS.html')
@login_required
def DNS():

    # custommize your page title / description here
    title = 'DNS servers - ipNX vCPE'
    description = 'Online ipNX virtual Customer Premises Equipment.'

    # try to match the pages defined in -> pages/
    return render_template('layouts/default.html',
                            content=render_template( 'pages/DNS.html') )

# Used only for static export
@main.route('/DHCP.html')
@login_required
def DHCP():

    # custommize your page title / description here
    title = 'DHCP - ipNX vCPE'
    description = 'Online ipNX virtual Customer Premises Equipment.'

    # try to match the pages defined in -> pages/
    return render_template('layouts/default.html',
                            content=render_template( 'pages/DHCP.html') )

# Used only for static export
@main.route('/device.html')
@login_required
def device():

    # custommize your page title / description here
    title = 'Device settings - ipNX vCPE'
    description = 'Online ipNX virtual Customer Premises Equipment.'

    # try to match the pages defined in -> pages/
    return render_template('layouts/default.html',
                            content=render_template( 'pages/device.html') )