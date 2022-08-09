import time
from django.core.mail import send_mail
from core.celery import app


@app.task
def celery_send_post_registration_email(code, email):
    full_link = f'http://localhost:8000/account/activate/{code}/'
    send_mail(
        'Do not forger to activate your account',  # topic
        full_link,  # content
        'esenturdildebekov8@gmail.com',  # from
        [email]  # to
    )


@app.task
def celery_send_info_about_activation(email):
    link = 'You can log in ! http://localhost:8000/account/login/'
    send_mail(
        'You activated your account !',
        {link},
        'esenturdildebekov8@gmail.com',
        [email]
    )


@app.task
def celery_forgot_password_email(code, email):
    send_mail(
        'Password recovery',
        f'Your confirmation code : {code}. Please use the code at this link '
        f'http://localhost:8000/account/forgot_password_complete/',
        'esenturdildebekov8@gmail.com',
        [email]
    )
