from django.shortcuts import redirect, render
from django.views import View
from .models import Dan, Tiem
from .forms import DanForm
# CRUD = Create, Read, Update, Delete


def dan_list(request):
    object_list = Dan.objects.all()
    return render(request, 'tiemchung/list.html', {'object_list': object_list})


def dan_detail(request, pk):
    object = Dan.objects.get(pk=pk)
    return render(request, 'tiemchung/detail.html', {'object': object})


def dan_create(request):
    form = DanForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            print(form.cleaned_data)
            cccd = form.cleaned_data['cccd']
            ten = form.cleaned_data['ten']
            # cccd = request.POST.get('cccd')
            # ten = request.POST.get('ten')
            dan = Dan.objects.create(cccd=cccd, ten=ten)
            return redirect('tiemchung:dan-list')
    return render(request, 'tiemchung/create.html', {'form': form})


def dan_update(request, pk):
    dan = Dan.objects.get(pk=pk)
    if request.method == "POST":
        dan.cccd = request.POST.get('cccd')
        dan.ten = request.POST.get('ten')
        dan.save()
        return redirect('tiemchung:dan-list')
    return render(request, 'tiemchung/update.html', {'object': dan})


def dan_delete(request, pk):
    dan = Dan.objects.get(pk=pk)
    dan.delete()
    return redirect('tiemchung:dan-list')
