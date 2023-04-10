from django.urls import path

from menu.views import MenuIndex, MenuDetail


urlpatterns = [
    path('menu/', MenuIndex.as_view(), name='menu_index'),
    path('menu/<int:pk>', MenuDetail.as_view(), name='menu_detail')
]