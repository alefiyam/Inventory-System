from django.conf.urls import url

from inventory import views

urlpatterns = [
    url(r'^items/$', views.ItemList.as_view(), name='item-list'),
    url(r'^$', views.ItemListView.as_view(), name='items'),
    url(r'^item-create/$', views.ItemCreateView.as_view(), name='item-create'),
    url(r'^item/(?P<pk>\d+)/update/$', views.ItemUpdateView.as_view(), name='item-update'),
    url(r'^item/(?P<pk>\d+)/$', views.ItemDetailView.as_view(), name='item-detail'),
    url(r'^item-delete/(?P<pk>\d+)/$', views.ItemConfirmDeleteView.as_view(), name='item-delete'),
]
