from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """Test API view"""

    def get(self,request,format=None):
        """returns a list of api features"""
        api_list=[
        'uses http methods as functions get,post,patch,put,delete',
        'is similar to a traditional django view specificlly for api',
        'gives u the most control over appl logc',
        'is manually mapped to urls',
        ]

        #every http funct must return a response whch will be the output when the api is called
        #it can return list/dict as json
        return Response({'message':'hello','api view':api_list})
