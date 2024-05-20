from django.contrib.auth.models import AbstractUser
from uniprot_db.managers.user import UserManager


class User(AbstractUser):

    objects = UserManager()

    class Meta:
        app_label = "uniprot_db"
