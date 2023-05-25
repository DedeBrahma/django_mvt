from django.contrib import admin
from .models import Pengguna


# Register your models here.

#1
# admin.site.register(Pengguna)

#2
class PenggunaAdmin(admin.ModelAdmin):
    list_display = ('nama', 'email', 'alamat', 'telpon')

admin.site.register(Pengguna, PenggunaAdmin)

