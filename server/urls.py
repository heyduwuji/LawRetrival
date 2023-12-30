from django.contrib import admin
from django.urls import re_path as url
from django.conf.urls import include
from django.views.generic import TemplateView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include('app.urls')),
    url(r'^$', TemplateView.as_view(template_name="index.html"))
]
