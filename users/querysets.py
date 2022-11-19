from django.db.models import QuerySet


class PersonQuerySet(QuerySet):
    def list(self):
        query = self.all()
        return query