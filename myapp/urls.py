from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name=""),
    path("counter", views.counter, name="counter"),
    path("register", views.register, name="register"),
    path("login", views.login, name="login"),
    path("myself", views.myself, name="myself"),
    path("logout", views.logout, name="logout"),
]
