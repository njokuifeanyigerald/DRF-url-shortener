from django.urls import path
from .views import ShortAPIView, ShortCreateSAPIView, RedirectView

app_name = 'app'
urlpatterns = [
    path('', ShortAPIView.as_view(), name='list_links'),
    path('create', ShortCreateSAPIView.as_view(), name='create_api'),
    path('<str:short_link>/', RedirectView.as_view(), name='redirect')
]
