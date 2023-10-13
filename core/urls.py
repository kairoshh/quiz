from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from core.swagger import schema_view



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('apps.quiz.urls')),
    path('registration/', include('apps.user.urls')),
    path('login/', include('rest_framework.urls')),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='shema-swagger-ui')
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
