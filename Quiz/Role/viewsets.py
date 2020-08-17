from rest_framework import viewsets
from .serializer import RoleSerializer
from .models import Role
from rest_framework.response import Response

class RoleViewSets(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

    def get_paginated_response(self, data):
        return Response(data)
