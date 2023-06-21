from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    html = '''
<!DOCTYPE html>
<html lang="ja">
    <head>
        <title>第1回 Instana Observability Meetup</title>
        <meta charset="utf-8"/>
        <script>
           (function(s,t,a,n){s[t]||(s[t]=a,n=s[a]=function(){n.q.push(arguments)},
           n.q=[],n.v=2,n.l=1*new Date)})(window,"InstanaEumObject","ineum");

           ineum('reportingUrl', 'https://instana.automate-your.work:446/eum/');
           ineum('key', 'MqMhdpz0TluBtZwlllJeXg');
           ineum('trackSessions');
        </script>
        <script defer crossorigin="anonymous" src="https://instana.automate-your.work:446/eum/eum.min.js"></script>
    </head>
    <body>
        <h2>◆◆◆◆し買う第1回 Instana Observability Meetup◆◆◆◆◆</h2>
        <ul>
            <p>１．コンテナ概要の説明</p>
            <p>２．OpenShift環境にPythonコンテナを作成</p>
            <p>３．OpenShift環境にクラウド監視製品（Instanaエージェントのコンテナ）導入</p>
            <p>４．Instanaのインフラストラクチャー画面で監視対象にしたOpenShiftと作成したPythonコンテナが監視対象となっていることの確認</p>
            
            <p><a href="https://www.nicsoft.co.jp/">リンク</a></p>
    </body>
</html>'''
    return html

if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0", port=8080)
