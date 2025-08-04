from django.urls import path
from .views import register, login_view, logout_view, me_view, verify_email, resend_otp

urlpatterns = [
    path('register/', register, name='register'),
    path('verify-email/', verify_email, name='verify_email'),
    path('resend-otp/', resend_otp, name='resend_otp'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('me/', me_view, name='me'),
]