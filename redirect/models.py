from random import choice
from string import ascii_letters, digits

from django.db import models
from django.shortcuts import reverse

SLUG_LENGTH = 6


def generate_slug(length=SLUG_LENGTH):
    return ''.join(choice(ascii_letters + digits) for _ in range(length))


class Redirect(models.Model):
    target = models.URLField(max_length=750)
    slug = models.SlugField(null=False, unique=True)

    def __str__(self) -> str:
        return f'Redirect to {self.target}'

    def save(self, *args, **kwargs):
        if not self.slug:
            # Generate unique slug
            valid = False
            while not valid:
                slug_string = generate_slug()
                if Redirect.objects.filter(slug=slug_string).count() == 0:
                    valid = True
            self.slug = slug_string
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('redirect', kwargs={'slug': self.slug})
