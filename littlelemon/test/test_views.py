from django.test import TestCase
from django.urls import reverse
from restaurant.models import Menu

# Create your tests here.
class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(title="Pizza", price=20, inventory=10)
        Menu.objects.create(title="Lemon Cake", price=9.55, inventory=50)

    def test_getall(self):
        response = self.client.get(reverse("menuItems"))
        self.assertEqual(response.status_code, 200)