from django.conf.urls import patterns, include, url
from frontend import admin


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'lesson_4.views.home', name='home'),
    url(r'^admin/', include(admin.admin_super.urls)),
    url(r'^editor/', include(admin.admin_editor.urls)),

    url(r'', include('frontend.urls', namespace='frontend')),
)
