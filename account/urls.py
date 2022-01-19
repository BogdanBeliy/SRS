from django.urls import path
from account.views import AllUserView

urlpatterns = [
    path('all-users/', AllUserView.as_view(), name='all_users'),
]