from tastypie import fields
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from testlink.models import Executions, Builds, Testsuites

class ExecutionsResource(ModelResource):
   status = fields.CharField(attribute='get_status_display', readonly=True)
   testcase = fields.CharField(attribute='_get_testcase_name', readonly=True)
   testsuite = fields.CharField(attribute='_get_testsuite_name', readonly=True)
   class Meta:
      queryset = Executions.objects.all()
      allowed_methods = ['get']

class BuildsResource(ModelResource):
   executions = fields.ToManyField(
      'testlink.api.resources.ExecutionsResource',
      'executions_set', full=True)
   class Meta:
      fields = ('id', 'name', 'creation_ts', 'notes')
      queryset = Builds.objects.all().select_related(
         'executions_set')
      allowed_methods = ['get']
      filtering = {
         'name': ALL,
      }

class TestsuitesResource(ModelResource):
   name = fields.CharField(attribute='_get_name', readonly=True)
   class Meta:
      queryset = Testsuites.objects.all()
      allowed_methods = ['get']