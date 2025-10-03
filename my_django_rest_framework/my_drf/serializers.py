from rest_framework import serializers

from .models import Cucumber


class CucumberSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=150)
    
    def validate_title(self, value):
        if len(value) > 150:
            raise serializers.ValidationError("Cucumber title length")
        return value
    
    def validate(self, data):
        if len(data["title"]) > 150:
            raise serializers.ValidationError("Cucumber title length")
        return data
    
    def create(self, validated_data):
        # validated_data = dictionary of clean data
        return Cucumber.objects.create(**validated_data) 
    
    def update(self, instance, validated_data):
        # instance = existing model object
        # validated_data = new data after validation
        instance.title = validated_data.get("title", instance.title)
        instance.save()
        return instance
    
    
class ModelCucumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cucumber
        fields = '__all__'
