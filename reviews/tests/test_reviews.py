from django.core.exceptions import ValidationError
from django.test import TestCase

from categories.models import Category
from reviews.models import Review
from establishments.models import Place
from django.contrib.auth import get_user_model
from django.utils import timezone

class ReviewModelTestCase(TestCase):
    def setUp(self):
        self.category = Category.objects.create(
            name='test'
        )
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='password'
        )
        self.place = Place.objects.create(
            name='Test Place',
            description='Test Place description',
            latitude=55.1234,
            longitude=37.4321,
            category=self.category
        )

    def test_review_creation(self):
        review = Review.objects.create(
            user=self.user,
            place=self.place,
            comment='Test review',
            rating=4,
        )
        self.assertIsInstance(review, Review)
        self.assertEqual(review.user, self.user)
        self.assertEqual(review.place, self.place)
        self.assertEqual(review.comment, 'Test review')
        self.assertEqual(review.rating, 4)

    def test_review_rating_validation(self):
        invalid_review = Review(user=self.user, place=self.place, comment='Invalid review', rating=11)
        with self.assertRaises(ValidationError):
            invalid_review.full_clean()

    def test_review_text_required(self):
        review = Review(user=self.user, place=self.place, rating=4)
        with self.assertRaises(Exception):
            review.full_clean()

    def test_review_user_deletion_cascade(self):
        self.user.delete()
        self.assertEqual(Review.objects.filter(user=self.user).count(), 0)

    def test_review_place_deletion_cascade(self):
        self.place.delete()
        self.assertEqual(Review.objects.filter(place=self.place).count(), 0)
