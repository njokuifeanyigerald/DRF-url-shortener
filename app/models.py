from random import choices
from string import ascii_letters
from django.conf import settings
from django.db import models


class LinkModel(models.Model):
    original_link = models.URLField()
    short_link = models.URLField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.original_link

    def shortener(self):
        while True:
            random_string = ''.join(choices(ascii_letters, k=6))
            new_link=settings.HOST_URL+'/'+random_string
            if not LinkModel.objects.filter(short_link=new_link).exists():
                break
        return new_link

    def save(self, *args, **kwargs):
        if not self.short_link:
            new_link = self.shortener()
            self.short_link = new_link
        return super().save(*args, **kwargs)