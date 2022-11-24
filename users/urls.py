from django.urls import path

from .views import PersonAPIViewAll, PersonAPIViewDetail

urlpatterns = [
    path("persons", PersonAPIViewAll.as_view()),
    path("persons/<int:pk>", PersonAPIViewDetail.as_view())
]
