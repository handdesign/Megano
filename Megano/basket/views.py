from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import AnonymousUser, User
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Basket, Order
from .serializers import OrderSerializer, BasketSerializer


@api_view(['GET', 'POST', 'DELETE'])
@permission_classes([IsAuthenticated])
def basket(request):
    if request.user.is_authenticated:
        try:
            user_basket = Basket.objects.get(user=request.user)
        except Basket.DoesNotExist:
            user_basket = Basket.objects.create(user=request.user)
    else:
        user_basket = None

    if request.method == 'GET':
        if user_basket:
            serializer = OrderSerializer(user_basket.orders.all(), many=True)
            serializer_data = [item for item in serializer.data]
            serializer_products = []
            for x in serializer_data:
                for j in x['products']:
                    # print(j)
                    # print(j['title'], '\n')
                    serializer_products.append(j)

            return Response(serializer_products)
        else:
            print('6')
            return Response([])

    elif request.method == 'POST':
        serializer = OrderSerializer(data=request.data)

        if serializer.is_valid():
            order = serializer.save()

            try:
                order = Order.objects.get(pk=order.orderId)
            except Order.DoesNotExist:
                return Response({'error': 'Order with given orderId does not exist'}, status=404)

            if not user_basket:
                user_basket = Basket.objects.create(user=request.user)
            user_basket.items.add(order)

            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        if user_basket:
            user_basket.items.clear()
            user_basket.delete()
            return Response({'message': 'Basket cleared successfully'}, status=204)
        else:
            return Response({'message': 'Basket is already empty'}, status=404)

    return Response({'error': 'Invalid request method'}, status=405)


@api_view(['GET', 'POST'])
def order_list(request):
    if request.method == 'GET':
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = OrderSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    return Response({'error': 'Invalid request method'}, status=405)


@api_view(['GET', 'PUT', 'DELETE'])
def order_detail(request, order_id):
    try:
        order = Order.objects.get(pk=order_id)
    except Order.DoesNotExist:
        return Response({'error': 'Order with given orderId does not exist'}, status=404)

    if request.method == 'GET':
        serializer = OrderSerializer(order)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = OrderSerializer(order, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        order.delete()
        return Response({'message': 'Order deleted successfully'}, status=204)

    return Response({'error': 'Invalid request method'}, status=405)


@api_view(['POST'])
def payment(request):
    order_id = request.data.get('order_id')
    payment_status = "success"

    if payment_status == "success":
        order = Order.objects.get(pk=order_id)
        order.status = "Paid successfully"
        order.save()

        return Response({'status': 'success', 'message': 'Payment completed successfully'})
    else:
        return Response({'status': 'failed', 'message': 'Payment failed'})
