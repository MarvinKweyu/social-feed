from account import views
from django.urls import path

app_name = 'account'
urlpatterns = [path('login/', views.user_login, name='login')]
