
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("me.urls")),
    path('blog/', include("blog.urls")),
    path('tinymce/', include('tinymce.urls')),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

handler404 = "me.views.page_not_found_view"
