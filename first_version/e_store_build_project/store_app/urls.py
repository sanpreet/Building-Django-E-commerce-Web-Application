from django.urls import path
from store_app import views


urlpatterns = [
    path('', views.catalog, name="catalog"),
    path('cart/', views.cart, name="cart"),
    path('cart/remove/', views.removefromcart, name="remove"),
    path('cart/checkout/', views.checkout, name="checkout"),
    path('cart/checkout/complete/', views.completeorder, name="completeorder"),
    path('admin-login/', views.adminLogin, name="admin_login"),
    path('admin-panel/', views.adminDashboard, name="admin") 
]
