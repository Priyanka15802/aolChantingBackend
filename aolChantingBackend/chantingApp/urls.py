from django.conf.urls import url,include
from django.urls import include, path
from django.contrib import admin
from .views import *
from . import views


urlpatterns = [

path("api/register_user/", register_user, name="register_user"),
path("api/login/", login, name="login"),
path("api/add_chants/", add_chants, name="add_chants"),
path("api/chanting_dashboard/", chanting_dashboard, name="chanting_dashboard"),
# path("api/get_user_chant_details/", get_user_chant_details, name="get_user_chant_details"),
path("api/add_japa/", add_japa, name="add_japa"),
path("api/view_all_users/", view_all_users, name="view_all_users"),
# path("api/get_chant_tot_count/", get_chant_tot_count, name="get_chant_tot_count"),

]