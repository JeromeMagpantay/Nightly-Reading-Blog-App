from django.urls import path
from . import views
urlpatterns = [
    path('post/<int:pk>/', views.BlogDetailView.as_view(), name='post_details'),
    path('', views.BlogListView.as_view(), name='home'),
]