from rest_framework import serializers

from SerializerLearn.models import Animal, Spider, People


class AnimalSerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)
    a_name = serializers.CharField()
    a_weight = serializers.FloatField()

    def update(self, instance, validated_data):

        instance.a_name = validated_data.get("a_name", instance.a_name)
        instance.a_weight = validated_data.get("a_weight", instance.a_weight)

        instance.save()
        return instance

    def create(self, validated_data):
        return Animal.objects.create(**validated_data)


class SpiderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Spider
        fields = ("id", "s_host")


class PeopleSerializer(serializers.ModelSerializer):

    class Meta:
        model = People
        fields = ("id", "p_name", "p_age")

