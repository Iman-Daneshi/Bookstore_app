from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve
from .views import HomePageview


class HomePageTest(SimpleTestCase):

    def setUp(self):
        url = reverse('pages:home')
        self.response = self.client.get(url)

    def test_homepage_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_template(self):
        self.assertTemplateUsed(self.response, 'home.html')

    def test_hompage_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, 'Hi there, I should not be on the page.')

    def test_hompage_contain_incorrect_html(self):
        self.assertContains(self.response, 'Homepage')

    def test_homepage_url_resolve_hompaheview(self):
        view = resolve('/')
        self.assertEqual(view.func.__name__, HomePageview.as_view().__name__)