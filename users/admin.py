from django.contrib import admin
from users.models import Person

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
        pass