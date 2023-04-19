from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    html = '''
<!DOCTYPE html>
<html lang="ja">
    <head>
        <title>美味しいデザート</title>
        <meta charset="utf-8"/>
    </head>
    <body>
        <h1>デザート一覧</h1>
        <ul>
            <li>アイス</li>
            <li>ケーキ</li>
            <li>パフェ</li>
    </body>
</html>'''
    return html

if __name__ == '__main__':
    app.debug = True
    app.run(host='localhost')