from django.shortcuts import render, redirect
from .models import Usuario



# Create your views here.
def home(request):
    return render(request, 'usuarios/home.html')

def usuario(request):
    # Salvar os dados da tela para o banco de dados 
    novo_usuario = Usuario()  
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.idade = request.POST.get('idade')
    novo_usuario.save()
    # Exibir os usuários já cadastrados em uma nova página
    usuarios = {
        'usuarios': Usuario.objects.all()
    }
    # Retornar os dados para a página de usuários
    return render(request, 'usuarios/usuarios.html', usuarios) 

