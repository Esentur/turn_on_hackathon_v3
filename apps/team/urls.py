from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.team.views import TeamView, CommentView

router = DefaultRouter()
router.register('comment', CommentView)
router.register('', TeamView)

urlpatterns = [
    path('', include(router.urls)),
]