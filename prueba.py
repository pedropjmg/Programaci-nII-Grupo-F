from django.http import HttpResponse
def saludo(request):
    retutn HttpResponse("Hola mundo desde Django")