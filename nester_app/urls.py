from django.views.decorators.csrf import csrf_exempt
from django.urls import path

from helpers.basic_auth import auth_required
from api.views import ApiNest

urlpatterns = [
    # exempting csrf token as REST API and HTTP Basic authentication are stateless.
    path('api/nest', csrf_exempt(auth_required(ApiNest.as_view())), name='api_nest'),
]
