from django.test import TestCase
from .models import Article, Category


class CategoryModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test
        Category.objects.create(category="Innovations", slug="innovations")

    def test_get_absolute_url(self):
        category = Category.objects.get(id=1)
        self.assertEquals(category.get_absolute_url(), "/articles/category/innovations")


class ArticleModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Article.objects.create(
            title="Політика 3",
            slug="politica-3",
            description="Опис політики 3",
            main_page=True,
        )

    def test_get_absolute_url(self):
        article = Article.objects.get(id=1)
        self.assertEquals(article.get_absolute_url(), "/articles/2022/04/29/politica-3")
