from django.urls import path
from ads.views import *

urlpatterns = [
    path('categories/', ShowAllCategoriesView.as_view(), name='all_categories'),
]
