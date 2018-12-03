from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from send_email.tasks import send_active_mail


def index(request):
    send_active_mail.delay(subject='xxx激活', to=['863517691@qq.com'])
    return HttpResponse('邮箱发送成功')
