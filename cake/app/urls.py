from django.urls import path
from . import views


urlpatterns = [
  
    path('',views.index ,name="index"),
    path('app/',views.app,name='app'),
    path('ele/',views.ele,name='ele'),
    path('login/',views.user_login,name='login'),
    path('logout/',views.user_logout,name='logout'),
    path('register/',views.register,name='register'),
]