from django.test import TestCase
from django.utils import reverse

from catalog.models import Author

class AuthorListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        number_of_authors = 13

        for author_id in range(number_of_authors):
            Author.objects.create(first_name=f'Dominique {author_id}', last_name=f'Surname { author_id}',)
