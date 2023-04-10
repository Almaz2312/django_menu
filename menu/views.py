from django.views import generic
from menu.models import Menu


class MenuIndex(generic.ListView):
    model = Menu
    template_name = 'index.html'
    context_object_name = 'menus'


class MenuDetail(generic.DetailView):
    model = Menu
    template_name = 'menu_detail.html'
    context_object_name = 'menu'
