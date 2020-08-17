from rest_framework import viewsets
from .models import Question
from rest_framework.response import Response
from .serializer import QuesSerializers

class QuesViewsets(viewsets.ModelViewSet):
    queryset=Question.objects.all()
    serializer_class = QuesSerializers

    def get_paginated_response(self, data):
        return Response(data)
