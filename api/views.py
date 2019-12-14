import json
from json import JSONDecodeError

from django.http import JsonResponse
from django.views import View

from nester.nester import Nester


class ApiNest(View):
    @staticmethod
    def post(request):
        nested_levels = request.GET.getlist('q[]')
        try:
            nested = Nester.nest_json(request.body, nested_levels)
            return JsonResponse(json.loads(nested))

        except KeyError as e:
            JsonResponse({"error": f"Could not find key: {e}\n"}, status=422)
        except JSONDecodeError as e:
            JsonResponse({"error": f"Malformed JSON: {e}\n"}, status=400)
        except ValueError as e:
            JsonResponse({"error": f"Inappropriate value: {e}\n"}, status=422)

        return JsonResponse({"error": f"nothing"}, status=422)
