from django.conf.urls import include, url
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
urlpatterns = [
    #Examples:
    #url(r'^$', 'mysite.views.home', name='home'),
    url(r'', include('blog.urls')),
	url(r'^admin/', include(admin.site.urls)),
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

