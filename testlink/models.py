# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals

from django.db import models

class AssignmentStatus(models.Model):
    id = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=100L)
    class Meta:
        db_table = 'assignment_status'

class AssignmentTypes(models.Model):
    id = models.IntegerField(primary_key=True)
    fk_table = models.CharField(max_length=30L, blank=True)
    description = models.CharField(max_length=100L)
    class Meta:
        db_table = 'assignment_types'

class Attachments(models.Model):
    id = models.IntegerField(primary_key=True)
    fk_id = models.IntegerField()
    fk_table = models.CharField(max_length=250L, blank=True)
    title = models.CharField(max_length=250L, blank=True)
    description = models.CharField(max_length=250L, blank=True)
    file_name = models.CharField(max_length=250L)
    file_path = models.CharField(max_length=250L, blank=True)
    file_size = models.IntegerField()
    file_type = models.CharField(max_length=250L)
    date_added = models.DateTimeField()
    content = models.TextField(blank=True)
    compression_type = models.IntegerField()
    class Meta:
        db_table = 'attachments'

class Builds(models.Model):
    id = models.IntegerField(primary_key=True)
    testplan_id = models.IntegerField()
    name = models.CharField(max_length=100L)
    notes = models.TextField(blank=True)
    active = models.IntegerField()
    is_open = models.IntegerField()
    author_id = models.IntegerField(null=True, blank=True)
    creation_ts = models.DateTimeField()
    release_date = models.DateField(null=True, blank=True)
    closed_on_date = models.DateField(null=True, blank=True)
    class Meta:
        db_table = 'builds'

class CfieldDesignValues(models.Model):
    field_id = models.IntegerField()
    node_id = models.IntegerField()
    value = models.CharField(max_length=4000L)
    class Meta:
        db_table = 'cfield_design_values'

class CfieldExecutionValues(models.Model):
    field_id = models.IntegerField()
    execution_id = models.IntegerField()
    testplan_id = models.IntegerField()
    testcase = models.ForeignKey('Testcase', db_column='tcversion_id')
    value = models.CharField(max_length=4000L)
    class Meta:
        db_table = 'cfield_execution_values'

class CfieldNodeTypes(models.Model):
    field_id = models.IntegerField()
    node_type = models.ForeignKey('NodeType', db_column='node_type_id')
    class Meta:
        db_table = 'cfield_node_types'

class CfieldTestplanDesignValues(models.Model):
    field_id = models.IntegerField()
    link_id = models.IntegerField()
    value = models.CharField(max_length=4000L)
    class Meta:
        db_table = 'cfield_testplan_design_values'

class CfieldTestprojects(models.Model):
    field_id = models.IntegerField()
    testproject_id = models.IntegerField()
    display_order = models.IntegerField()
    location = models.IntegerField()
    active = models.IntegerField()
    required_on_design = models.IntegerField()
    required_on_execution = models.IntegerField()
    class Meta:
        db_table = 'cfield_testprojects'

class CustomFields(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=64L, unique=True)
    label = models.CharField(max_length=64L)
    type = models.IntegerField()
    possible_values = models.CharField(max_length=4000L)
    default_value = models.CharField(max_length=4000L)
    valid_regexp = models.CharField(max_length=255L)
    length_min = models.IntegerField()
    length_max = models.IntegerField()
    show_on_design = models.IntegerField()
    enable_on_design = models.IntegerField()
    show_on_execution = models.IntegerField()
    enable_on_execution = models.IntegerField()
    show_on_testplan_design = models.IntegerField()
    enable_on_testplan_design = models.IntegerField()
    class Meta:
        db_table = 'custom_fields'

class DbVersion(models.Model):
    version = models.CharField(max_length=50L)
    upgrade_ts = models.DateTimeField()
    notes = models.TextField(blank=True)
    class Meta:
        db_table = 'db_version'

class Events(models.Model):
    id = models.IntegerField(primary_key=True)
    transaction_id = models.IntegerField()
    log_level = models.IntegerField()
    source = models.CharField(max_length=45L, blank=True)
    description = models.TextField()
    fired_at = models.IntegerField()
    activity = models.CharField(max_length=45L, blank=True)
    object_id = models.IntegerField(null=True, blank=True)
    object_type = models.CharField(max_length=45L, blank=True)
    class Meta:
        db_table = 'events'

class ExecutionBugs(models.Model):
    execution_id = models.IntegerField()
    bug_id = models.CharField(max_length=16L)
    class Meta:
        db_table = 'execution_bugs'

