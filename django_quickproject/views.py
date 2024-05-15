from django.shortcuts import render
#@login_required
def login(request):
    # Lógica de login, se necessário
    return render(request, 'core/index.html')  # Renderiza o template de login
def registro(request):
    # Lógica de registro, se necessário
    return render(request, 'core/registro.html')  # Renderiza o template de registro

# def simula_view(request):
#     # Lógica para a página de simulação, se necessário
#     return render(request, os.path.join(os.path.dirname(__file__), '..', '../../front/index__simulador.html'))

from django.shortcuts import redirect

def simula_view(request):
    # Lógica para a página de simulação, se necessário
    return render(request, os.path.join(os.path.dirname(__file__), '..', './template/index__simulador.html'))

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def minha_view(request):
    # Seu código aqui
    return render(request, 'template/index.html')  