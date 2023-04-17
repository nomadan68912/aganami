from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # �摜�t�@�C���̃p�X��ݒ肷��
    image_path = './image.jpg'
    return render_template('index.html', image_path=image_path)

if __name__ == '__main__':
    app.run(debug=True)