class Executions(models.Model):
    id = models.IntegerField(primary_key=True)
    build_id = models.IntegerField()
    tester_id = models.IntegerField(null=True, blank=True)
    execution_ts = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=1L, blank=True)
    testplan_id = models.IntegerField()
    testcase = models.ForeignKey('Testcase', db_column='tcversion_id')
    tcversion_number = models.IntegerField()
    platform_id = models.IntegerField()
    execution_type = models.IntegerField()
    notes = models.TextField(blank=True)
    class Meta:
        db_table = 'executions'

class Inventory(models.Model):
    id = models.IntegerField(primary_key=True)
    testproject_id = models.IntegerField()
    owner_id = models.IntegerField()
    name = models.CharField(max_length=255L)
    ipaddress = models.CharField(max_length=255L)
    content = models.TextField(blank=True)
    creation_ts = models.DateTimeField()
    modification_ts = models.DateTimeField()
    class Meta:
        db_table = 'inventory'

class Issuetrackers(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100L, unique=True)
    type = models.IntegerField(null=True, blank=True)
    cfg = models.TextField(blank=True)
    class Meta:
        db_table = 'issuetrackers'

class Keywords(models.Model):
    id = models.IntegerField(primary_key=True)
    keyword = models.CharField(max_length=100L)
    testproject_id = models.IntegerField()
    notes = models.TextField(blank=True)
    class Meta:
        db_table = 'keywords'

class LastExecutions(models.Model):
    id = models.IntegerField(primary_key=True)
    # id = models.IntegerField(null=True, blank=True)
    testcase = models.ForeignKey('Testcase', db_column='tcversion_id')
    testplan_id = models.IntegerField()
    platform_id = models.IntegerField()
    build_id = models.IntegerField()
    class Meta:
        db_table = 'last_executions'

class LastExecutionsByPlatform(models.Model):
    id = models.IntegerField(primary_key=True)
    # id = models.IntegerField(null=True, blank=True)
    testcase = models.ForeignKey('Testcase', db_column='tcversion_id')
    testplan_id = models.IntegerField()
    platform_id = models.IntegerField()
    class Meta:
        db_table = 'last_executions_by_platform'

class Milestones(models.Model):
    id = models.IntegerField(primary_key=True)
    testplan_id = models.IntegerField()
    target_date = models.DateField(null=True, blank=True)
    start_date = models.DateField()
    a = models.IntegerField()
    b = models.IntegerField()
    c = models.IntegerField()
    name = models.CharField(max_length=100L)
    class Meta:
        db_table = 'milestones'

class NodeType(models.Model):
    id = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=100L)
    class Meta:
        db_table = 'node_types'

class NodesHierarchy(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100L, blank=True)
    parent_id = models.IntegerField(null=True, blank=True)
    node_type = models.ForeignKey('NodeType', db_column='node_type_id')
    node_order = models.IntegerField(null=True, blank=True)
    class Meta:
        verbose_name = 'nodes hierarchy'
        verbose_name_plural = 'nodes hierarchy'
        db_table = 'nodes_hierarchy'

class ObjectKeywords(models.Model):
    id = models.IntegerField(primary_key=True)
    fk_id = models.IntegerField()
    fk_table = models.CharField(max_length=30L, blank=True)
    keyword_id = models.IntegerField()
    class Meta:
        db_table = 'object_keywords'

class Platforms(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100L)
    testproject_id = models.IntegerField()
    notes = models.TextField()
    class Meta:
        db_table = 'platforms'

class ReqCoverage(models.Model):
    req_id = models.IntegerField()
    testcase_id = models.IntegerField()
    class Meta:
        db_table = 'req_coverage'

class ReqRelations(models.Model):
    id = models.IntegerField(primary_key=True)
    source_id = models.IntegerField()
    destination_id = models.IntegerField()
    relation_type = models.IntegerField()
    author_id = models.IntegerField(null=True, blank=True)
    creation_ts = models.DateTimeField()
    class Meta:
        db_table = 'req_relations'

class ReqRevisions(models.Model):
    parent_id = models.IntegerField()
    id = models.IntegerField(primary_key=True)
    revision = models.IntegerField()
    req_doc_id = models.CharField(max_length=64L, blank=True)
    name = models.CharField(max_length=100L, blank=True)
    scope = models.TextField(blank=True)
    status = models.CharField(max_length=1L)
    type = models.CharField(max_length=1L, blank=True)
    active = models.IntegerField()
    is_open = models.IntegerField()
    expected_coverage = models.IntegerField()
    log_message = models.TextField(blank=True)
    author_id = models.IntegerField(null=True, blank=True)
    creation_ts = models.DateTimeField()
    modifier_id = models.IntegerField(null=True, blank=True)
    modification_ts = models.DateTimeField()
    class Meta:
        db_table = 'req_revisions'

class ReqSpecs(models.Model):
    id = models.IntegerField(primary_key=True)
    testproject_id = models.IntegerField()
    doc_id = models.CharField(max_length=64L)
    class Meta:
        db_table = 'req_specs'

