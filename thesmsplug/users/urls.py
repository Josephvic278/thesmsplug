from django.urls import path
from users.views import *

app_name = 'users'

urlpatterns = [
    path ("signup/", signup, name="signup"),
    path("login/", login_view, name="login"),
    path("logout/", logout, name="logout")
]