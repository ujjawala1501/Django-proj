"""
URL configuration for Hello project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path ,include

admin.site.site_header = "Ujjawala Ice cream Admin"
admin.site.site_title = "Welcome to Admin Portal"
admin.site.index_title = "Welcome to icecream Researcher Portal"

urlpatterns = [
    path('admin/', admin.site.urls), #Whenever there is a /admin in front of server port send them to django admin
    path('',include('Home.urls'))
]

#Testing where it goes
#test2