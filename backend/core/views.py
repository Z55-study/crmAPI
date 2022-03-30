from django_filters.rest_framework import DjangoFilterBackend

from .models import Person
from rest_framework import generics
from rest_framework import permissions
from .serializers import PersonSerializer


class PersonViewSet(generics.ListAPIView):
    queryset = Person.objects.all().order_by('position')
    serializer_class = PersonSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['position']
