from django.contrib import admin
from django.urls import path

from redirect.views import DoRedirect, HomePageView, LinkSuccessView

urlpatterns = [
    path('admin', admin.site.urls),
    path('<slug:slug>', DoRedirect.as_view(), name='redirect'),
    path('', HomePageView.as_view(), name='home'),
    path('success/<slug:slug>', LinkSuccessView.as_view(), name='show-link'),
]
