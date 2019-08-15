from rest_framework import serializers

from ViewLearn.models import Computer


class ComputerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Computer
        fields = ("id", "c_name", "c_price")