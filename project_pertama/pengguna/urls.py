from django.urls import path
from . import views

#1
# urlpatterns = [
#     path('pengguna/', views.pengguna, name='pengguna'),
# ]


#2
# urlpatterns = [
#     path('pengguna/', views.pengguna, name='pengguna'),
#     path('penggunadb/', views.penggunadb, name='penggunadb'),
# ]


#3
# urlpatterns = [
#     path('pengguna/', views.pengguna, name='pengguna'),
#     path('penggunadb/', views.penggunadb, name='penggunadb'),
#     path('logic/', views.logic, name='logic'),
# ]


#4
# urlpatterns = [
#     path('pengguna/', views.pengguna, name='pengguna'),
#     path('penggunadb/', views.penggunadb, name='penggunadb'),
#     path('logic/', views.logic, name='logic'),
#     path('forloop/', views.forloop, name='forloop'),
# ]


#5
# urlpatterns = [
#     path('pengguna/', views.pengguna, name='pengguna'),
#     path('penggunadb/', views.penggunadb, name='penggunadb'),
#     path('logic/', views.logic, name='logic'),
#     path('forloop/', views.forloop, name='forloop'),
#     path('allpengguna/', views.allPengguna, name='allpengguna'),
#     path('allpengguna/detailpengguna/<int:id>', views.detailPengguna, name='detailpengguna'),
# ]


#6
urlpatterns = [
    path('pengguna/', views.pengguna, name='pengguna'),
    path('penggunadb/', views.penggunadb, name='penggunadb'),
    path('logic/', views.logic, name='logic'),
    path('forloop/', views.forloop, name='forloop'),
    path('allpengguna/', views.allPengguna, name='allpengguna'),
    path('allpengguna/detailpengguna/<int:id>', views.detailPengguna, name='detailpengguna'),
    path('', views.index, name='index'),
]