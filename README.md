# Handcrafted WebApp

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

## 追記
[【PyCon JP 2018】仕組みから理解するWebアプリケーション Webフレームワークを使わずに原理を学ぶ](https://logmi.jp/tech/articles/314757)をもとに実装した。 \
ただ、[Http通信とSocket通信の違い](https://bny64.github.io/2020/12/13/http-socket-jp/)や[pythonでローカルwebサーバを立ち上げる](https://qiita.com/okhrn/items/4d3c74563154f191ba16)からわかるようにソケット通信だけを使って実装しているだけなのでHTTP通信を使って実装したいところ。 \
また、アカウント周りはセッションの維持などを行えてないので、そこら辺は課題である。 \
[KUMO MTGでの発表スライド](https://docs.google.com/presentation/d/1l8_ZKDM_Wpyon1X0w8RpljXsv-AjGOCh/edit?usp=sharing&ouid=112105813656729520733&rtpof=true&sd=true)
