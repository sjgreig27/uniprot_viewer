from rest_framework import viewsets
from uniprot_db.models import User
from uniprot_db.serializers.user import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.with_full_name().all()
    serializer_class = UserSerializer
