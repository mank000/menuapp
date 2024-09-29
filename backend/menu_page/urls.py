from django.urls import path

from . import views

app_name = 'pages'

urlpatterns = [
    path('',
         views.MenuDetailView.as_view(),
         name='menu'
         ),
    path('<path:path>/',
         views.SubMenuDetailView.as_view(),
         name='submenus')
]
