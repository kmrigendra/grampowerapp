
import os
from functools import wraps
from flask import render_template, url_for, redirect, send_from_directory, request, make_response, Response
from grampower import app
from grampower.service import StoreService
from grampower.validator import Store
import httplib
from grampower.utils import RestResponse
import logging
from grampower.data_builder import DataBuilderService

store_service = StoreService()


def check_auth(username, password):
    return username == 'admin' and password == 'Welcome@GP'

def authenticate():
    """Sends a 401 response that enables basic auth"""
    return Response(
    'Could not verify your access level for that URL.\n'
    'You have to login with proper credentials', 401,
    {'WWW-Authenticate': 'Basic realm="Login Required"'})

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated

@app.route('/get-store')
def get_store():
    store_id = request.args.get('id')
    return store_service.find_store_by_id(store_id)

# routing for basic pages (pass routing onto the Angular app)
@app.route('/')
@app.route('/register')
@app.route('/store')
@requires_auth
def basic_pages(**kwargs):
    return make_response(open('grampower/templates/index.html').read())


@app.route('/stores-all')
def get_stores_pagination():
    page = int(request.args.get('page'))
    return RestResponse(store_service.find_stores_pagination(page)).to_json()


@app.route('/save-store',methods=['POST'])
def save_store():
    payload = request.data
    try:
        store = Store.VALIDATOR.validate(payload)
    except Exception as e:
        logging.error(e)
        return RestResponse(data = None, status = httplib.INTERNAL_SERVER_ERROR, messages="internal server error", success = False).to_json()
    return store_service.register(store)


@app.route('/build-data')
def data_builder():
    DataBuilderService().data_builder()
    return RestResponse(data = None, messages="Build data successfully...").to_json()


# special file handlers and error handlers
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),'img/favicon.ico')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
