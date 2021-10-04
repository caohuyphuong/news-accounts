from django.shortcuts import redirect, render
from django.views import View
from django.views import generic
from .models import Dan, Tiem
from .forms import DanForm, DanModelForm

# CRUD = Create, Read, Update, Delete


class DashboardView(generic.TemplateView):
    template_name = 'dashboard.html'


class DanListView(generic.ListView):
    template_name = 'tiemchung/list.html'
    queryset = Dan.objects.all()


def dan_list(request):
    object_list = Dan.objects.all()
    return render(request, 'tiemchung/list.html', {'object_list': object_list})


def dan_detail(request, pk):
    object = Dan.objects.get(pk=pk)
    return render(request, 'tiemchung/detail.html', {'object': object})


def dan_create(request):
    # form = DanForm(request.POST or None)
    if request.method == "POST":
        form = DanModelForm(request.POST)
        if form.is_valid():
            # print(form.cleaned_data)
            # cccd = form.cleaned_data['cccd']
            # ten = form.cleaned_data['ten']
            # dan = Dan.objects.create(cccd=cccd, ten=ten)
            form.save()
            return redirect('tiemchung:dan-list')
    else:
        form = DanModelForm()
    return render(request, 'tiemchung/create.html', {'form': form})


def dan_update(request, pk):
    dan = Dan.objects.get(pk=pk)
    if request.method == "POST":
        dan.cccd = request.POST.get('cccd')
        dan.ten = request.POST.get('ten')
        dan.save()
        return redirect('tiemchung:dan-list')
    return render(request, 'tiemchung/update.html', {'object': dan})


def dan_update_form(request, pk):
    dan = Dan.objects.get(pk=pk)
    form = DanForm(request.POST or None, initial={
        'cccd': dan.cccd,
        'ten': dan.ten
    })
    if form.is_valid():
        dan.cccd = form.cleaned_data.get('cccd')
        dan.ten = form.cleaned_data.get('ten')
        dan.save()
        return redirect('tiemchung:dan-list')
    return render(request, 'tiemchung/update.html', {'form': form})


def dan_update_model_form(request, pk):
    dan = Dan.objects.get(pk=pk)
    form = DanModelForm(request.POST or None, instance=dan)
    if form.is_valid():
        form.save()
        return redirect('tiemchung:dan-list')
    return render(request, 'tiemchung/update.html', {'form': form})


def dan_delete(request, pk):
    dan = Dan.objects.get(pk=pk)
    dan.delete()
    return redirect('tiemchung:dan-list')
