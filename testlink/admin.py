
from django.contrib import admin
from .models import *

admin.site.register(AssignmentStatus)
admin.site.register(AssignmentTypes)
admin.site.register(Attachments)
admin.site.register(Builds)
admin.site.register(CfieldDesignValues)
admin.site.register(CfieldExecutionValues)
admin.site.register(CfieldNodeTypes)
admin.site.register(CfieldTestplanDesignValues)
admin.site.register(CfieldTestprojects)
admin.site.register(CustomFields)
admin.site.register(DbVersion)
admin.site.register(Events)
admin.site.register(ExecutionBugs)
admin.site.register(Executions)
admin.site.register(Inventory)
admin.site.register(Issuetrackers)
admin.site.register(Keywords)
admin.site.register(LastExecutions)
admin.site.register(LastExecutionsByPlatform)
admin.site.register(Milestones)
admin.site.register(NodesHierarchy)
admin.site.register(ObjectKeywords)
admin.site.register(Platforms)
admin.site.register(ReqCoverage)
admin.site.register(ReqRelations)
admin.site.register(ReqRevisions)
admin.site.register(ReqSpecs)
admin.site.register(ReqSpecsRevisions)
admin.site.register(ReqVersions)
admin.site.register(Reqmgrsystems)
admin.site.register(Requirements)
admin.site.register(Rights)
admin.site.register(RiskAssignments)
admin.site.register(RoleRights)
admin.site.register(Roles)
admin.site.register(TcasesActive)
admin.site.register(Tcsteps)
admin.site.register(TcversionsLastActive)
admin.site.register(TcversionsLastActiveBareBones)
admin.site.register(TestcaseKeywords)
admin.site.register(TestplanPlatforms)
admin.site.register(TestplanTcversions)
admin.site.register(Testplans)
admin.site.register(TestprojectIssuetracker)
admin.site.register(TestprojectReqmgrsystem)
admin.site.register(Testprojects)
admin.site.register(Testsuites)
admin.site.register(Transactions)
admin.site.register(UserAssignments)
admin.site.register(UserGroup)
admin.site.register(UserGroupAssign)
admin.site.register(UserTestplanRoles)
admin.site.register(UserTestprojectRoles)
admin.site.register(Users)

class TestcaseAdmin(admin.ModelAdmin):
    list_display = ('id', 'tc_external_id', 'version')

admin.site.register(Testcase, TestcaseAdmin)

class NodeTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'description')

admin.site.register(NodeType, NodeTypeAdmin)
