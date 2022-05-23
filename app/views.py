from django.conf import settings
from django.shortcuts import redirect, render
from rest_framework.generics import ListAPIView , CreateAPIView
from django.views import View

from app.serializer import LinkSerializer
from .models import LinkModel

class ShortAPIView(ListAPIView):
    queryset = LinkModel.objects.all().order_by('-date_created')
    serializer_class = LinkSerializer

class ShortCreateSAPIView(CreateAPIView):
    serializer_class = LinkSerializer

class RedirectView(View):
    def get(self, request, short_link, *args,**kwargs):
        short_link = settings.HOST_URL+'/'+self.kwargs['short_link']
        redirect_link = LinkModel.objects.filter(short_link=short_link).first().original_link
        return redirect(redirect_link)