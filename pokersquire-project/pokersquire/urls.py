from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import jobs.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', jobs.views.home, name="home"),
    path('features/', jobs.views.features, name="features"),
    path('about/', jobs.views.about, name="about"),
    path('squire/', include('pokerfunc.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
