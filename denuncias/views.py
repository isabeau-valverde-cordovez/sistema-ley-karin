from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Denuncia
from .forms import DenunciaForm

def lista_denuncias(request):
    denuncias = Denuncia.objects.all()
    return render(request, 'denuncias/lista.html', {'denuncias': denuncias})

def nueva_denuncia(request):
    if request.method == 'POST':
        form = DenunciaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_denuncias')
    else:
        form = DenunciaForm()
    return render(request, 'denuncias/nueva.html', {'form': form})

def acerca_de(request):
    return render(request, 'denuncias/acerca_de.html')

def contacto(request):
    return render(request, 'denuncias/contacto.html')