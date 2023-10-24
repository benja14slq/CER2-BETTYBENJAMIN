from django.shortcuts import render
from .models import Entidad, Comunicado

# Create your views here.
def pagina(request):
    entidades = Entidad.objects.all()
    entidad_seleccionada = None

    comunicados = Comunicado.objects.filter(visible=True).order_by('-fecha_publicacion')

    if 'entidad' in request.GET:
        entidad_id = request.GET['entidad']
        if entidad_id:
            comunicados = Comunicado.objects.filter(entidad_id=entidad_id, visible=True).order_by('-fecha_publicacion')
            entidad_seleccionada = Entidad.objects.get(id=entidad_id)
    
    Datos = {
        'entidades': entidades,
        'comunicados': comunicados,
        'entidad_seleccionada': entidad_seleccionada,
    }
    return render(request, 'miapp/base.html', Datos)

