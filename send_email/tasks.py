import time

from celery import shared_task
from django.core.mail import send_mail

from celery_send_mail import settings


@shared_task
def send_active_mail(subject='', content=None, to=None):
    print('开始发送邮件')
    send_mail(subject=subject,
              message='',
              html_message=content,
              from_email=settings.EMAIL_HOST_USER,
              recipient_list=to
              )
    print('发送完成')
    return '1'