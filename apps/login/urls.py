from django.urls import path

from apps.login.views import RegisterView

app_name = 'login'

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
]