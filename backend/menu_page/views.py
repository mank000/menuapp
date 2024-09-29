from django.views.generic import ListView

from .models import Menu, SubMenu


class MenuDetailView(ListView):
    model = Menu
    template_name = 'index.html'
    context_object_name = 'menus'


class SubMenuDetailView(ListView):
    model = SubMenu
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        path = self.kwargs.get('path', '').split('/')
        context['menu_name'] = path[0]
        context['menu_item'] = path[-1]
        return context
