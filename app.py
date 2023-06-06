from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    html = '''
<!DOCTYPE html>
<html lang="ja">
    <head>
        <title>第1回SE塾「コンテナの知識について（基本編）」</title>
        <meta charset="utf-8"/>
        <script>
            (function(s,t,a,n){s[t]||(s[t]=a,n=s[a]=function(){n.q.push(arguments)},
            n.q=[],n.v=2,n.l=1*new Date)})(window,"InstanaEumObject","ineum");

            ineum('reportingUrl', 'https://eum-orange-saas.instana.io');
            ineum('key', 'GMyajlc7Ss-2lLTxoFqslg');
            ineum('trackSessions');
            </script>
            <script defer crossorigin="anonymous" src="https://eum.instana.io/eum.min.js"></script>
    </head>
    <body>
        <h2>◆GitHubのサンプルコードをOpenShiftでコンテナ化してクラウド監視製品で監視対象にしてみる！</h2>
        <ul>
            <p>１．コンテナ概要の説明</p>
            <p>２．OpenShift環境にPythonコンテナを作成</p>
            <p>３．OpenShift環境にクラウド監視製品（Instanaエージェントのコンテナ）導入</p>
            <p>４．Instanaのインフラストラクチャー画面で監視対象にしたOpenShiftと作成したPythonコンテナが監視対象となっていることの確認</p>
            
            <p><a href="https://www.nicsoft.co.jp/">ソフトのホームぺ～ジ～</a></p>
    </body>
</html>'''
    return html

if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0", port=8080)
