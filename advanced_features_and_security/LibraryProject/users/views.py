from django.http import JsonResponse
from .models import CustomUser

def role_list_view(request):
    roles = list(CustomUser.objects.values("id", "username", "role"))
    return JsonResponse({"roles": roles})
