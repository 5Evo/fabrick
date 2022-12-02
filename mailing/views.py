from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from mailing.models import Status
from mailing.serializers import StatusSerializer


# Create your views here.


class StatusViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]   # IsAdminUser - права администратора Django
    queryset = Status.objects.all()
    serializer_class = StatusSerializer

