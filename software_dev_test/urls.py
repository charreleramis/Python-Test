"""software_dev_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from App import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('create_data', views.create_values_or_principle, name='create_data'),
    path('read_data/<slug:context_type>/<int:id>',   views.read_values_principle, name='read_data'),
    path('read_all_data', views.read_all_values_principle, name='read_all_data'),
    path('update_data', views.update_values_principle, name='update_data'),
    path('delete_data', views.delete_values_principle, name='delete_data'),
    path('clear_all', views.clearAll, name='clear_all'), # done
    path('fill_database', views.store_all_values_principle, name='fill_database'),

]
