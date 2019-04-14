from rest_framework import serializers
from .models import Movie


class WatchListSerializer(serializers.ModelSerializer):

	class Meta:
		model = Movie
		fields = ('title', 'year', 'genre', 'ratings')