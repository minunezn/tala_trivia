from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RankingViewSet

router = DefaultRouter()
router.register(r'', RankingViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
