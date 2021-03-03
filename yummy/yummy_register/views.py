from django.shortcuts import render, redirect
from .forms import produtoForm
from .models import Produto
# Create your views here.


def produto_list(request):
    context = {'produto_list': Produto.objects.all()}
    return render(request, "yummy_register/produto_list.html", context)


def produto_form(request, id=0):
    if request.method == "GET":
        if id==0:
            form = produtoForm()
        else:
            prod = Produto.objects.get(pk=id)
            form = produtoForm(instance=prod)
        return render(request, "yummy_register/produto_form.html", {'form':form})
    else:
        if id==0:
            form = produtoForm(request.POST)
        else:
            prod = Produto.objects.get(pk=id)
            form = produtoForm(request.POST, instance=prod)
        if form.is_valid():
            form.save()
        return redirect('/produto/list')


def produto_delete(request, id):
    prod = Produto.objects.get(pk=id)
    prod.delete()
    return redirect('/produto/list')