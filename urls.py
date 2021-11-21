from views import *

# URLの書く順番だいじ．全て合致したら後のURLを見ずにviewを返してしまうので'/register_process'よりも'/register'を先に書くと'/register_process'のURLが来ても'/register'が先に合致してしまう
URL_PATTERNS = {
    '/static/': file_view,
    '/register_process': register_process_view,
    '/register': register_form_view,
    '/login_process': Login.login_process_view,
    '/login': Login.login_form_view,
    '/': index_view,
}