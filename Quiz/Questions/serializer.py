from rest_framework import serializers
from .models import Question
from django_restql.mixins import DynamicFieldsMixin

class FewSerializer(serializers.ModelSerializer):
    class Meta:
        model=Question
        fields=('id','Question', 'Option_A', 'Option_B',
                  'Option_C', 'Option_D')


class QuesSerializers(serializers.ModelSerializer):
    class Meta:
        model=Question
        fields = '__all__'


