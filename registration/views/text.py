from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view

from registration.models.text import Text, Questions
from registration.serializers.text import TextSerializer, QuestionsSerializer


@api_view(['GET',])
def get_text(request):
    if request.method == 'GET':
        text = Text.objects.get(name=request.query_params['name'])
        text_serializer = TextSerializer(text, many=False)
        return JsonResponse(text_serializer.data, status=status.HTTP_200_OK)


@api_view(['GET',])
def get_questions(request):
        questions = Questions.objects.all()
        questions_serializer = QuestionsSerializer(questions, many=True)

        return JsonResponse(questions_serializer.data, status=status.HTTP_200_OK, safe=False)
