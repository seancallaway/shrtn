from django.shortcuts import reverse
from django.test import TestCase

from redirect.models import Redirect, SLUG_LENGTH


class RedirectModelTests(TestCase):

    def setUp(self) -> None:
        self.redirect = Redirect.objects.create(
            target='https://mail.google.com/'
        )

    def test_redirect_creation(self) -> None:
        # Ensure slug was created and is of proper length
        self.assertEqual(len(self.redirect.slug), SLUG_LENGTH)

    def test_absolute_url(self) -> None:
        self.assertEqual(self.redirect.get_absolute_url(), reverse('redirect', kwargs={'slug': self.redirect.slug}))

    def test_str_repr(self) -> None:
        self.assertEqual(f'Redirect to {self.redirect.target}', str(self.redirect))
