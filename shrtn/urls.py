from django.contrib import admin
from django.urls import path

from redirect.views import DoRedirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('<slug:slug>', DoRedirect.as_view(), name='redirect'),
]
