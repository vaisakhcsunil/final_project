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


]