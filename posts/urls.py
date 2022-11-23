from django.urls import path
from .views import (
        PostListView, 
        PostDetailView,
        PostCreateView,
        HomePageView,
        AboutPageView,
)


urlpatterns = [
    path('', PostListView.as_view(), name='list'),
    path('<int:pk>/', PostDetailView.as_view(), name='detail'),
    path('new/', PostCreateView.as_view(), name='new'),
    path('home/', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
]