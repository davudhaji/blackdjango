from rest_framework.response import Response
from rest_framework.views import APIView
from ..models import Location

class LocationPost(APIView):

    def post(self,request):
        print(self.request.data)
        Location.objects.create(**self.request.data)
        return Response(['Success'])