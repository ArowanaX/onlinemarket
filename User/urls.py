from django.urls import path
<<<<<<< HEAD
from .views import forget_password, login, logout, register, activate,forget_pass,set_true,show_profile

=======
from django.urls.conf import re_path

from .views import forget_password, login, logout, register, activate,forget_pass,user_session_logedin
>>>>>>> 383575db56cb3953b3f744017113aa5380f7d088
app_name="User"

urlpatterns = [
    path("login/", login, name="login"),
    path("logout/", logout, name="logout"),
    path("register/", register, name="register"),
    path("activate/<str:valid>", activate, name="activate"),
    path("forget_password/", forget_password, name="forget_password"),
    path("forget_pass/", forget_pass, name="forget_pass"),
<<<<<<< HEAD
    path("set_true/<str:auten>", set_true, name="set_true"),
    path('profile/<int:id>',show_profile.as_view(),name="profile"),
=======
    path("linked_dev/", user_session_logedin, name="user_session"),

>>>>>>> 383575db56cb3953b3f744017113aa5380f7d088


]
