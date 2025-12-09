from django.http import JsonResponse
from .models import Relationship

def relationship_list(request):
    data = list(Relationship.objects.values())
    return JsonResponse({"relationships": data})
