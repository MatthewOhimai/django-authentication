from django.core.mail import send_mail
from django.conf import settings

def send_otp_email(user):
    otp = user.generate_otp()
    subject = "Verify your account"
    message = f"Your OTP code is: {otp}. It will expire in 10 minutes."
    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [user.email])
