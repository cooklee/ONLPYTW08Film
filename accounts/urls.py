from django.urls import path, include
from accounts import views

urlpatterns = [
    # path('', include('django.contrib.auth.urls')),
    path('login/', views.LoginView.as_view(), name='login'),
]
