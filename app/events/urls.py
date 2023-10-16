from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EventViewSet, CommentViewSet

router = DefaultRouter()

router.register(r'', EventViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]