from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from rest_framework.decorators import api_view
# Create your views here.
from rest_framework import viewsets

from .serializers import AgLitterSerializer
from .models import AgLitter, AgParity, Herd


# class AgLitterViewSet(viewsets.ModelViewSet):
#     queryset = AgLitter.objects.all().order_by('litter_id')
#     serializer_class = AgLitterSerializer


@api_view(['GET', 'POST', 'DELETE'])
def tutorial_list(request):
    if request.method == 'GET':
        tutorials = AgLitter.objects.all().order_by('litter_id')

        title = request.query_params.get('litter_id', None)
        if title is not None:
            tutorials = tutorials.filter(title__icontains=title)

        aglitter_serializer = AgLitterSerializer(tutorials, many=True)
        return JsonResponse(aglitter_serializer.data, safe=False)
        # 'safe=False' for objects serialization

    elif request.method == 'POST':
        tutorial_data = JSONParser().parse(request)
        aglitter_serializer = AgLitterSerializer(data=tutorial_data)
        if aglitter_serializer.is_valid():
            aglitter_serializer.save()
            return JsonResponse(aglitter_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(aglitter_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = AgLitter.objects.all().delete()
        return JsonResponse({'message': '{} aglitter were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def tutorial_detail(request, pk):
    try:
        tutorial = AgLitter.objects.get(pk=pk)
    except AgLitter.DoesNotExist:
        return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        aglitter_serializer = AgLitterSerializer(tutorial)
        return JsonResponse(aglitter_serializer.data)

    elif request.method == 'PUT':
        tutorial_data = JSONParser().parse(request)
        print(tutorial_data)
        aglitter_serializer = AgLitterSerializer(tutorial, data=tutorial_data)
        if aglitter_serializer.is_valid():
            aglitter_serializer.save()
            return JsonResponse(aglitter_serializer.data)
        return JsonResponse(aglitter_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        tutorial.delete()
        return JsonResponse({'message': 'Tutorial was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


# @api_view(['GET'])
# def tutorial_list_published(request):
#     tutorials = Tutorial.objects.filter(published=True)

#     if request.method == 'GET':
#         tutorials_serializer = TutorialSerializer(tutorials, many=True)
#         return JsonResponse(tutorials_serializer.data, safe=False)
