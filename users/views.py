from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from users.models import Person
from users.serializers import PersonSerializer


class PersonView(ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    permission_classes = [AllowAny]
    lookup_field = 'id'

    # def update(self, request, id, format=None):
    #     print(request)
    #     print("id",id)
    #     return {}
