from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response 
from .models import Movie
from .serializers import WatchListSerializer


class MovieList(APIView):

	def get(self, response):
		movies = Movie.objects.all()
		serializer = WatchListSerializer(movies, many=True)
		return Response(serializer.data)