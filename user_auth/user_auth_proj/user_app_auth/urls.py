from django.urls import path
from user_app_auth import views

app_name="user_app_auth"

urlpatterns = [
    path('register/',views.register,name="register"),
    path('login/',views.user_login,name="user_login")
]
