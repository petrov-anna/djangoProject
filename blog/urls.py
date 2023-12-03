from django.urls import path

from .views import BlogListView, AboutPageView, ImputationPageView

urlpatterns = [
    path('', BlogListView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('imputation/', ImputationPageView.as_view(), name='imputation')
]