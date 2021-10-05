from django.urls import path
from tiemchung.views import (
    DanCreateView,
    DanDeleteView,
    DanDetailView,
    DanUpdateView,
    DanDeleteView,
    dan_create,
    dan_delete,
    dan_detail,
    dan_list,
    dan_update,
    dan_update_form,
    dan_update_model_form,
    DanListView
)

app_name = 'tiemchung'

urlpatterns = [
    path('', DanListView.as_view(), name='dan-list'),
    path('create/', DanCreateView.as_view(), name='dan-create'),
    path('detail/<pk>', DanDetailView.as_view(), name='dan-detail'),
    path('update/<pk>', DanUpdateView.as_view(), name='dan-update'),
    path('update-form/<pk>', dan_update_form, name='dan-update-form'),
    path('update-model-form/<pk>', dan_update_model_form,
         name='dan-update-model-form'),
    path('delete/<pk>', DanDeleteView.as_view(), name='dan-delete'),
]
