from django.test import TestCase
from django.urls import reverse, resolve
from frontend.views import IndexView


class TestApiUrls(TestCase):
    def setUp(self):
        return

    def test_index_url_is_resolved(self):
        resolver = resolve(reverse("frontend:index"))
        self.assertEqual(resolver.func.view_class, IndexView)

    def test_accommodation_url_is_resolved(self):
        resolver = resolve(reverse("frontend:accommodation"))
        self.assertEqual(resolver.func.view_class, IndexView)

    def test_location_url_is_resolved(self):
        resolver = resolve(reverse("frontend:location"))
        self.assertEqual(resolver.func.view_class, IndexView)

    def test_features_url_is_resolved(self):
        resolver = resolve(reverse("frontend:features"))
        self.assertEqual(resolver.func.view_class, IndexView)

    def test_feature_children_urls_are_resolved(self):
        features = ["ocean", "boating", "hiking"]
        for feature in features:
            resolver = resolve(reverse("frontend:feature", args=[feature]))
            self.assertEqual(resolver.func.view_class, IndexView)

    def test_book_url_is_resolved(self):
        resolver = resolve(reverse("frontend:book"))
        self.assertEqual(resolver.func.view_class, IndexView)

    def test_contact_url_is_resolved(self):
        resolver = resolve(reverse("frontend:contact"))
        self.assertEqual(resolver.func.view_class, IndexView)

    def test_about_url_is_resolved(self):
        resolver = resolve(reverse("frontend:about"))
        self.assertEqual(resolver.func.view_class, IndexView)

    def test_terms_url_is_resolved(self):
        resolver = resolve(reverse("frontend:terms"))
        self.assertEqual(resolver.func.view_class, IndexView)

    def test_privacy_url_is_resolved(self):
        resolver = resolve(reverse("frontend:privacy"))
        self.assertEqual(resolver.func.view_class, IndexView)

    def test_faq_url_is_resolved(self):
        resolver = resolve(reverse("frontend:faq"))
        self.assertEqual(resolver.func.view_class, IndexView)

    def tearDown(self):
        return
