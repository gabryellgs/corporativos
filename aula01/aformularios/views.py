from django.shortcuts import render

def cadastro(request):
    return render(request, 'cadastro.html')

def dados(request):
    nome = request.POST['nome']
    cpf = request.POST['cpf']
    disc = request.POST['disc']
    context = {
        'nome':nome,
        'cpf':cpf,
        'disc':disc
    }
    return render(request, 'dados.html', context)