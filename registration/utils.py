from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


def send_login_email(user, code):

    account_url = f"http://127.0.0.1:8000/accounts/change_password/?name={user.username}/"

    html_content = render_to_string(
        "emails/login_successful.html",
        {
            "user": user,
            "account_url": account_url,
            'code': code
        }
    )

    email = EmailMultiAlternatives(
        subject="Login Successful",
        body="Get this 6-digit code to reset your password",
        from_email=settings.EMAIL_HOST_USER,
        to=[user.email,settings.EMAIL_HOST_USER],
    )

    email.attach_alternative(html_content, "text/html")

    email.send()


import random
# Create your tests here.

def create_code():
    code = random.randint(100000, 999999)
    return str(code)