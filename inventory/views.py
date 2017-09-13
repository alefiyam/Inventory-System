from django.http import HttpResponseRedirect
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView
from inventory.models import Item
from django.urls import reverse_lazy
from serializers import (
    ItemSerializer)
from rest_framework import generics
import urllib
import requests

class ItemListView(generic.ListView):
    template_name = 'inventory/item.html'
    context_object_name = 'item_list'

    def get_queryset(self):
        if 'all_user' in self.request.GET:
            urlencode = urllib.urlencode(self.request.GET)
            item_list = requests.get('http://localhost:8000/items/?'+urlencode).json()
            item_ids = []
            for item in item_list:
                item_ids.append(item['id'])

            return Item.objects.filter(id__in=item_ids)
        return Item.objects.filter(is_active=True).order_by('-date_added')

    def get_context_data(self, **kwargs):
        context = super(ItemListView, self).get_context_data(**kwargs)
        if self.request.GET.get('all_user', None):
            context['all_user'] = True
            context['active_user'] = False
        if self.request.GET.get('active_user', None):
            context['active_user'] = True
            context['all_user'] = False

        return context

class ItemCreateView(CreateView):
    model = Item
    fields = ['name', 'vendor', 'catalog', 'size', 'category']
    success_url = reverse_lazy('inventory:items')


class ItemUpdateView(UpdateView):
    model = Item
    fields = ['name', 'vendor', 'catalog', 'size', 'category']
    success_url = reverse_lazy('inventory:items')
    template_name_suffix = '_update_form'


class ItemDetailView(generic.DetailView):
    model = Item

    def get_context_data(self, **kwargs):
        context = super(ItemDetailView, self).get_context_data(**kwargs)
        context['lineitems'] = context['item']
        return context


class ItemConfirmDeleteView(generic.DeleteView):
    template_name = 'inventory/confirm_delete_items.html'
    model = Item
    success_url = reverse_lazy('inventory:items')
    items_to_delete = []

    def get_context_data(self, **kwargs):
        context = super(ItemConfirmDeleteView, self).get_context_data(**kwargs)
        return context

    def post(self, request, *args, **kwargs):

        # self.items_to_delete = self.request.POST.getlist('itemsToDelete')
        if self.request.POST.get("confirm_delete"):
            # when confirmation page has been displayed and confirm button
            # pressed
            item_to_delete = self.get_queryset().get(id=self.kwargs['pk'])
            item_to_delete.is_active = False
            item_to_delete.save()
            return HttpResponseRedirect(self.success_url)
        elif self.request.POST.get("cancel"):
            # when confirmation page has been displayed and cancel button
            # pressed
            return HttpResponseRedirect(self.success_url)
        else:
            # when data is coming from the form which lists all items
            return self.get(self, *args, **kwargs)

class ItemList(generics.ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def get_queryset(self):
        if 'all_user' in self.request.GET:
            return self.queryset.all()
        else:
            return self.queryset.filter(is_active=True)

