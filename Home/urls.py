from django.urls import path,include
from . import views
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('register/', register_page, name = 'register_page'), 
    path('login/', login_page, name = 'login_page'), 
    path('logout/', logout_page, name='logout_page'),
    path('about/', about, name='about'),
]

