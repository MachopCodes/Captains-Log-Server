from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
import os
from dotenv import load_dotenv, find_dotenv, dotenv_values
load_dotenv(find_dotenv())

API_KEY = os.getenv('API_KEY')

class Key(generics.RetrieveUpdateDestroyAPIView):
    def get(self, request):
        """Get Request"""
        return Response(API_KEY)
