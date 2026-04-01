from django.shortcuts import render


def saludos(request):
    contexto = {"nombres":  ["Facu", "Juancito", "Pepito"]}
    return render(request,'saludos/hola.html', contexto)

def despedir(request):
    return render(render, 'saludos/adios.html')
