from django.urls import path
from movie import views

urlpatterns = [
    path('', views.AddMovieView.as_view(), name='add_movie'),
    path('list_movie/', views.ListMovieView.as_view(), name='list_movie'),
    path('add_actor/', views.AddActorView.as_view(), name='add_actor'),
    path('list_actor/', views.ListActorView.as_view(), name='list_actor'),
    path('detailActorView/<int:pk>/', views.DetailActorView.as_view(), name='detail_actor'),
    path('UpdateActorView/<int:pk>/', views.UpdateActorView.as_view(), name='update_actor'),
    path('DeleteActorView/<int:pk>/', views.DeleteActorView.as_view(), name='delete_actor'),
]
