from django.shortcuts import render, redirect
from delta.forms import CadastroForm
from delta.models import Cadastro
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
def home(request):
    data = {}
    search = request.GET.get('search')
    all_items = Cadastro.objects.all().order_by('-id')

    if search:
        search_results = all_items.filter(sinistro__icontains=search)
        paginator = Paginator(search_results, 10)
    else:
        paginator = Paginator(all_items, 10)

    page = request.GET.get('page')
    try:
        db = paginator.page(page)
    except PageNotAnInteger:
        db = paginator.page(1)
    except EmptyPage:
        db = paginator.page(paginator.num_pages)

    data['db'] = db
    return render(request, 'index.html', data)


def form(request):
    data = {}
    data['form'] = CadastroForm()
    return render(request, 'form.html', data)


def create(request):
    form = CadastroForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    else:
        print('Formulário inválido:', form.errors)


def view(request, pk):
    data = {}
    data['db'] = Cadastro.objects.get(pk=pk)
    return render(request, 'view.html', data)


def edit(request, pk):
    data = {}
    data['db'] = Cadastro.objects.get(pk=pk)
    data['form'] = CadastroForm(instance=data['db'])
    return render(request, 'form.html', data)


def update(request, pk):
    data = {}
    data['db'] = Cadastro.objects.get(pk=pk)
    form = CadastroForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('home')


def delete(request, pk):
    db = Cadastro.objects.get(pk=pk)
    db.delete
    return redirect('home')

