"""home_inventory URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static, serve
from django.conf import settings
from django.views.generic import RedirectView

# print(dir(admin.site))
admin.site.site_header = 'PIMS'
admin.site.site_title = 'PIMS'
admin.site.index_title = 'Welcome to PIMS admin'


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('pims.urls')),
    path('', RedirectView.as_view(url='pims/')),
    path('pims/', include('pims.urls')),
    path('static/<path:path>/', serve, {'document_root': settings.STATIC_ROOT, }),
]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

