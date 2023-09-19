from django.shortcuts import render
from .tasks import send_mail

# Create your views here.
def index(request):
    mail_sent = False

    if request.method == 'POST':
        email = request.POST.get('email')
        send_mail(email)
        mail_sent = True
    
    return render(request, 'index.html',{
        'mail_sent': mail_sent
    })