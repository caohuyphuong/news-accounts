from django.utils import timezone
from django.db import models


class Dan(models.Model):
    cccd = models.CharField(max_length=20, unique=True)
    ten = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Dan'

    def __str__(self):
        return self.cccd


class Tiem(models.Model):
    dan = models.ForeignKey(Dan, on_delete=models.CASCADE)
    ngay_tiem = models.DateTimeField(default=timezone.now)
    noi_tiem = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Tiem'

    def __str__(self):
        return self.dan.cccd
