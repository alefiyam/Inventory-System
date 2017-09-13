
from rest_framework import serializers
# from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.core.mail import EmailMultiAlternatives
from inventory.models import Item

class ItemSerializer(serializers.ModelSerializer):

    """ Itemlist serializer
        show itemlist
    """
    class Meta:
        model = Item
        fields = ('id','name', 'is_active', 'vendor', 'catalog', 'size', 'category')
