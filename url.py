from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    # Add your app URLs here, for example:
    url(r'^q/', include('quiz.urls')),
)