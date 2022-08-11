from rest_framework import serializers

from apps.team.models import Team, Comment


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'

    captain = serializers.ReadOnlyField(source='captain.username')

    def create(self, validated_data):
        team = Team.objects.create(**validated_data)
        team.save()
        return team

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['comments'] = CommentSerializer(instance.comments.all(), many=True).data
        representation['likes']= instance.likes.filter(like=True).count()

        final_rating =0
        for rating in instance.ratings.all():
            final_rating+=int(rating.rating)
        try:
            representation['rating'] = final_rating / instance.ratings.all().count()
            return representation
        except ZeroDivisionError:
            return representation




class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Comment
        fields = '__all__'


class RatingSerializer(serializers.Serializer):
    rating = serializers.IntegerField(required=True, min_value=1, max_value=5)
