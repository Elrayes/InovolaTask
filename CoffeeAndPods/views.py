
from django.http.response import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from .CoffeeSerializer import *
from .models import *


# Create your views here.

@api_view(['GET'])
def coffee_machines_products(request):
    if request.method == "GET":
        coffee_machines = CoffeeMachines.objects.all()

        product_type = request.GET.get('product_type', None)
        water_comb = request.GET.get('water_line_compatible', None)

        if product_type:
            coffee_machines = coffee_machines.filter(product_type__product_type__contains=product_type)
            print(product_type)
        if water_comb:
            if water_comb == 'true':
                water_comb = True
            else:
                water_comb = False

            coffee_machines = coffee_machines.filter(water_line_compatible=water_comb)
        coffee_serializer = CoffeeMachinesSerializer(coffee_machines, many=True)
        if coffee_machines.count() > 0:
            return JsonResponse(coffee_serializer.data, safe=False)
        else:
            return JsonResponse({"message": "No machines presented with the entered filters"},
                                status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def coffee_pots_products(request):
    pots = CoffeePot.objects.all()
    product_type = request.GET.get('product_type', None)
    flavor = request.GET.get('flavor', None)
    size = request.GET.get('pack_size', None)

    if product_type:
        pots = pots.filter(product_type__type__contains=product_type)

    if flavor:
        pots = pots.filter(coffee_flavor__flavor__contains=flavor)
    if size:
        pots = pots.filter(pack_size__contains=size)

    pots_serializer = CoffeePotSerializer(pots, many=True)
    if pots.count() > 0:
        return JsonResponse(pots_serializer.data, safe=False)
    else:
        return JsonResponse({"message": "No pots presented with the entered filters"},
                            status=status.HTTP_204_NO_CONTENT)
