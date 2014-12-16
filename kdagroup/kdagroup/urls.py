from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.base import TemplateView

#New Ones (also added base above)
from django.conf import settings


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'kdagroup.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^kdagroup/$', 'website.views.website'),
    url(r'^consulting/$', 'website.views.consulting'),
    url(r'^thankyou/$', 'website.views.sendemail'),
    url(r'^thanks/$', 'website.views.thanks'),
)

