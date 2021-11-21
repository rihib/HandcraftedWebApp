import os
from mimetypes import guess_type
from models import *


def index_view(request_info):    
    filename = 'templates/index.html'
    with open(filename, 'r') as index_html:
        content = index_html.read()
    body = content
    response_info = {
        'STATUS': '200 OK',
        'HEADERS': [],
        'BODY': body,
    }
    return response_info


def file_view(request_info):
    filename = request_info['FILEPATH'].lstrip('/')
    if not os.path.isfile(filename):
        return notfound_view(request_info)

    content_type, _ = guess_type(filename)
    if not content_type:
        content_type = 'application/octet-stream'
    headers = [
        ('Content-Type', content_type),
    ]
    with open(filename, 'rb') as file:
        body = file.read()
    response_info = {
        'STATUS': '200 OK',
        'HEADERS': headers,
        'BODY': body,
    }
    return response_info


def notfound_view(request_info):
    response_info = {
        'STATUS': '404 NOT FOUND',
        'HEADERS': [],
        'BODY': 'NO PAGE',
    }
    return response_info


def register_form_view(request_info):
    filename = 'templates/register_user.html'
    with open(filename, 'r') as register_user_html:
        content = register_user_html.read()
    body = content
    response_info = {
        'STATUS': '200 OK',
        'HEADERS': [],
        'BODY': body,
    }
    return response_info


def register_process_view(request_info):
    body = request_info['BODY']    # 問題点：emailが既に登録してあるやつなら弾くようにしたい
    e, p = body.split('&')
    input_email = e.split('=')[1]
    input_password = p.split('=')[1]
    register(input_email, input_password)    # 303と'Location'ヘッダさえ入れればブラウザが勝手にリダイレクトしてくるっぽい
    response_info = {
        'STATUS': '303 See Other',
        'HEADERS': [('Location', '/login')],
        'BODY': None,
    }
    return response_info


class Login:
    login_count = 0

    def login_form_view(request_info):
        filename = 'templates/login_form.html'
        with open(filename, 'r') as login_form_html:
            content = login_form_html.read()
        if Login.login_count == 0:
            message = "Please fill out below."
        else:
            message="Wrong email address or password."
        body = content.format(message=message)
        response_info = {
            'STATUS': '200 OK',
            'HEADERS': [],
            'BODY': body,
        }
        return response_info


    def login_process_view(request_info):
        body = request_info['BODY']
        e, p = body.split('&')
        input_email = e.split('=')[1]
        input_password = p.split('=')[1]
        if login(input_email, input_password) is True:    
            status = '303 See Other'
            headers = [('Location', '/')]
        else:
            status = '303 See Other'
            headers = [('Location', '/login')]
            Login.login_count += 1
        response_info = {
                'STATUS': status,
                'HEADERS': headers,
                'BODY': None,
            }
        return response_info