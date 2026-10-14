from django.test import TestCase
from django.urls import reverse


class IndexAccessTests(TestCase):
    def test_dashboard_requires_shop_login(self):
        response = self.client.get(reverse("root_path"))
        self.assertEqual(response.status_code, 302)
        self.assertIn("login", response["Location"])

    def test_login_page_renders(self):
        response = self.client.get(reverse("shopify_app_login"))
        self.assertEqual(response.status_code, 200)
