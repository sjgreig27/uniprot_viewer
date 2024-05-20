from rest_framework import routers
from uniprot_db.viewsets.user import UserViewSet

router = routers.DefaultRouter()

router.register('users', UserViewSet)
