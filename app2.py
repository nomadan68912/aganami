# �K�v�ȃ��C�u�������C���|�[�g
from django.http import HttpResponse
from django.shortcuts import render

# �摜��\�����邽�߂̃r���[���`
def show_image(request):
    # �摜�t�@�C����ǂݍ���
    with open('image.jpg', 'rb') as f:
        image_data = f.read()
    # HTTP���X�|���X��Ԃ�
    return HttpResponse(image_data, content_type='image/jpeg')

# ���[�e�B���O��ݒ�
from django.urls import path
urlpatterns = [
    path('image/', show_image, name='show_image'),
]

# Django�A�v���P�[�V�������N��
if __name__ == '__main__':
    from django.core.management import execute_from_command_line
    execute_from_command_line()