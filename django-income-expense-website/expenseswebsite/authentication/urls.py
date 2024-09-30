from .views import RegistrationView, UsernameValidationView, LoginView, LogoutView
from django.urls import path
urlpatterns = [
    path('register', RegistrationView.as_view(), name="register"),
    path('login', LoginView.as_view(), name="login"),
    path('logout', LogoutView.as_view(), name="logout"),
    path('validate-username',(UsernameValidationView.as_view()),
         name="validate-username"), 
]