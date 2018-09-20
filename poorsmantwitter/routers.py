from rest_framework import routers
from poortwitter.viewsets import TwitterViewSet

router = routers.DefaultRouter()

router.register(r'tweet', TwitterViewSet)
