from django.urls import path
from rest_framework.response import Response
from rest_framework.views import APIView

class HelloView(APIView):
    def get(self, request):
        return Response({"message": "Welcome to ALX Travel App!"})

urlpatterns = [
    path("hello/", HelloView.as_view(), name="hello"),
]
