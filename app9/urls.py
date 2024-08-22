from django.urls import path
from . import views
urlpatterns=[
    path('',views.index,name='index'),
    path('shop/',views.shop,name='shop'),
    path('product/<int:pk>/',views.product_detail,name='product_detail'),
    path('cart/',views.cart,name='cart'),
    path('checkout/',views.checkout,name='checkout'),
    path('contact/',views.contact,name='contact'),
    path('login_page/',views.login_page,name='login_page'),
    path('upload/', views.upload_product, name='upload_product'),
    path('cart/', views.cart, name='cart'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<int:cart_item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('update-cart/<int:cart_item_id>/', views.update_cart, name='update_cart'),



]