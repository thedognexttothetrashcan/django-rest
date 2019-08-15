from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from ViewLearn.models import Computer
from ViewLearn.serializers import ComputerSerializer
from rest_framework import generics


class ComputersView(APIView):

    def get(self, request, format=None):

        computers = Computer.objects.all()

        serializer = ComputerSerializer(computers, many=True)

        return Response(serializer.data)


class ComputersAPIView(generics.ListAPIView):

    queryset = Computer.objects.all()

    serializer_class = ComputerSerializer


class ComputerAPIView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Computer.objects.all()

    serializer_class = ComputerSerializer

