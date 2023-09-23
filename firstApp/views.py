from django.shortcuts import render
from .tasks import send_mail
from datetime import datetime
from datetime import timedelta

# Create your views here.
def index(request):
    mail_sent = False

    if request.method == 'POST':
        email = request.POST.get('email')
        send_mail.apply_async(
            args=[email],
            eta=datetime.now()+ timedelta(seconds=5)
        )

        mail_sent = True

    return render(request, 'index.html',{
        'mail_sent': mail_sent
    })