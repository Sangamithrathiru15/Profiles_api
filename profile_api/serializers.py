from rest_framework import serializers
from profile_api import models

class HelloSerializer(serializers.Serializer):
    """serializes a name field for testing ourAPIView,also takes care of the validation"""
    name=serializers.CharField(max_length=10)

class UserProfileSerializer(serializers.ModelSerializer):#to confiigure a serializer to a model
    """serializes a user profile object"""

    class Meta:
        model=models.UserProfile
        fields=('id','email','name','password')#to make these fields accessible
        extra_kwargs={#to make exception to the password we provide this rule
        'password':{
            'write_only':True,#only for creating user
            'style':{'input_type':'password'}#to make the values entered as a hashed one.i.e to make this as a password field
        }
        }

    def create(Self,validated_data):
        """create and return a new user"""
        user=models.UserProfile.objects.create_user(
        email=validated_data['email'],
        name=validated_data['name'],
        password=validated_data['password']
        )
        return user
