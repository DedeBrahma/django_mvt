from django.db import models

class Pengguna (models.Model):
    nama = models.CharField(max_length=50)
    alamat = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    telpon = models.IntegerField(null=True)

    def __str__(self):
        return self.nama
    
    class Meta:
        verbose_name_plural ="Pengguna"

# Create your models here.
