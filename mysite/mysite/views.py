from .models import Car, Customer, Employee
from rest_framework.response import Response
from .serializers import CarSerializer
from .customer import CustomerSerializer
from .employee import EmployeeSerializer
from rest_framework import status
from rest_framework.decorators import api_view



@api_view(['GET'])
def get_cars(request, car_pk):
    try:
        car = Car.objects.get(pk=car_pk)
    except Car.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CarSerializer(car)
        return Response(serializer.data)


@api_view(['GET'])
def get_customer(request, customer_pk):
    try:
        customer = Customer.objects.get(pk=customer_pk)
    except Customer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)


@api_view(['GET'])
def get_employee(request, employee_pk):
    try:
        employee = Employee.objects.get(pk=employee_pk)
    except Employee.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)


@api_view(['POST'])
def save_car(request):
    if request.method == 'POST':
        serializer = CarSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def save_customer(request):
    if request.method == 'POST':
        serializer = CustomerSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def save_employee(request):
    if request.method == 'POST':
        serializer = EmployeeSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def update_car(request, id):
    try:
        theCar = Car.objects.get(pk=id)
    except Car.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'PUT':
        serializer = CarSerializer(theCar, data=request.data)
    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def update_customer(request, id):
    try:
        theCustomer = Customer.objects.get(pk=id)
    except Customer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'PUT':
        serializer = CustomerSerializer(theCustomer, data=request.data)
    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def update_employee(request, id):
    try:
        theEmployee = Employee.objects.get(pk=id)
    except Employee.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'PUT':
        serializer = EmployeeSerializer(theEmployee, data=request.data)
    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_car(request, id):
    try:
        theCar = Car.objects.get(pk=id)
    except Car.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'DELETE':
        theCar.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



@api_view(['DELETE'])
def delete_customer(request, id):
    try:
        theCustomer = Customer.objects.get(pk=id)
    except Customer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        theCustomer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



@api_view(['DELETE'])
def delete_employee(request, id):
    try:
        theEmployee = Employee.objects.get(pk=id)
    except Employee.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'DELETE':
        theEmployee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['ORDER'])
def order_car(customer_id, car_id):
    if customer_id not in CustomerSerializer.fields:
        car_id.status = 'booked'
    else:
        car_id.status = 'available'


@api_view(['CANCEL'])
def cancel_order_car(customer_id, car_id):
    if customer_id and car_id.status == 'booked' in CustomerSerializer.fields:
        car_id.status = 'available'
    else:
        car_id.status = 'booked'


@api_view(['RENT'])
def rent_car(customer_id, car_id):
    if customer_id and car_id.status == 'booked' in CustomerSerializer.fields:
        car_id.status = 'rented'
    else:
        car_id.status = 'available'


@api_view(['RETURN'])
def return_car(customer_id, car_id, car_status):
    if customer_id and car_id.status == 'booked' in CustomerSerializer.fields:
        if car_status == 'damaged':
            car_id.status = 'damaged'
        elif car_status == 'ok':
            car_id.status = 'available'