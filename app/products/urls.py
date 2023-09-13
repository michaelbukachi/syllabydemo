from django.urls import path

from .views import ProductsList, ProductDetails, AddProductImage

urlpatterns = [
    path('', ProductsList.as_view()),
    path('<int:pk>/', ProductDetails.as_view()),
    path('<int:pk>/images/', AddProductImage.as_view())
]

