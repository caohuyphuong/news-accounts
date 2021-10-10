from django.shortcuts import get_object_or_404, redirect, render
from django.urls.base import reverse, reverse_lazy
from django.views import generic, View
from django.db.models import Q
from .models import Dan, Tiem
from .forms import DanForm, DanModelForm, SearchForm

# CRUD = Create, Read, Update, Delete


class DashboardView(generic.TemplateView):
    template_name = 'dashboard.html'


class DanListView(generic.ListView):
    template_name = 'tiemchung/list.html'
    queryset = Dan.objects.all()


class DanDetailView(generic.DetailView):
    template_name = 'tiemchung/detail.html'
    queryset = Dan.objects.all()


class DanCreateView(generic.CreateView):
    template_name = 'tiemchung/create.html'
    form_class = DanModelForm
    queryset = Dan.objects.all()
    success_url = reverse_lazy('tiemchung:dan-list')


class DanUpdateView(generic.UpdateView):
    template_name = 'tiemchung/update.html'
    form_class = DanModelForm
    queryset = Dan.objects.all()
    success_url = reverse_lazy('tiemchung:dan-list')


class DanDeleteView(generic.DeleteView):
    template_name = 'tiemchung/delete.html'
    queryset = Dan.objects.all()
    success_url = reverse_lazy('tiemchung:dan-list')


class SearchView(View):
    template_name = 'tiemchung/search.html'
    form_class = SearchForm

    def get(self, request, *args, **kwargs):
        form = self.form_class(request.GET or None)
        q = request.GET.get('q')
        qs = Dan.objects.all()
        if q is not None:
            qs = qs.filter(Q(cccd__icontains=q) | Q(ten__icontains=q))

        context = {
            'form': form,
            'object_list': qs
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        pass
