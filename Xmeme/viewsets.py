from rest_framework import viewsets
from . import models
from . import serializers

class memesViewset(viewsets.ModelViewSet):
    queryset = models.memes.objects.all()
    serializer_class = serializers.memesSerializer


# class memesList(APIView):
    
#     def get(self, request):
#         memes1=models.memes.objects.all()
#         serializer=serializers.memesSerializer(memes1, many=True)
    
#     def post(self):
#         pass