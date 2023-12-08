from django.core import mail
from django.test import TestCase
from django.shortcuts import resolve_url as r


class SubscribeEmail(TestCase):
    def setUp(self):
        data = dict(name='Felipe Limeira', cpf='38899999901',
                    email='feh.neo@hotmail.com', phone='85-99999-9999')
        self.client.post(r('subscriptions:new'), data)
        self.email = mail.outbox[0]
    
    
    def test_subscription_email_subject(self):
        expect = 'Confirmação de inscrição'
        
        self.assertEqual(expect, self.email.subject)
        
    def test_subscription_email_from(self):
        expect = 'feh.neo@hotmail.com'
        self.assertEqual(expect, self.email.from_email)
    
    def test_subscription_email_to(self):
        expect = ['feh.neo@hotmail.com', 'feh.neo@hotmail.com']
        self.assertEqual(expect, self.email.to)
        
    def test_subscription_body(self):
        contents = [
            'Felipe Limeira',
            '38899999901',
            'feh.neo@hotmail.com',
            '85-99999-9999',
        ]
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)
