from django.urls import path
from . import views

urlpatterns = [
    path('users/',views.getUsers,name='getUsers' ),
    path('users/<int:pk>',views.UserDetails.as_view()),
]