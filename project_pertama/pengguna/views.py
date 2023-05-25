from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Pengguna

#1
# def pengguna(request):
#     return HttpResponse("Selamat Datang Pengguna")

#2
# def pengguna(request):
#     template = loader.get_template('pengguna.html')
#     return HttpResponse(template.render())

#3
# def pengguna(request):
#     context = {
#         'nama': 'Dede'
#     }
#     template = loader.get_template('pengguna.html')
#     return HttpResponse(template.render(context, request))


#4
# def pengguna(request):
#     context = {
#         'nama': 'Dede'
#     }
#     template = loader.get_template('pengguna.html')
#     return HttpResponse(template.render(context, request))

# def penggunadb(request):
#     data = Pengguna.objects.all().values()[5]
#     context = {
#         'data_pengguna': data
#     }
#     template = loader.get_template('pengguna2.html')
#     return HttpResponse(template.render(context, request))

#5
# def pengguna(request):
#     context = {
#         'nama': 'Dede'
#     }
#     template = loader.get_template('pengguna.html')
#     return HttpResponse(template.render(context, request))

# def penggunadb(request):
#     data = Pengguna.objects.all().values()[5]
#     context = {
#         'data_pengguna': data
#     }
#     template = loader.get_template('pengguna2.html')
#     return HttpResponse(template.render(context, request))

# def logic(request):
#     template = loader.get_template('logic.html')
#     return HttpResponse(template.render())


#6
# def pengguna(request):
#     context = {
#         'nama': 'Dede'
#     }
#     template = loader.get_template('pengguna.html')
#     return HttpResponse(template.render(context, request))

# def penggunadb(request):
#     data = Pengguna.objects.all().values()[5]
#     context = {
#         'data_pengguna': data
#     }
#     template = loader.get_template('pengguna2.html')
#     return HttpResponse(template.render(context, request))

# def logic(request):
#     template = loader.get_template('logic.html')
#     return HttpResponse(template.render())

# def forloop(request):
#     data = Pengguna.objects.all().values()
#     context = {
#         'data_pengguna': data
#     }
#     template = loader.get_template('forloop.html')
#     return HttpResponse(template.render(context, request))


#7
# def pengguna(request):
#     context = {
#         'nama': 'Dede'
#     }
#     template = loader.get_template('pengguna.html')
#     return HttpResponse(template.render(context, request))

# def penggunadb(request):
#     data = Pengguna.objects.all().values()[5]
#     context = {
#         'data_pengguna': data
#     }
#     template = loader.get_template('pengguna2.html')
#     return HttpResponse(template.render(context, request))

# def logic(request):
#     template = loader.get_template('logic.html')
#     return HttpResponse(template.render())

# def forloop(request):
#     data = Pengguna.objects.all().values()
#     context = {
#         'data_pengguna': data
#     }
#     template = loader.get_template('forloop.html')
#     return HttpResponse(template.render(context, request))

# def allPengguna(request):
#     data = Pengguna.objects.all().values()
#     context = {
#         'data_pengguna': data
#     }
#     template = loader.get_template('all_pengguna.html')
#     return HttpResponse(template.render(context, request))

# def detailPengguna(request, id):
#     data = Pengguna.objects.get(id=id)
#     context = {
#         'data_pengguna': data
#     }
#     template = loader.get_template('detail_pengguna.html')
#     return HttpResponse(template.render(context, request))


#8
def pengguna(request):
    context = {
        'nama': 'Dede'
    }
    template = loader.get_template('pengguna.html')
    return HttpResponse(template.render(context, request))

def penggunadb(request):
    data = Pengguna.objects.all().values()[5]
    context = {
        'data_pengguna': data
    }
    template = loader.get_template('pengguna2.html')
    return HttpResponse(template.render(context, request))

def logic(request):
    template = loader.get_template('logic.html')
    return HttpResponse(template.render())

def forloop(request):
    data = Pengguna.objects.all().values()
    context = {
        'data_pengguna': data
    }
    template = loader.get_template('forloop.html')
    return HttpResponse(template.render(context, request))

def allPengguna(request):
    data = Pengguna.objects.all().values()
    context = {
        'data_pengguna': data
    }
    template = loader.get_template('all_pengguna.html')
    return HttpResponse(template.render(context, request))

def detailPengguna(request, id):
    data = Pengguna.objects.get(id=id)
    context = {
        'data_pengguna': data
    }
    template = loader.get_template('detail_pengguna.html')
    return HttpResponse(template.render(context, request))

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

# Create your views here.
