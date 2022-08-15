from rest_framework import serializers

from apps.court.models import Court


class CourtSerializer(serializers.ModelSerializer):
    customer = serializers.ReadOnlyField(source='customer.username')

    class Meta:
        model = Court
        fields = '__all__'

    def create(self, validated_data):
        booked_court = Court.objects.create(**validated_data)
        booked_court.save()
        return booked_court