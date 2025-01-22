from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Payment
from .serializers import PaymentSerializer
from paystackapi.paystack import Paystack
from paystackapi.transaction import Transaction
from django.conf import settings
import uuid

paystack = Paystack(secret_key=settings.PAYSTACK_SECRET_KEY)


class PaymentInitiateView(APIView):
    def post(self, request):
        serializer = PaymentSerializer(data=request.data)
        if serializer.is_valid():
            # Create a unique payment reference
            reference = str(uuid.uuid4())  # Generate a unique reference
            # Validate and convert the amount
            try:
                amount = float(serializer.validated_data['amount'])  # Ensure amount is a float
                amount_in_kobo = int(amount * 100)  # Convert to kobo (integer)
            except (ValueError, TypeError) as e:
                return Response({'amount': f'Invalid amount format: {str(e)}'}, status=status.HTTP_400_BAD_REQUEST)
            
            # Save the payment with the reference
            payment = serializer.save(reference=reference)
            # Integrate Paystack payment initialization here
            response = Transaction.initialize(
                reference=reference,
                email=serializer.data['customer_email'],
                amount=amount_in_kobo  # amount in kobo
            )
            return Response({
                'reference': reference,
                'data': response
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PaymentStatusView(APIView):
    def get(self, request, reference):
        try:
            payment = Payment.objects.get(reference=reference)
            # Integrate Paystack transaction verification here
            response = Transaction.verify(reference=reference)
            payment.status = response['data']['status']
            payment.save()
            return Response({'payment': PaymentSerializer(payment).data, 'status': 'success', 'message': 'Payment details retrieved successfully.'})
        except Payment.DoesNotExist:
            return Response({'status': 'error', 'message': 'Payment not found.'}, status=status.HTTP_404_NOT_FOUND)
