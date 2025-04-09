from django.shortcuts import render, get_object_or_404, redirect
from .models import Pagamento
from .forms import PagamentoForm
from rest_framework import viewsets
from .serializers import PagamentoSerializer
from django.http import HttpResponse

def index(request):
    return render(request, 'pagamentos/index.html')

def listar_pagamentos(request):
    pagamentos = Pagamento.objects.all()
    return render(request, 'pagamentos/listar.html', {'pagamentos': pagamentos})

def criar_pagamentos(request):
    if request.method == 'POST':
        form = PagamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_pagamentos')
    else:
        form = PagamentoForm()
    return render(request, 'pagamentos/form.html', {'form': form})

def detalhes_pagamento(request, id):
    pagamento = get_object_or_404(Pagamento, id=id)
    return render(request, 'pagamentos/detalhes.html', {'pagamento': pagamento})

def editar_pagamentos(request, id):
    pagamento = get_object_or_404(Pagamento, id=id)
    if request.method == 'POST':
        form = PagamentoForm(request.POST, instance=pagamento)
        if form.is_valid():
            form.save()
            return redirect('listar_pagamentos')
    else:
        form = PagamentoForm(instance=pagamento)
    return render(request, 'pagamentos/form.html', {'form': form})

def excluir_pagamentos(request, id):
    pagamento = get_object_or_404(Pagamento, id=id)
    if request.method == 'POST':
        pagamento.delete()
        return redirect('listar_pagamentos')
    return render(request, 'pagamentos/confirmar_exclusao.html', {'pagamento': pagamento})

def relatorios(request):
    return render(request, 'pagamentos/relatorios.html')

class PagamentoViewSet(viewsets.ModelViewSet):
    queryset = Pagamento.objects.all()  # Retorna todos os pagamentos do banco
    serializer_class = PagamentoSerializer  # Usa o serializer para formatar os dados