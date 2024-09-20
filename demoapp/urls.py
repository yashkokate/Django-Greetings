from django.urls import path
from . import views

urlpatterns = [
    path('set-cookie-session/', views.set_cookie_and_session, name='set_cookie_and_session'),
    path('set-cookie/', views.set_cookie, name='set_cookie'),
    path('get-cookie/', views.get_cookie, name='get_cookie'),
    path('set-session/', views.set_session, name='set_session'),
    path('get-session/', views.get_session, name='get_session'),
    path('show-info/', views.show_info, name='show_info'),
]
