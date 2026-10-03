from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("cart/", views.cart_view, name="cart"),
    path("cart/add/<int:pk>/", views.cart_add, name="cart_add"),
    path("cart/<int:pk>/<str:action>/", views.cart_change, name="cart_change"),
    path("order/", views.place_order, name="place_order"),
    path("order/success/", views.order_success, name="order_success"),
]
