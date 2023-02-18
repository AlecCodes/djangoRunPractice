from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
# Create your views here.

class FirstView(View):
    def get(self, request):
        return JsonResponse({"hello":"word", "method":request.method})
    def post(self, request):
        return JsonResponse({"hello":"word", "method":request.method})
    def put(self, request):
        return JsonResponse({"hello":"word", "method":request.method})
    def delete(self, request):
        return JsonResponse({"hello":"word", "method":request.method})
    
class SecondView(View):
    def get(self, request, param):
        query = request.GET.get("query", "no query")
        return JsonResponse({"param":param, "query":query})
    def post(self, request, param):
        query = request.GET.get("query", "no query")
        return JsonResponse({"param":param, "query": query})
    def put(self, request, param):
        query = request.GET.get("query", "no query")
        return JsonResponse({"param":param, "query": query})
    def delete(self, request, param):
        query = request.GET.get("query", "no query")
        return JsonResponse({"param":param, "query": query})
