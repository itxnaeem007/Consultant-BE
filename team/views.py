from django.db.models import query
from django.shortcuts import render
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework import generics


from .models import Team
from .serializer import TeamSerializer


class TeamListView(generics.ListAPIView):
    queryset = Team.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = TeamSerializer


class TeamUpdateView(generics.UpdateAPIView):
    queryset = Team.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = TeamSerializer


class TeamDeleteView(generics.DestroyAPIView):
    queryset = Team.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = TeamSerializer
