from django.urls import path
from tiemchung.views import dan_create, dan_delete, dan_detail, dan_list, dan_update

app_name = 'tiemchung'

urlpatterns = [
    path('', dan_list, name='dan-list'),
    path('create/', dan_create, name='dan-create'),
    path('detail/<pk>', dan_detail, name='dan-detail'),
    path('update/<pk>', dan_update, name='dan-update'),
    path('delete/<pk>', dan_delete, name='dan-delete'),
]
