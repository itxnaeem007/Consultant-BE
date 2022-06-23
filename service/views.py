from rest_framework.fields import get_error_detail
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.filters import SearchFilter,OrderingFilter
from rest_framework import generics

from .models import Service
from .serializer import ServiceSerializer

class ServiceListView(generics.ListAPIView):
    queryset = Service.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = ServiceSerializer



class ServiceUpdateView(generics.UpdateAPIView):
    queryset = Service.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = ServiceSerializer


class ServiceDeleteView(generics.DestroyAPIView):
    queryset = Service.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = ServiceSerializer


