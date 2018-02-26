from django.db import models
from django.contrib.auth.models import User


class APIClient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    api_key = models.CharField(max_length=20)

    def __str__(self):
        return "{0} - {1}".format(self.user.username, self.api_key)

    def get_username(self):
        return self.user.username

    @staticmethod
    def get_by_user(user):
        return APIClient.objects.get(user=user)
