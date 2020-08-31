from django.test import TestCase
from django.test import Client
from cv.models import Field


class Tests(TestCase):

    def setUp(self):
        Field.objects.create(name="Palantir", start_date="2020-01-01", end_date="2020-02-02", sub ="tester1", category="Unit testing")
        Field.objects.create(name="Google", start_date="2020-03-03", end_date="2020-04-04", sub="tester2", category="Unit testing")

    def test_object_creation(self):
        o1 = Field.objects.get(name="Palantir")
        o2 = Field.objects.get(name="Google")
        self.assertEqual(o1.sub, 'tester1')
        self.assertEqual(o2.sub, 'tester2')

    def test_template(self):
        self.assertTemplateUsed(Client().get('/cv/'), 'base.html')
        self.assertTemplateUsed(Client().get('/cv/'), 'cv.html')

    def test_header(self):
        self.assertIn("Curriculum Vitae", Client().get('/').content.decode())
        self.assertIn("Blog", Client().get('/').content.decode())
        self.assertIn("Edoardo Bassett", Client().get('/').content.decode())

    def test_cv(self):
        self.assertIn("Course of Life", Client().get('/cv/').content.decode())
        self.assertIn("Fakebusters", Client().get('/cv/').content.decode())

    def test_home(self):
        self.assertIn("Hello.", Client().get('/').content.decode())
        self.assertIn("Welcome to my portfolio.", Client().get('/').content.decode())

    def test_blog(self):
        self.assertIn("What is Django", Client().get('/blog/').content.decode())
        self.assertIn("Test Driven Development", Client().get('/blog/').content.decode())




