######## general
from django.contrib import admin
from django.urls import path, include
####### to display images
from django.conf import settings
from django.conf.urls.static import static
######### for swagger
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
    openapi.Info(
        title='Turn On',
        default_version='version 1',
        description='basketball court network'
    ),
    public=True
)

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('swagger/', schema_view.with_ui('swagger')),
                  path('account/', include('apps.account.urls')),
                  path('team/', include('apps.team.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
