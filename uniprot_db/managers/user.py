from django.contrib.auth.models import UserManager as DefaultUserManager
from django.db.models import Value
from django.db.models.functions import Concat


class UserManager(DefaultUserManager):
    def with_full_name(self):
        return self.annotate(full_name=Concat("first_name", Value(" "), "last_name"))
