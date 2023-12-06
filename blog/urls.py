from django.urls import path
from . import views

from .views import BlogListView, AboutPageView, RecognitionPageView, PredictionPageView, ClassificationPageView

urlpatterns = [
    path('', BlogListView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('recognition/', RecognitionPageView.as_view(), name='recognition'),
    path('prediction/', PredictionPageView.as_view(), name='prediction'),
    path('classification/', ClassificationPageView.as_view(), name='classification'),
    path('register/', views.register_request, name="register"),
    path('login/', views.login_request, name="login")
]