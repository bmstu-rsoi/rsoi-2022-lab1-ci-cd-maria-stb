from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.renderers import JSONRenderer
from rest_framework.settings import api_settings

from .serializers import PersonSerializer
from .models import Person


class PersonAPIViewAll(ListCreateAPIView):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()
    renderer_classes = [JSONRenderer]

    def get_success_headers(self, data):
        try:
            return {'Location': str(data[api_settings.URL_FIELD_NAME])}
        except (TypeError, KeyError):
            return {'Location': f"/{data.get('id', '')}"}


class PersonAPIViewDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()
    renderer_classes = [JSONRenderer]