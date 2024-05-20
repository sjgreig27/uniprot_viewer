from rest_framework import serializers
from uniprot_db.models import User


class UserSerializer(serializers.ModelSerializer):

    full_name = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = "__all__"
