from django.urls import path
from .views import main_page, about_page, register_view,login_view

urlpatterns = [
    path('', main_page),
    path('about/', about_page, name = 'about'),
    path('register/', register_view, name = 'register'),
    path('login/', login_view, name = 'login'),
]