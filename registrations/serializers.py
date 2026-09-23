from rest_framework import serializers
from .models import Registration
from events.models import Event
from events.serializers import EventSerializer


class RegistrationSerializer(serializers.ModelSerializer):
    event = EventSerializer(read_only=True)

    class Meta:
        model = Registration
        fields = '__all__'
