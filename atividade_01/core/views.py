from django.shortcuts import render

def quiz(request):
    return render(request, 'quiz.html')

def resposta(request):
    if request.method == "POST":    
        nome = request.POST['nome']         
        barco = request.POST['barco']      
        usuario = request.POST['usuario']   
        resposta_barco = "Moby Dick"
        resposta_nome = "Edward Newgate"
        acertou_barco = barco == resposta_barco
        acertou_nome = nome == resposta_nome

        context = {
            'nome': nome,
            'barco': barco,
            'usuario': usuario,
            'acertou_barco': acertou_barco,
            'acertou_nome': acertou_nome,
            'resposta_barco': resposta_barco,
            'resposta_nome': resposta_nome,
        }

        return render(request, 'resposta.html', context)
    else:
        return render(request, 'resposta.html')
