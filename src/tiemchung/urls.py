from django.urls import path
from tiemchung.views import (
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
    path('create/', dan_create, name='dan-create'),
    path('detail/<pk>', dan_detail, name='dan-detail'),
    path('update/<pk>', dan_update, name='dan-update'),
    path('update-form/<pk>', dan_update_form, name='dan-update-form'),
    path('update-model-form/<pk>', dan_update_model_form,
         name='dan-update-model-form'),
    path('delete/<pk>', dan_delete, name='dan-delete'),
]
