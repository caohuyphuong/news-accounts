from django.shortcuts import render
from .models import Dan, Tiem
# CRUD = Create, Read, Update, Delete


def dan_list(request):
    object_list = Dan.objects.all()
    return render(request, 'list.html', {'object_list': object_list})


def dan_detail(request, pk):
    object = Dan.objects.get(pk=pk)
    return render(request, 'detail.html', {'object': object})