class ReqSpecsRevisions(models.Model):
    parent_id = models.IntegerField()
    id = models.IntegerField(primary_key=True)
    revision = models.IntegerField()
    doc_id = models.CharField(max_length=64L, blank=True)
    name = models.CharField(max_length=100L, blank=True)
    scope = models.TextField(blank=True)
    total_req = models.IntegerField()
    status = models.IntegerField(null=True, blank=True)
    type = models.CharField(max_length=1L, blank=True)
    log_message = models.TextField(blank=True)
    author_id = models.IntegerField(null=True, blank=True)
    creation_ts = models.DateTimeField()
    modifier_id = models.IntegerField(null=True, blank=True)
    modification_ts = models.DateTimeField()
    class Meta:
        db_table = 'req_specs_revisions'

class ReqVersions(models.Model):
    id = models.IntegerField(primary_key=True)
    version = models.IntegerField()
    revision = models.IntegerField()
    scope = models.TextField(blank=True)
    status = models.CharField(max_length=1L)
    type = models.CharField(max_length=1L, blank=True)
    active = models.IntegerField()
    is_open = models.IntegerField()
    expected_coverage = models.IntegerField()
    author_id = models.IntegerField(null=True, blank=True)
    creation_ts = models.DateTimeField()
    modifier_id = models.IntegerField(null=True, blank=True)
    modification_ts = models.DateTimeField()
    log_message = models.TextField(blank=True)
    class Meta:
        db_table = 'req_versions'

class Reqmgrsystems(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100L, unique=True)
    type = models.IntegerField(null=True, blank=True)
    cfg = models.TextField(blank=True)
    class Meta:
        db_table = 'reqmgrsystems'

class Requirements(models.Model):
    id = models.IntegerField(primary_key=True)
    srs_id = models.IntegerField()
    req_doc_id = models.CharField(max_length=64L)
    class Meta:
        db_table = 'requirements'

class Rights(models.Model):
    id = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=100L, unique=True)
    class Meta:
        db_table = 'rights'

class RiskAssignments(models.Model):
    id = models.IntegerField(primary_key=True)
    testplan_id = models.IntegerField()
    node_id = models.IntegerField()
    risk = models.CharField(max_length=1L)
    importance = models.CharField(max_length=1L)
    class Meta:
        db_table = 'risk_assignments'

class RoleRights(models.Model):
    role_id = models.IntegerField()
    right_id = models.IntegerField()
    class Meta:
        db_table = 'role_rights'

class Roles(models.Model):
    id = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=100L, unique=True)
    notes = models.TextField(blank=True)
    class Meta:
        db_table = 'roles'

class TcasesActive(models.Model):
    tcase_id = models.IntegerField(null=True, blank=True)
    tc_external_id = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'tcases_active'

class Tcsteps(models.Model):
    id = models.IntegerField(primary_key=True)
    step_number = models.IntegerField()
    actions = models.TextField(blank=True)
    expected_results = models.TextField(blank=True)
    active = models.IntegerField()
    execution_type = models.IntegerField()
    class Meta:
        db_table = 'tcsteps'

class Testcase(models.Model):
    id = models.IntegerField(primary_key=True)
    tc_external_id = models.IntegerField(null=True, blank=True)
    version = models.IntegerField()
    layout = models.IntegerField()
    status = models.IntegerField()
    summary = models.TextField(blank=True)
    preconditions = models.TextField(blank=True)
    importance = models.IntegerField()
    author = models.ForeignKey('Users', db_column='author_id', related_name='authored_testcase_set')
    creation_ts = models.DateTimeField()
    updater = models.ForeignKey('Users', db_column='updater_id', related_name='updated_testcase_set')
    modification_ts = models.DateTimeField()
    active = models.IntegerField()
    is_open = models.IntegerField()
    execution_type = models.IntegerField()
    class Meta:
        db_table = 'tcversions'

class TcversionsLastActive(models.Model):
    id = models.IntegerField(primary_key=True)
    # id = models.IntegerField()
    tc_external_id = models.IntegerField(null=True, blank=True)
    version = models.IntegerField()
    layout = models.IntegerField()
    status = models.IntegerField()
    summary = models.TextField(blank=True)
    preconditions = models.TextField(blank=True)
    importance = models.IntegerField()
    author_id = models.IntegerField(null=True, blank=True)
    creation_ts = models.DateTimeField()
    updater_id = models.IntegerField(null=True, blank=True)
    modification_ts = models.DateTimeField()
    active = models.IntegerField()
    is_open = models.IntegerField()
    execution_type = models.IntegerField()
    tcase_id = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'tcversions_last_active'

class TcversionsLastActiveBareBones(models.Model):
    tcase_id = models.IntegerField(null=True, blank=True)
    testcase = models.ForeignKey('Testcase', db_column='tcversion_id')
    class Meta:
        db_table = 'tcversions_last_active_bare_bones'

