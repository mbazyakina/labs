from django.contrib import admin
from django.urls import path
from flatpages.views import home, static_page

urlpatterns = [
    path('', home, name='home'),
    path('hello/', home, name='hello'),
    path('static-page/', static_page, name='static_page'),
    path('admin/', admin.site.urls),
]