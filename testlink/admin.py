
from django.contrib import admin
from django import forms
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
admin.site.register(RiskAssignments)
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

class TcversionAdmin(admin.ModelAdmin):
    list_display = ('id', 'tc_external_id', 'version')

admin.site.register(Tcversion, TcversionAdmin)

class NodeTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'description')

admin.site.register(NodeType, NodeTypeAdmin)

class NodesHierarchyAdmin(admin.ModelAdmin):
    list_display = ('id', 'description', 'name')
    def description(self, obj):
        return obj.node_type.description

admin.site.register(NodesHierarchy, NodesHierarchyAdmin)


# Roles and Rights
admin.site.register(RoleRights)
admin.site.register(Right)
admin.site.register(Role)
admin.site.register(UserTestplanRoles)
admin.site.register(UserTestprojectRoles)

# Users and groups
class UserGroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description')

class UserGroupAssignInlineForm(forms.ModelForm):
    auto_id = False
    exclude = ('id',)
    class Meta:
        model = User.groups.through

class UserGroupAssignInline(admin.TabularInline):
    model = User.groups.through
    form = UserGroupAssignInlineForm

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'login', 'email', 'active')
    inlines = [UserGroupAssignInline,]


admin.site.register(UserGroup, UserGroupAdmin)
admin.site.register(User, UserAdmin)


