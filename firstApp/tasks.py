from celery import shared_task

@shared_task
def send_mail(to):
    print(f">>> Hemos enviado el Mail a: {to}")
    return to

@shared_task
def send_welcome_mail(to):
    print(f">>> Hemos enviado el Welcome Mail a: {to}")
    return to

@shared_task
def send_subscription_mail(to):
    print(f">>> Hemos enviado el Subscription Mail a: {to}")
    return to