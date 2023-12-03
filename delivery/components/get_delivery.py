from django_unicorn.components import UnicornView, LocationUpdate
from typing import List, Dict
from delivery.models import Items, CartItems
from django.shortcuts import redirect

class GetDeliveryView(UnicornView):
    carts: List = []
    fields:Dict = {'name': "", "price": 0, "unit": 1}
    selected =""
    items = Items.objects.none()
    total_price = 0

    def mount(self):
        self.items = Items.objects.all()
        return super().mount()
    
    def get_total(self):
        price_list = [float(i.get('price')) for i in self.carts]
        print(price_list)
        self.total_price = sum(price_list)

    def updatePrice(self):
        get_item = self.items.filter(name = self.selected).first()
        self.fields['price'] = get_item.price*int(self.fields.get('unit'))
        self.fields['name'] = get_item.name

    def addItem(self):
        self.carts.append(self.fields)
        self.get_total()
        self.selected = ""
        self.fields = {'name': "", "price": 0, "unit": 1}

    def delItem(self, k):
        self.carts.remove(k)
        self.get_total()
        self.selected = ""

    def save_items(self):
        for item_obj in self.carts:
            CartItems.objects.create(**item_obj)
        return LocationUpdate(redirect("/items/checkout/"))