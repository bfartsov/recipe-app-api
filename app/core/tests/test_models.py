from django.test import TestCase
from django.contrib.auth import get_user_model
from core import models


def sample_user(email='test@example.com', password='password'):
    return get_user_model().objects.create_user(email=email, password=password)


class ModelTests(TestCase):
    """ Testing models"""
    def test_create_user_with_email_successful(self):
        email = 'test@bvf.com'
        password = 'password'
        user = get_user_model().objects.create_user(email=email,
                                                    password=password)
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        email = 'test@BVF.com'
        user = get_user_model().objects.create_user(email=email,
                                                    password='tsteat')
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_superuser_is_created(self):
        user = get_user_model().objects.create_superuser(
            'test@bvf.bg', 'test123')
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_tag_str(self):
        tag = models.Tag.objects.create(user=sample_user(), name='Vigan')
        self.assertEqual(str(tag), tag.name)
