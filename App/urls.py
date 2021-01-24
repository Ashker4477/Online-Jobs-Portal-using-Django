from .views import *
from django.urls import path


urlpatterns = [
    path('', home, name='home'),
    path('login/', loginUser, name='login'),
    path('logout/', logoutUser, name='logout'),
    path('register/', registerUser, name='register'),
    path('apply/', applyPage, name='apply'),
]
