from django.shortcuts import redirect, render
from .models import Dan, Tiem
# CRUD = Create, Read, Update, Delete


def dan_list(request):
    object_list = Dan.objects.all()
    return render(request, 'list.html', {'object_list': object_list})


def dan_detail(request, pk):
    object = Dan.objects.get(pk=pk)
    return render(request, 'detail.html', {'object': object})


def dan_create(request):
    if request.method == "POST":
        cccd = request.POST.get('cccd')
        ten = request.POST.get('ten')
        dan = Dan.objects.create(cccd=cccd, ten=ten)
        return redirect('/list')
    return render(request, 'create.html', {})


def dan_update(request, pk):
    dan = Dan.objects.get(pk=pk)
    if request.method == "POST":
        dan.cccd = request.POST.get('cccd')
        dan.ten = request.POST.get('ten')
        dan.save()
        return redirect('/list')
    return render(request, 'update.html', {'object': dan})


def dan_delete(request, pk):
    dan = Dan.objects.get(pk=pk)
    dan.delete()
    return redirect('/list')
