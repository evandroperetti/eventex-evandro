# coding: utf-8
from django.test import TestCase
from django.db import IntegrityError
from datetime import datetime
from eventex.subscriptions.models import Subscription

class SubscriptionTest(TestCase):
    def setUp(self):
        self.obj = Subscription(
            name='Evandro Peretti',
            cpf='12345678901',
            email='evandroperetti@gmail.com',
            phone='54-99173705'
        )
    def test_create(self):
        'Subscription must have name, cpf, email, phone'
        self.obj.save()
        self.assertEqual(1, self.obj.id)
        
    def test_has_created_at(self):
        'Subscription must have automatic created_at'
        self.obj.save()
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_unicode(self):
        self.assertEqual(u'Evandro Peretti', unicode(self.obj))
        
class SubscriptionUniqueTest(TestCase):
    def setUp(self):
        #Create a first entry to force the colision
        Subscription.objects.create(name='Evandro Peretti', cpf='12345678901',
                                    email='evandroperetti@gmail.com', phone='54-99173705')
    
    def test_cpf_unique(self):
        'CPF must be unique'
        s = Subscription(name='Evandro Peretti', cpf='12345678901',
                        email='evandroperetti@gmail.com', phone='54-99173705')
        self.assertRaises(IntegrityError, s.save)
        
    def test_email_unique(self):
        'Email must be unique'
        s = Subscription(name='Evandro Peretti', cpf='12345678901',
                        email='evandroperetti@gmail.com', phone='54-99173705')
        self.assertRaises(IntegrityError, s.save)