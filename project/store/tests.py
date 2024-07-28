from django.test import TestCase, Client
from django.urls import reverse
from .models import Product, Customer, Order, OrderItem, ShippingAddress
from django.contrib.auth.models import User
import json

class ViewTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.customer = Customer.objects.create(user=self.user, name='Test Customer', email='test@example.com')
        self.product = Product.objects.create(name='Test Product', price=10.0, digital=False)
        self.order = Order.objects.create(customer=self.customer, complete=False)
        self.order_item = OrderItem.objects.create(order=self.order, product=self.product, quantity=1)

    def test_index_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'store/index.html')

    def test_store_view(self):
        response = self.client.get(reverse('store'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'store/store.html')
        self.assertIn('products', response.context)
        self.assertIn('cartItems', response.context)

    def test_cart_view(self):
        response = self.client.get(reverse('cart'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'store/cart.html')
        self.assertIn('items', response.context)
        self.assertIn('order', response.context)
        self.assertIn('cartItems', response.context)

    def test_checkout_view(self):
        response = self.client.get(reverse('checkout'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'store/checkout.html')
        self.assertIn('items', response.context)
        self.assertIn('order', response.context)
        self.assertIn('cartItems', response.context)

    def test_update_item_view_authenticated(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.post(reverse('update_item'), json.dumps({'productId': self.product.id, 'action': 'add'}),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), 'Item was added')

    def test_update_item_view_unauthenticated(self):
        response = self.client.post(reverse('update_item'), json.dumps({'productId': self.product.id, 'action': 'add'}),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json(), {'error': 'User not authenticated'})

    def test_process_order_view_authenticated(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.post(reverse('process_order'), json.dumps({
            'form': {'total': str(self.order.get_cart_total)},
            'shipping': {
                'address': '123 Test St',
                'city': 'Test City',
                'state': 'Test State',
                'zipcode': '12345'
            }
        }), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), 'Payment submitted..')

    def test_process_order_view_unauthenticated(self):
        response = self.client.post(reverse('process_order'), json.dumps({
            'form': {'total': str(self.order.get_cart_total), 'name': 'Guest', 'email': 'guest@example.com'},
            'shipping': {
                'address': '123 Test St',
                'city': 'Test City',
                'state': 'Test State',
                'zipcode': '12345'
            }
        }), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), 'Payment submitted..')
