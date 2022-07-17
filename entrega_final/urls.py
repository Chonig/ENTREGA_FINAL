from django.contrib import admin
from django.urls import include, path
from AppCoder.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('AppCoder.urls')),
]
