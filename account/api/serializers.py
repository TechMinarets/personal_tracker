from rest_framework import serializers

from account.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
class CatergorySerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
    

class UserCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'