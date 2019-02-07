from django.http import HttpResponse

def inicio(request):
    return HttpResponse('Hola mundo')

def autor(request):
    return HttpResponse('Desarrollado por Fred Paucar')

