"""first URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url
from django.contrib import admin
# from first.views import inicio
# from first.views import autor
from first.views import *

# url(r'^inicio$', inicio)
# la r es para usar caracteres especiales
# el ^ es para indicar que la URL debe comnezar con "inicio"
# el $ es para indicar que la URL termina en "inicio"
urlpatterns = [
    url('^$', autor),
    url(r'^admin/', admin.site.urls),
    url(r'^inicio$', inicio),
]
