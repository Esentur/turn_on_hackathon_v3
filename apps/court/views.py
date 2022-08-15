from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from apps.court.models import Court
from apps.court.serializers import CourtSerializer


class CourtView(ModelViewSet):
    queryset = Court.objects.all()
    serializer_class = CourtSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_fields = ['customer', 'court_num', ]
    search_fields = ['customer', ]
    ordering_fields = ['schedule', 'court_num']

    def perform_create(self, serializer):
        serializer.save(customer=self.request.user)
