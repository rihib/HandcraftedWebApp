# No Framework Blog

## 実行手順
1. ローカルにクローンする
1. 以下のコマンドを実行し、ブラウザで[ローカルホスト](http://localhost:8000/)を開く
    ```
    % cd no_framework_blog
    % python3 -m venv .venv
    (.venv) % source .venv/bin/activate
    (.venv) % python3 -m pip install -r requirements.txt
    (.venv) % python3 manage.py
    ```