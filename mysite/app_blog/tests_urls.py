from django.test import TestCase
from django.urls import reverse, resolve
from .views import HomePageView, ArticleDetail, ArticleList, ArticleCategoryList
from .models import Article
from django.utils import timezone
from django.utils.timezone import localtime, now


class HomeTests(TestCase):
    def test_home_view_status_code(self):
        url = reverse("home")
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_home_url_resolves_home_view(self):
        view = resolve("/")
        self.assertEquals(view.func.view_class, HomePageView)


class ArticlesCategoryListTests(TestCase):
    def test_articles_category_view_status_code(self):
        url = reverse("articles-category-list", args=("politica",))
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_articles_category_url_resolves_articles_category_view(self):
        view = resolve("/articles/category/politica")
        self.assertEquals(view.func.view_class, ArticleCategoryList)


class ArticlesTests(TestCase):
    def test_articles_view_status_code(self):
        url = reverse("articles-list")
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_articles_url_resolves_articles_view(self):
        view = resolve("/articles")
        self.assertEquals(view.func.view_class, ArticleList)


class ArticleDetailTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        Article.objects.create(
            title="Політика 3",
            slug="politica-3",
            description="Опис політики 3",
            main_page=True,
        )

    def test_article_detail_view_status_code(self):
        today = localtime(now())
        day = today.day
        month = today.month
        year = today.year

        url = reverse("news-detail", args=(year, month, day, "politica-3"))
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_article_detail_url_resolves_article_detail_view(self):
        today = localtime(now())
        day = today.day
        month = today.month
        year = today.year

        view = resolve("/articles/{}/{}/{}/politica-3".format(year, month, day))
        self.assertEquals(view.func.view_class, ArticleDetail)
