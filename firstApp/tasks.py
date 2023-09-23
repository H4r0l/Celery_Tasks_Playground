from celery import shared_task

@shared_task
def send_mail(to):
    print(f">>> Hemos enviado el Mail a: {to}")