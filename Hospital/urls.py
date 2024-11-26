"""
URL configuration for Hospital project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from cardio.views import *
from ent.views import *
from neuro.views import *
from pulmonary.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Cardio/', Cardio, name='Cardio'),
    path('ent/', ent, name='ent'),
    path('Neuro/', Neuro, name='Neuro'),
    path('Pulmonary/', Pulmonary, name='Pulmonary')
]
