from rest_framework import viewsets
from .models import Twitter
from .serializers import TwitterSerializer


class TwitterViewSet(viewsets.ModelViewSet):
    queryset = Twitter.objects.all()
    serializer_class = TwitterSerializer
