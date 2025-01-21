from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient


# paymentTest class
class PaymentTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_initiate_payment(self):
        data = {
            'customer_name': 'John Doe',
            'customer_email': 'john@example.com',
            'amount': 5000.00
        }
        response = self.client.post(reverse('payment-initiate'), data, format='json')
        print(response.content)  # print the error details if there's any
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('reference', response.data)

    def test_payment_status(self):

        # First, initiate a payment to ensure there is a valid reference
        data = {
            'customer_name': 'John Doe',
            'customer_email': 'john@example.com',
            'amount': 5000.00
        }
        initiate_response = self.client.post(reverse('payment-initiate'), data, format='json')
        self.assertEqual(initiate_response.status_code, status.HTTP_201_CREATED)
        
        reference = initiate_response.data['reference']  # Extract the reference from the response
        
        # Now, check the payment status using the valid reference
        response = self.client.get(reverse('payment-status', kwargs={'reference': reference}))
        print(response.content)  # Add this line to see the error details
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['status'], 'success')
