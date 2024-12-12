from django.db import models
from django.shortcuts import reverse



class Music(models.Model):
    album_title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    release_year = models.DateField()
    genre = models.CharField(max_length=100)


    def get_detail_url(self):
        return reverse('music:detail', args=[self.pk])


    def get_delete_url(self):
        return reverse('music:delete', args=[self.pk])


    def get_update_url(self):
        return reverse('music:update', args=[self.pk])


