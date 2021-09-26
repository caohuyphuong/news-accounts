"""newspro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from blogs.views import Dashboard, category_create, category_list, category_update, category_delete, category_detail


urlpatterns = [
    path('', Dashboard, name='dashboard'),
    path('admin/', admin.site.urls),
    path('tiemchung/', include('tiemchung.urls', namespace='tiemchung')),

    path('category_create', category_create),
    path('category_list', category_list),
    path('category/<pk>', category_detail),
    path('category_update/<pk>/', category_update),
    path('category_delete/<pk>/', category_delete),
]
