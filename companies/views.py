from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination
from .serializers import CompanySerializer
from .models import Company


class CompanyViewSet(ModelViewSet):
    queryset = Company.objects.all().order_by("-last_update")
    serializer_class = CompanySerializer
    pagination_class = PageNumberPagination
