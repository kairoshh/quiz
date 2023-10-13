from rest_framework import permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="IT platform V0.0.2",
        default_version='V0.0.2',
        description="Online and ofline IT cource or video cources by proggramer lessons, created by Kairat",
        terms_of_service="#",
        contact=openapi.Contact(email="pony290807@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)