class TestcaseKeywords(models.Model):
    testcase_id = models.IntegerField()
    keyword_id = models.IntegerField()
    class Meta:
        db_table = 'testcase_keywords'

class TestplanPlatforms(models.Model):
    id = models.IntegerField(primary_key=True)
    testplan_id = models.IntegerField()
    platform_id = models.IntegerField()
    class Meta:
        db_table = 'testplan_platforms'

class TestplanTcversions(models.Model):
    id = models.IntegerField(primary_key=True)
    testplan_id = models.IntegerField()
    testcase = models.ForeignKey('Testcase', db_column='tcversion_id')
    node_order = models.IntegerField()
    urgency = models.IntegerField()
    platform_id = models.IntegerField()
    author_id = models.IntegerField(null=True, blank=True)
    creation_ts = models.DateTimeField()
    class Meta:
        db_table = 'testplan_tcversions'

class Testplans(models.Model):
    id = models.IntegerField(primary_key=True)
    testproject_id = models.IntegerField()
    notes = models.TextField(blank=True)
    active = models.IntegerField()
    is_open = models.IntegerField()
    is_public = models.IntegerField()
    class Meta:
        db_table = 'testplans'

class TestprojectIssuetracker(models.Model):
    testproject_id = models.IntegerField(primary_key=True)
    issuetracker_id = models.IntegerField()
    class Meta:
        db_table = 'testproject_issuetracker'

class TestprojectReqmgrsystem(models.Model):
    testproject_id = models.IntegerField(primary_key=True)
    reqmgrsystem_id = models.IntegerField()
    class Meta:
        db_table = 'testproject_reqmgrsystem'

class Testprojects(models.Model):
    id = models.IntegerField(primary_key=True)
    notes = models.TextField(blank=True)
    color = models.CharField(max_length=12L)
    active = models.IntegerField()
    option_reqs = models.IntegerField()
    option_priority = models.IntegerField()
    option_automation = models.IntegerField()
    options = models.TextField(blank=True)
    prefix = models.CharField(max_length=16L, unique=True)
    tc_counter = models.IntegerField()
    is_public = models.IntegerField()
    issue_tracker_enabled = models.IntegerField()
    reqmgr_integration_enabled = models.IntegerField()
    class Meta:
        db_table = 'testprojects'

class Testsuites(models.Model):
    id = models.IntegerField(primary_key=True)
    details = models.TextField(blank=True)
    class Meta:
        db_table = 'testsuites'

class Transactions(models.Model):
    id = models.IntegerField(primary_key=True)
    entry_point = models.CharField(max_length=45L)
    start_time = models.IntegerField()
    end_time = models.IntegerField()
    user_id = models.IntegerField()
    session_id = models.CharField(max_length=45L, blank=True)
    class Meta:
        db_table = 'transactions'

class UserAssignments(models.Model):
    id = models.IntegerField(primary_key=True)
    type = models.IntegerField()
    feature_id = models.IntegerField()
    user_id = models.IntegerField(null=True, blank=True)
    build_id = models.IntegerField(null=True, blank=True)
    deadline_ts = models.DateTimeField(null=True, blank=True)
    assigner_id = models.IntegerField(null=True, blank=True)
    creation_ts = models.DateTimeField()
    status = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'user_assignments'

class UserGroup(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100L, unique=True)
    description = models.TextField(blank=True)
    class Meta:
        db_table = 'user_group'

class UserGroupAssign(models.Model):
    usergroup_id = models.IntegerField()
    user_id = models.IntegerField()
    class Meta:
        db_table = 'user_group_assign'

class UserTestplanRoles(models.Model):
    user_id = models.IntegerField()
    testplan_id = models.IntegerField()
    role_id = models.IntegerField()
    class Meta:
        db_table = 'user_testplan_roles'

class UserTestprojectRoles(models.Model):
    user_id = models.IntegerField()
    testproject_id = models.IntegerField()
    role_id = models.IntegerField()
    class Meta:
        db_table = 'user_testproject_roles'

class Users(models.Model):
    id = models.IntegerField(primary_key=True)
    login = models.CharField(max_length=30L, unique=True)
    password = models.CharField(max_length=32L)
    role_id = models.IntegerField()
    email = models.CharField(max_length=100L)
    first = models.CharField(max_length=30L)
    last = models.CharField(max_length=30L)
    locale = models.CharField(max_length=10L)
    default_testproject_id = models.IntegerField(null=True, blank=True)
    active = models.IntegerField()
    script_key = models.CharField(max_length=32L, blank=True)
    cookie_string = models.CharField(max_length=64L, unique=True)
    class Meta:
        db_table = 'users'

