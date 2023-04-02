from django.urls import path
from .views import ShortAPIView, ShortCreateAPIView

app_name = 'app'
urlpatterns = [
    path('', ShortAPIView.as_view(), name='list_links'),
    path('create', ShortCreateAPIView.as_view(), name='create_api'),
    
]
