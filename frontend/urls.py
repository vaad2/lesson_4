from django.conf.urls import patterns, include, url
import views

urlpatterns = patterns('',
    # Examples:
    url(r'^$', views.IndexView.as_view(), name='IndexView'),
)
