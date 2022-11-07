from account import views
from django.urls import path
from django.contrib.auth import views as auth_views

app_name = 'account'
urlpatterns = [
    # path('login/', views.user_login, name='login'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('password_change/', auth_views.PasswordChangeView.as_view(),
         name='password_change'),
    path('password_change/done', auth_views.PasswordChangeDoneView.as_view(),
         name='password_change_done'),  # success message after change i.e password changed successfully
    #  I forgot my password
    path("password_reset/", auth_views.PasswordResetView.as_view(),
         name="password_reset"),
    path("password_reset/done/", auth_views.PasswordResetDoneView.as_view(),
         name="password_reset_done"),  # please check your email for a link to change /reset your password.Someone has hit reset on your account
    path("reset/<uid64>/<token>/", auth_views.PasswordResetConfirmView.as_view(),
         name="password_reset_confirm"),  # view to show after click of email view
    path("reset/done/", auth_views.PasswordResetDoneView.as_view(),
         name="password_reset_complete"),
    path('', views.dashboard, name='dashboard'),

]
