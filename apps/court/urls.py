from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.court.views import CourtView

router = DefaultRouter()
router.register('book', CourtView)

urlpatterns = [
    path('', include(router.urls)),
]