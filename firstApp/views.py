from django.shortcuts import render
from .tasks import send_mail, send_welcome_mail, send_subscription_mail

from datetime import datetime
from datetime import timedelta

from celery import chain

# Create your views here.
def index(request):
    mail_sent = False

    if request.method == 'POST':
        email = request.POST.get('email')

        tasks = chain(
            send_mail.s(email),
            send_welcome_mail.s(),
            send_subscription_mail.s(),
        )
        tasks.apply_async(
            countdown=5,
        )

        mail_sent = True

    return render(request, 'index.html',{
        'mail_sent': mail_sent
    })