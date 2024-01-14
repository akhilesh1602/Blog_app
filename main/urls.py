from django.urls import path
from . import views
urlpatterns = [
    path("",views.home, name = "home"),
    path("login",views.login, name = "login"),
    path("register",views.register, name = "register"),
    path("logout",views.logout, name = "logout"),
    path("create_post",views.create_post, name = "create_post"),
    path("dashboard", views.dashboard, name = "dashboard"),
    path('get_articles/<int:pk>', views.get_articles, name = "get_articles"),
    path("comments/<int:pk>", views.comments, name = "comments")

]