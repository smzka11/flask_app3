#coding: utf-8

# 必要なモジュールのインポート
from flask import Flask, render_template

# Flaskをインスタンス化
app = Flask(__name__)

# ルートディレクトリにアクセスがあった時の処理
@app.route('/')
def index():
    return render_template('index.html')
    
# エントリーポイント
if __name__ == '__main__':
    app.run()