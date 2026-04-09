from django.urls import path
from .views import *

urlpatterns = [
    path('',homeView,name="homeView"),
    path("register/",register_user,name="registerUser"),
    path("login_view/",login_view,name="login"),
    path("logout_view/",logout_view,name="logout"),
    path("createView/",createView,name="createView"),
    
    path("editview/<int:id>/",editview,name="editview"),
]
