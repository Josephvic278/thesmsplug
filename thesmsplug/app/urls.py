from django.urls import path
from app.views import *

app_name = 'app'

urlpatterns = [
    path ("", landingPage, name="landing_page"),
    path("dashboard/", dashBoard, name="dash_board")
]