from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view()
def health_check(request):
    content = {"status": "healthy"}
    return Response(content, status=status.HTTP_200_OK)