
from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from tastypie.api import Api
from testlink.api.resources import ExecutionsResource, BuildsResource
from testlink.api.resources import TestsuitesResource, TestplansResource

v1_api = Api(api_name='v1')
v1_api.register(BuildsResource())
v1_api.register(ExecutionsResource())
v1_api.register(TestplansResource())
v1_api.register(TestsuitesResource())

urlpatterns = patterns('',
   url(r'^api/', include(v1_api.urls)),
   url(r'^$',  TemplateView.as_view(template_name="testlink/results.html")),
)
