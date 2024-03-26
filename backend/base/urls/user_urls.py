from django.urls import path
from base.views import user_views as views

urlpatterns = [
    path('', views.get_users, name='users'),
    path('login/', views.MyTokenObtainPairView.as_view(), name='token_refresh'),
    path('register/', views.register, name='register'),
    path('profile/', views.get_user_profile, name='user_profile'),
]