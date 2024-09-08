from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RestaurantViewSet, MenuCategoryViewSet, MenuItemViewSet,ModifierViewSet

router = DefaultRouter()
router.register(r'restaurants', RestaurantViewSet)
router.register(r'categories', MenuCategoryViewSet)
router.register(r'menu-items', MenuItemViewSet, basename='menu-item')
router.register(r'modifiers', ModifierViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
