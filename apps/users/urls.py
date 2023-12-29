from django.urls import path
from .views import MyLoginView, Register, AdminUsers, UsersUpdate, UserDetail
from django.contrib.auth.views import LogoutView

app_name = "users"

urlpatterns = [
    path('login/', MyLoginView.as_view(template_name="users/login.html"), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path('register/', Register.as_view(), name="register"),
    path('users/', AdminUsers.as_view(), name="users"),
    path('update_user/<int:pk>', UsersUpdate.as_view(), name="update_user"),
    path('detail_user/<int:pk>', UserDetail.as_view(), name="detail_user"),
]