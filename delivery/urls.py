from django.urls import path
from django.contrib.auth.decorators import login_required
from .components.get_delivery import GetDeliveryView
from .views import HomeView, CheckoutView, CreateItemsView
urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("items/", CreateItemsView.as_view(), name="items"),
    path("items/checkout/", CheckoutView.as_view(), name="checkout"),
]