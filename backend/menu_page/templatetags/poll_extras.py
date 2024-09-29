from django import template
from django.core.exceptions import ObjectDoesNotExist

from ..models import SubMenu

register = template.Library()


@register.inclusion_tag('menu.html')
def draw_menu(parent, menu_item=None):

    def get_menu(menu_item=None, submenu=None):
        if menu_item is None:
            menu = list(items.filter(parent=None))
        else:
            menu = list(items.filter(parent__name=menu_item))

        if submenu:
            try:
                index = menu.index(submenu[0].parent) + 1
                menu.insert(index, submenu)
            except (IndexError, TypeError):
                pass

        try:
            parent_name = items.get(name=menu_item).parent.name
            return get_menu(parent_name, menu)
        except AttributeError:
            return get_menu(submenu=menu)
        except ObjectDoesNotExist:
            return menu

    items = SubMenu.objects.filter(menu__name=parent)

    if parent == menu_item:
        return {'menu': get_menu()}
    else:
        return {'menu': get_menu(menu_item)}