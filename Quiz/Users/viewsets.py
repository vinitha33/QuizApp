from rest_framework import viewsets
from .models import Users
from rest_framework.response import Response
from .serializer import AddSerializer

class AddViewSets(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = AddSerializer

    def get_paginated_response(self, data):
        return Response(data)
