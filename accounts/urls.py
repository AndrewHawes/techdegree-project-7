from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from . import views

urlpatterns = [
    path('sign_in/', LoginView.as_view(template_name='accounts/sign_in.html'), name='sign_in'),
    path('sign_up/', views.SignUpView.as_view(), name='sign_up'),
    path('sign_out/', LogoutView.as_view(), name='sign_out'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('profile/edit/', views.EditProfileView.as_view(), name='edit'),
    path('change_password/', views.change_password, name='change_password')
]
