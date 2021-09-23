from django.urls import path
from .views import AuthView, UserDetailsAPIView


app_name = 'accounts'

urlpatterns = [
    path('auth/', AuthView.as_view(), name="auth_view"),
    path('<id>/', UserDetailsAPIView.as_view(), name='user_details')
]
