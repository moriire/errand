from django.urls import path, include
from user.views import IndexView, AboutView, ContactView, signup_view, activation_sent_view, activate

urlpatterns = [
    path("", include("django.contrib.auth.urls")),
    path('signup/', signup_view, name="signup"),
    path('sent/', activation_sent_view, name="activation_sent"),
    path('activate/<slug:uidb64>/<slug:token>/', activate, name='activate'),
]