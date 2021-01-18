from django.urls import path
from . import views
urlpatterns=[
    path('',views.home,name='home'),
    path('admin',views.admin,name='admin'),
    path('adm_login',views.adm_login,name='adm_login'),
    path('user',views.user,name='user'),
    path('login',views.validate,name='validate'),
    path('signup',views.signup,name='signup'),
   
]