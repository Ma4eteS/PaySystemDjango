from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('config/', views.stripe_config, name='config'),
    path('buy/<int:_id>', views.buy, name='buy'),
    path('item/<int:_id>', views.ItemBuyView.as_view(), name='item'),
    path('success/', views.SuccessView.as_view()),
    path('cancelled/', views.CancelledView.as_view()),
]