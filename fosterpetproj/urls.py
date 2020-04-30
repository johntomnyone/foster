from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from fosterapp import views
from django.views.static import serve
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$',views.index,name='index'),
    url(r'^special/',views.special,name='special'),
    url(r'^fosterapp/',include('fosterapp.urls')),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^about/$', views.about, name='about'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^services/$', views.services, name='services'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^carousel/$', views.carousel, name='carousel'),
    url('avatar/', include('avatar.urls')),
]

urlpatterns += staticfiles_urlpatterns()
if settings.DEBUG:
		urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
		urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
