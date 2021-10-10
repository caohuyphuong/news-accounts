from django.urls import path
from tiemchung.forms import SearchForm
from tiemchung.views import (
    DanCreateView,
    DanDeleteView,
    DanDetailView,
    DanUpdateView,
    DanListView,
    SearchView
)

app_name = 'tiemchung'

urlpatterns = [
    path('', DanListView.as_view(), name='dan-list'),
    path('create/', DanCreateView.as_view(), name='dan-create'),
    path('search/', SearchView.as_view(), name='search'),
    path('detail/<pk>', DanDetailView.as_view(), name='dan-detail'),
    path('update/<pk>', DanUpdateView.as_view(), name='dan-update'),
    path('delete/<pk>', DanDeleteView.as_view(), name='dan-delete'),

]
