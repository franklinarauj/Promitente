from django.shortcuts import render, redirect
from app.forms import ClienteForm
from app.models import TB_Cliente


def home(request):
    return render(request, 'app/home.html')


def cadastrar_cliente(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/pesquisar-clientes/')
    else:
        form = ClienteForm()
        return render(request, 'app/cadastrar-cliente.html', {'form': form})


def pesquisar_clientes(request):
    clientes = TB_Cliente.objects.all()
    return render(request, 'app/pesquisar-clientes.html', {'clientes': clientes})


def atualizar_cadastro(request, cpf):
    dados = {}
    cliente = TB_Cliente.objects.get(cpf=cpf)
    form = ClienteForm(request.POST or None, instance=cliente)
    dados['cliente'] = cliente
    dados['form'] = form
    if form.is_valid():
        form.save()
        return redirect('/pesquisar-clientes/')
    return render(request, 'app/atualizar-cadastro.html', dados)


def excluir_cliente(request, cpf):
    cliente = TB_Cliente.objects.get(cpf=cpf)
    cliente.delete()
    return redirect('/pesquisar-clientes/')
