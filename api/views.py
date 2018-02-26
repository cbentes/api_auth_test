import json
import time

from django.http import HttpResponse
from django.contrib.auth import models

from api.api_auth import api_auth


def index(request):
    """
    """
    data = {
        'api': "Test V1",
        'timestamp': int(time.time())
    }
    data_json = json.dumps(data)
    return HttpResponse(data_json, content_type='application/json')


@api_auth
def api_hello(request, username):
    """
    """
    user = models.User.objects.get(username=username)
    name = "{0} {1}".format(user.first_name, user.last_name)
    data = {"msg": "Hello {}".format(name)}

    data_json = json.dumps(data)
    return HttpResponse(data_json, content_type='application/json')
