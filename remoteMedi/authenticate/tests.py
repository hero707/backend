from django.test import TestCase

class SimpleTest(TestCase):
    def test_pass_always(self):
        self.assertEqual(1+1, 2)