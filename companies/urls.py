from rest_framework.routers import DefaultRouter
from .views import CompanyViewSet

company_router = DefaultRouter()
company_router.register(
    prefix="companies", viewset=CompanyViewSet, basename="companies"
)
