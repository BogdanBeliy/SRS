from django.urls import path
from account.views import UserView

urlpatterns = [
    path('user/<int:user_id>/', UserView.as_view(), name='user_profile'),
    # path('user-settings/<int:user_id>/', UserSettingsView.as_view(), name='user_settings'),
]