from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Curso, Avaliacao
from .serializers import CursoSerializer, AvaliacaoSerializer
from rest_framework import status


class CursoAPIView(APIView):
    """
    API Senai
    """

    def get(self, request):
        curso = Curso.objects.all()
        serializer = CursoSerializer(curso, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CursoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'id': serializer.data['id']})

class AvaliacaoAPIView(APIView):
    """
    API Senai
    """

    def get(self, request):
        av = Avaliacao.objects.all()
        serializer = AvaliacaoSerializer(av)
        return Response(serializer.data)
