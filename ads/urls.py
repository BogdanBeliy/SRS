from django.urls import path
from ads.views import *

urlpatterns = [
    path('all-categories/', AllCategoriesView.as_view(), name='all_categories'),
    path('all-advertisement', ShowAllAdvertisementView.as_view(), name='all_advertisement'),
]
