import base64

import binascii
from django.contrib.auth import authenticate
from django.http import HttpResponse


def auth_required(q):
    def func(request):
        if 'HTTP_AUTHORIZATION' in request.META:
            auth = request.META['HTTP_AUTHORIZATION'].split()
            if len(auth) == 2:
                if auth[0].lower() == "basic":
                    try:
                        username, password = base64.b64decode(auth[1]).decode('utf-8').split(':')
                    except (binascii.Error, UnicodeDecodeError):
                        return HttpResponse('Malformed authentication header.', status=401)

                    user = authenticate(username=username, password=password)
                    if user is not None and user.is_active:
                        return q(request)

        return HttpResponse('Unauthorized', status=401)

    return func
