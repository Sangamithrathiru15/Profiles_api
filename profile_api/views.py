from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status#contains status codes for returning responses from api
from profile_api import serializers

class HelloApiView(APIView):
    """Test API view"""

    serializer_class=serializers.HelloSerializer

    def get(self,request,format=None):
        """returns a list of api features"""
        api_list=[
        'uses http methods as functions get,post,patch,put,delete',
        'is similar to a traditional django view specificlly for api',
        'gives u the most control over appl logc',
        'is manually mapped to urls',
        ]

        #every http funct must return a response whch will be the output when the api is called
        #it can return list/dict
        return Response({'message':'hello','api view':api_list})

    def post(self,request):
        """creates a hello message with our name"""
        serializer=self.serializer_class(data=request.data)

        if serializer.is_valid():#to validate the input
            name=serializer.validated_data.get('name')
            message=f'hello {name}'
            return Response({'message':message})

        else:
            return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
            )

    def put(self,request,pk=None):#updates the complete object
        """handle updating object """
        return Response({'method':'PUT'})

    def patch(self,request,pk=None):#updates just a part
        """partial updating object """
        return Response({'method':'PATCH'})

    def delete(self,request,pk=None):
        """handle deletion of object """
        return Response({'method':'DELETE'})
