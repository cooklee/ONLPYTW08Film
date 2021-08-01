from django.urls import path, include
from accounts import views

urlpatterns = [
    # path('', include('django.contrib.auth.urls')),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('singup/', views.SignUpView.as_view(), name='signup'),
]
