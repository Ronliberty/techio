from django.contrib.auth.views import LogoutView
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('custom/', include('custom.urls')),
    path('bms/', include('bms.urls')),
    path('portfolio/', include('portfolio.urls')),
    path('skillsync/', include('skillsync.urls')),
    path('editing/', include('editing.urls')),
    path('shop/', include('shop.urls')),
    path('accounts/', include('allauth.urls')),
    path('logout/', LogoutView.as_view(), name='logout'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)