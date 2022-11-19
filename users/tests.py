# from django.urls import reverse
# from rest_framework import status
# from rest_framework.test import APITestCase
# from .models import Person
#
# class PersonTests(APITestCase):
#     def setUp(self):
#         self.data = {
#             "name": "nikita",
#             "age": 13,
#             "address": "govt",
#             "work": "test"
#         }
#         self.response = self.client.post(
#             reverse('users:person-list'),
#             self.data,
#             format="json")
#
#
#     def test_api_create_person(self):
#         self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
#         self.assertEqual(Person.objects.count(), 1)
#         self.assertEqual(Person.objects.get().name, 'nikita')
#
#     def test_api_list_persons(self):
#         url = reverse('users:person-list')
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(Person.objects.count(), 1)
#
#     # def test_api_detail_person(self):
#     #     person = Person.objects.get()
#     #     response = self.client.get(
#     #         reverse('users:person-detail',
#     #         kwargs={'id': person.id}), format="json"
#     #     )
#     #     self.assertEqual(response.status_code, status.HTTP_200_OK)
#     #     self.assertContains(response.get('id'), Person.objects.get().id)
#
#     def test_api_update_person(self):
#         person = Person.objects.get()
#         new_data = {
#             "name": "maria",
#             "work": "sber"
#         }
#         response = self.client.patch(
#             reverse('users:person-detail',
#             kwargs={'id': person.id}), data=new_data, format="json"
#         )
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(Person.objects.get().name, 'maria')
#
#     def test_api_delete_person(self):
#         person = Person.objects.get()
#         response = self.client.delete(
#             reverse('users:person-detail',
#             kwargs={'id': person.id}), format="json"
#         )
#         self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
#         self.assertEqual(Person.objects.count(), 0)