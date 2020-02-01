from django.urls import path
from django.conf.urls import include
from product import views

urlpatterns = [
	path('products/', views.ProductViewSet.as_view()),
]