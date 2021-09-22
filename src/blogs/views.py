from django.shortcuts import get_object_or_404, redirect, render
from .models import Category

# Create your views here.


def Dashboard(request):
    return render(request, 'dashboard.html', {})


def category_create(request):
    if request.method == "POST":
        title = request.POST.get('title')
        Category.objects.create(title=title)
        return redirect('/category_list')

    return render(request, 'category_create.html', {})


def category_list(request):
    qs = Category.objects.all()
    return render(request, 'category_list.html', {'object_list': qs})


def category_detail(request, pk):
    cate = get_object_or_404(Category, pk=pk)
    return render(request, 'category_detail.html', {'object': cate})


def category_update(request, pk):
    cate = Category.objects.get(pk=pk)
    if request.method == "POST":
        cate.title = request.POST.get('title')
        cate.save()
        return redirect('/category_list')
    return render(request, 'category_update.html', {'object': cate})


def category_delete(request, pk):
    cate = Category.objects.get(pk=pk)
    cate.delete()
    return redirect('/category_list')
