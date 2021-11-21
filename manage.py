import socket
from urls import *
from views import *


def make_request_info(byte_request):
    str_request = byte_request.decode('utf-8')
    if str_request[-4:] == '\r\n\r\n':
        startline_and_headers = str_request.rstrip('\r\n\r\n')
        body = None
    else:
        startline_and_headers, body = str_request.split('\r\n\r\n', 1)   
    splited_startline_and_headers = startline_and_headers.splitlines()
    startline = splited_startline_and_headers[0]
    splited_headers = splited_startline_and_headers[1:]
    method, filepath, server_protocol = startline.split(' ', 2)
    request_info = {
        'REQUEST_METHOD': method,
        'FILEPATH': filepath,
        'SERVER_PROTOCOL': server_protocol,
        'HEADERS': splited_headers,
        'BODY': body,
    }
    return request_info


def select_view_from_filepath(request_info):
    filepath = request_info['FILEPATH']
    for path, view in URL_PATTERNS.items():
        if filepath.startswith(path):
            return view
    return notfound_view


def make_byte_response(response_info):
    startline = ('HTTP/1.1 ' + response_info['STATUS']).encode('utf-8')
    headers_list = []
    for k, v in response_info['HEADERS']:
        header = '%s: %s' % (k, v)
        headers_list.append(header)
    headers = ('\r\n'.join(headers_list)).encode('utf-8')
    body = response_info['BODY']
    if isinstance(body, str):
        body = body.encode('utf-8')
    if not body:
        body = b''
    byte_response = startline + b'\r\n' + headers + b'\r\n\r\n' + body
    return byte_response


def main():
    with socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM) as server_socket:
        server_socket.bind(('127.0.0.1', 8000))
        server_socket.listen()
        while True:
            conn, _ = server_socket.accept()
            with conn:
                byte_request = b''
                while True:
                    chunk = conn.recv(4096)    # 問題点：最後のチャンクがちょうど4096byteだった時，この行でフリーズしてしまう
                    byte_request += chunk
                    if len(chunk) < 4096:
                        break   
                request_info = make_request_info(byte_request)
                view = select_view_from_filepath(request_info)
                response_info = view(request_info)
                byte_response = make_byte_response(response_info)
                conn.sendall(byte_response)


if __name__ == '__main__':
    main()