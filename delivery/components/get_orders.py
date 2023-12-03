from django_unicorn.components import UnicornView
from delivery.models import Items, CartItems
from django.shortcuts import redirect

class GetOrdersView(UnicornView):
    items = Items.objects.none()
    total_price = 0

    def mount(self):
        self.updateItems()
        print(self.total_price)
        return super().mount()

    def updateItems(self):
        self.items = CartItems.objects.all()
        self.get_total()
        
    def get_total(self):
        price_list = [float(i.price) for i in self.items]
        self.total_price = sum(price_list)

    def delItem(self, k):
        self.items.get(id=k).delete()
        self.updateItems()
        self.get_total()
        