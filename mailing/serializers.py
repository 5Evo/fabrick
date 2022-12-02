from rest_framework import serializers

from mailing.models import Tag, Status, MobileCode, Mailing, Client, Message


class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class StatusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'


class MobileCodeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MobileCode
        fields = '__all__'


class MailingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Mailing
        fields = '__all__'


class ClientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class MessageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'
