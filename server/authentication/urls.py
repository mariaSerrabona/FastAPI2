from django.contrib import admin


from django.urls import path, include
from .views import LoginView, LogoutView
from .views import LoginView, LogoutView, SignupView
from .views import LoginView, LogoutView, SignupView, ProfileView

urlpatterns = [
        # Auth views
        path("admin/", admin.site.urls),
        path('auth/login/',
            LoginView.as_view(), name='auth_login'),
        path('auth/logout/',
            LogoutView.as_view(), name='auth_logout'),
        path('auth/singup/',SignupView.as_view(), name='auth_signup'),
        path('auth/reset/', include('django_rest_passwordreset.urls',
            namespace='password_reset')),
        path('user/profile/',
            ProfileView.as_view(), name='user_profile'),
        ]
