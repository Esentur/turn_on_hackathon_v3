from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from requests import Response
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from apps.team.models import Team, Favourite, Like, Rating, Comment
from apps.team.serializers import TeamSerializer, RatingSerializer, CommentSerializer


class LargeResultsSetPagination(PageNumberPagination):
    page_size = 4
    page_query_param = 'page_size'
    max_page_size = 1000

class TeamView(ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    pagination_class = LargeResultsSetPagination
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_fields = ['name', 'slogan', 'captain']
    search_fields = ['name', 'slogan']
    ordering_fields = ['name', 'id']

    def perform_create(self, serializer):
        serializer.save(captain=self.request.user)

    @action(methods=['POST'], detail=True)
    def favorite(self, request, pk, *args, **kwargs):
        try:
            fav_obj, _ = Favourite.objects.get_or_create(author=request.user, team_id=pk)
            fav_obj.favourite = not fav_obj.favourite
            fav_obj.save()
        except:
            return ('The team does not exits!')
        if fav_obj.favourite:
            return Response('Added to Favourites')
        return Response('Removed from Favourites')

    @action(methods=['POST'], detail=True)
    def like(self, request, pk, *args, **kwargs):
        try:
            like_obj, _ = Like.objects.get_or_create(author=request.user, team_id=pk)
            like_obj.like = not like_obj.like
            like_obj.save()
        except:
            return ('The team does not exist!')

        if like_obj.like:
            return Response('LIKED')
        return Response('UNLIKED')

    @action(methods=['POST'], detail=True)
    def rating(self, request, pk, *args, **kwargs):
        serializer = RatingSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        obj, _ = Rating.objects.get_or_create(seller=request.user, team_id=pk)
        obj.rating = request.data['rating']
        obj.save()
        return Response(request.data)

    def get_permissions(self):
        # print(self.action)
        if self.action in ['list', 'retrieve']:
            permissions = []
        elif self.action == 'like' or self.action == 'rating':
            permissions = [IsAuthenticated]
        else:
            permissions = [IsAuthenticated]
        return [p() for p in permissions]


class CommentView(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

