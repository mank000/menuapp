
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('menu/', include('menu_page.urls', namespace='menu'))
]
