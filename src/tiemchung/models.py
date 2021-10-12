from django.shortcuts import redirect
from django.utils import timezone
from django.db import models
from django.urls import reverse


class Dan(models.Model):
    cccd = models.CharField(max_length=20, unique=True)
    ten = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Dan'

    def __str__(self):
        return self.cccd

    def get_absolute_url(self, *args, **kwargs):
        return reverse('tiemchung:dan-detail', kwargs={'pk': self.pk})


class Vaccine(models.Model):
    title = models.CharField(max_length=50)
    made_in = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Vaccine'

    def __str__(self):
        return self.title


class Tiem(models.Model):
    dan = models.ForeignKey(Dan, on_delete=models.CASCADE)
    ngay_tiem = models.DateTimeField(default=timezone.now)
    noi_tiem = models.CharField(max_length=100)
    vaccine = models.ForeignKey(
        Vaccine, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Tiem'

    def __str__(self):
        return self.dan.cccd
