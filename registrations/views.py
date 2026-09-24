from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Registration
from .serializers import RegistrationSerializer
from django.shortcuts import get_object_or_404

@api_view(['POST'])
def create_registration(request):
    serializer = RegistrationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['GET'])
def my_registrations(request):
    registrations = Registration.objects.filter(user=request.user)
    serializer = RegistrationSerializer(registrations, many=True)
    return Response(serializer.data)

@api_view(['DELETE'])
def cancel_registration(request, pk):
    registration = get_object_or_404(Registration, pk=pk, user=request.user)
    registration.delete()
    return Response(status=204)