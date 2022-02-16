from django.urls import path
from ads.views import ShowAllCategoriesView, AdvByCatView, AdvDetailView

urlpatterns = [
    path('categories/', ShowAllCategoriesView.as_view(), name='all_categories'),
    path('by-category/', AdvByCatView.as_view(), name='adv_by_cat'),
    path('detail/', AdvDetailView.as_view(), name='detail'),
]
