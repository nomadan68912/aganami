# 必要なライブラリをインポート
from django.http import HttpResponse
from django.shortcuts import render

# 画像を表示するためのビューを定義
def show_image(request):
    # 画像ファイルを読み込み
    with open('image.jpg', 'rb') as f:
        image_data = f.read()
    # HTTPレスポンスを返す
    return HttpResponse(image_data, content_type='image/jpeg')

# ルーティングを設定
from django.urls import path
urlpatterns = [
    path('image/', show_image, name='show_image'),
]

# Djangoアプリケーションを起動
if __name__ == '__main__':
    from django.core.management import execute_from_command_line
    execute_from_command_line()