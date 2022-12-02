from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from mailing.models import Status, Tag, MobileCode, Mailing, Client, Message
from mailing.serializers import StatusSerializer, TagSerializer, MobileCodeSerializer, MailingSerializer, \
    ClientSerializer, MessageSerializer


# Create your views here.

class StatusViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]   # IsAdminUser - права администратора Django
    queryset = Status.objects.all()
    serializer_class = StatusSerializer


class TagViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]   # IsAdminUser - права администратора Django
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class MobileCodeViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]   # IsAdminUser - права администратора Django
    queryset = MobileCode.objects.all()
    serializer_class = MobileCodeSerializer


class MailingViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]   # IsAdminUser - права администратора Django
    queryset = Mailing.objects.all()
    serializer_class = MailingSerializer


class ClientViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]   # IsAdminUser - права администратора Django
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class MessageViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]   # IsAdminUser - права администратора Django
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

