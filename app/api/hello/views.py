from django.http import JsonResponse
from django.views import View

class HelloView(View):
    def get(self, request):
        return JsonResponse("Hello World", safe=False)
