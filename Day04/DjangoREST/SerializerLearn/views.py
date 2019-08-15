from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from SerializerLearn.models import Animal, Spider, People
from SerializerLearn.serializers import AnimalSerializer, SpiderSerializer, PeopleSerializer


@csrf_exempt
def animals(request):
    if request.method == "GET":

        animal_list = Animal.objects.all()

        serializer = AnimalSerializer(animal_list, many=True)

        return JsonResponse(serializer.data, safe=False)

    elif request.method == "POST":

        a_name = request.POST.get("a_name")
        a_weight = request.POST.get("a_weight")

        animal_data = {
            "a_name": a_name,
            "a_weight": a_weight,
        }

        serializer = AnimalSerializer(data=animal_data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse({"msg": "create fial"})


def animal(request, pk):

    if request.method == "GET":
        animal_obj = Animal.objects.get(pk=pk)

        serializer = AnimalSerializer(animal_obj)

        return JsonResponse(serializer.data)


def spiders(request):
    if request.method == "GET":
        spider_list = Spider.objects.all()

        serializer = SpiderSerializer(spider_list, many=True)

        return JsonResponse(serializer.data, safe=False)


class PeopleAPIView(APIView):

    def get(self, request):

        print(type(request))

        peoples = People.objects.all()

        serializer = PeopleSerializer(peoples, many=True)

        return Response(data=serializer.data)


@api_view(["GET"])
def HelloAPIView(request):

    print(type(request))

    # return HttpResponse("haha")

    data = {
        "msg": "ok"
    }

    return Response(data)