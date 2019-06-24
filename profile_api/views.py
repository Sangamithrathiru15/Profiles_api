from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status#contains status codes for returning responses from api
from profile_api import serializers
from rest_framework import viewsets

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


class HelloViewSet(viewsets.ViewSet):
    """test  api viewset"""
    serializer_class=serializers.HelloSerializer

    def list(self,request):
        """"return hello message"""
        view_set=[
        'uses actions (lit,create,retrieve,update,partial_update)',
        'Automatically maps to URL using routers',
        'provides more functionality with less code',
        ]
        return Response({'message':'hello','view_set':view_set})

    def create(self,request):
        """create a new hello message"""
        serializer=self.serializer_class(data=request.data)

        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            message=f'hello {name}'
            return Response({'message':message})

        else:
            return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
            )

    def retrieve(self,request,pk=None):
        """to handle the retrieval of an object by its id"""
        return Response({'http_method':'GET'})

    def update(self,request,pk=None):
        """to handle the updation of an object by its id"""
        return Response({'http_method':'PUT'})

    def partial_update(self,request,pk=None):
        """to handle the partialupdate  of an object by its id"""
        return Response({'http_method':'PATCH'})

    def destroy(self,request,pk=None):
        """to handle the removal of an object by its id"""
        return Response({'http_method':'DELETE'})
