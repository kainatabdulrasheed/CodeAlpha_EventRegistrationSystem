from rest_framework import serializers
from .models import Registration
from events.models import Event
from events.serializers import EventSerializer


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = '__all__'
        read_only_fields = ['user']

    def to_representation(self, instance): 
        data = super().to_representation(instance)
        data['event'] = EventSerializer(instance.event).data
        return data