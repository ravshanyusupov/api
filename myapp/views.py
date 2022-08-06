from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Api
from .serializers import SerializerModel


@api_view(['GET'])
def apiList(request):
    api = Api.objects.all()
    serializer = SerializerModel(api, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def apiDetail(request, pk):
    api = Api.objects.get(pk=pk)
    serializer = SerializerModel(api, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def apiCreate(request):
    serializer = SerializerModel(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def apiUpdate(request, pk):
    api = Api.objects.get(pk=pk)
    serializer = SerializerModel(instance=api, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def apiDelete(request, pk):
    api = Api.objects.get(pk=pk)
    api.delete()
    return Response('Deleted data')

