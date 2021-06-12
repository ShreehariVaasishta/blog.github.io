from django.test import TestCase

# Create your tests here.
class GithubActionsTests(TestCase):
    def run_actions(self):
        assert 200 == 200