from django import http
from django.shortcuts import redirect
from django_unicorn.components import UnicornView
from typing import Any, List, Dict
from django.views.generic.base import View, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

class HomeView(
    #LoginRequiredMixin, 
    TemplateView):
    template_name="delivery/index.html"
    #login_url = "/auth/login/"
    #redirect_field_name = 'next'
    #raise_exception = False
 
class CreateItemsView(LoginRequiredMixin, TemplateView):
    template_name="delivery/items.html"

class CheckoutView(LoginRequiredMixin, TemplateView):
    template_name="delivery/checkout.html"

