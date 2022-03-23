from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404, handler500
from django.conf import settings
from django.conf.urls.static import static
import jobs.views
import pokerfunc.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', jobs.views.home, name="home"),
    path('features/', jobs.views.features, name="features"),
    path('about/', jobs.views.about, name="about"),
    path('squire/', pokerfunc.views.squire, name="squire"),
    path('settings/', pokerfunc.views.settings, name="settings"),
    path('results/', pokerfunc.views.results, name="results"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'jobs.views.error_404'
handler500 = 'jobs.views.error_500'
