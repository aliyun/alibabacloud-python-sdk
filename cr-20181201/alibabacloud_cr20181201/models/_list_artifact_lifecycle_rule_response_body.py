# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cr20181201 import models as main_models
from darabonba.model import DaraModel

class ListArtifactLifecycleRuleResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        is_success: bool = None,
        page_no: int = None,
        page_size: int = None,
        request_id: str = None,
        rules: List[main_models.ListArtifactLifecycleRuleResponseBodyRules] = None,
        total_count: int = None,
    ):
        # The return value.
        self.code = code
        # Indicates whether the request is successful. Valid values:
        # 
        # *   `true`: The request is successful.
        # *   `false`: The request fails.
        self.is_success = is_success
        # The page number.
        self.page_no = page_no
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # _
        self.rules = rules
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.rules:
            for v1 in self.rules:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.is_success is not None:
            result['IsSuccess'] = self.is_success

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Rules'] = []
        if self.rules is not None:
            for k1 in self.rules:
                result['Rules'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.rules = []
        if m.get('Rules') is not None:
            for k1 in m.get('Rules'):
                temp_model = main_models.ListArtifactLifecycleRuleResponseBodyRules()
                self.rules.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListArtifactLifecycleRuleResponseBodyRules(DaraModel):
    def __init__(
        self,
        auto: bool = None,
        create_time: int = None,
        enable_delete_tag: bool = None,
        instance_id: str = None,
        modified_time: int = None,
        namespace_name: str = None,
        next_time: int = None,
        policies: List[main_models.ListArtifactLifecycleRuleResponseBodyRulesPolicies] = None,
        repo_name: str = None,
        retention_tag_count: int = None,
        rule_id: str = None,
        schedule_time: str = None,
        scope: str = None,
        tag_regexp: str = None,
    ):
        # Indicates whether the lifecycle management rule is automatically executed.
        self.auto = auto
        # The time when the lifecycle management rule was created.
        self.create_time = create_time
        # Indicates whether lifecycle management is enabled for the artifact.
        self.enable_delete_tag = enable_delete_tag
        # The instance ID.
        self.instance_id = instance_id
        # The time when the lifecycle management rule was last modified.
        self.modified_time = modified_time
        # The name of the namespace.
        self.namespace_name = namespace_name
        # The time when the lifecycle management rule is next executed.
        self.next_time = next_time
        self.policies = policies
        # The name of the image repository.
        self.repo_name = repo_name
        # The number of retained images.
        self.retention_tag_count = retention_tag_count
        # The rule ID.
        self.rule_id = rule_id
        # The execution cycle of the lifecycle management rule.
        self.schedule_time = schedule_time
        # The deletion scope of artifacts.
        self.scope = scope
        # The regular expression that indicates which image tags are retained.
        self.tag_regexp = tag_regexp

    def validate(self):
        if self.policies:
            for v1 in self.policies:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto is not None:
            result['Auto'] = self.auto

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.enable_delete_tag is not None:
            result['EnableDeleteTag'] = self.enable_delete_tag

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time

        if self.namespace_name is not None:
            result['NamespaceName'] = self.namespace_name

        if self.next_time is not None:
            result['NextTime'] = self.next_time

        result['Policies'] = []
        if self.policies is not None:
            for k1 in self.policies:
                result['Policies'].append(k1.to_map() if k1 else None)

        if self.repo_name is not None:
            result['RepoName'] = self.repo_name

        if self.retention_tag_count is not None:
            result['RetentionTagCount'] = self.retention_tag_count

        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        if self.schedule_time is not None:
            result['ScheduleTime'] = self.schedule_time

        if self.scope is not None:
            result['Scope'] = self.scope

        if self.tag_regexp is not None:
            result['TagRegexp'] = self.tag_regexp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Auto') is not None:
            self.auto = m.get('Auto')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('EnableDeleteTag') is not None:
            self.enable_delete_tag = m.get('EnableDeleteTag')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')

        if m.get('NamespaceName') is not None:
            self.namespace_name = m.get('NamespaceName')

        if m.get('NextTime') is not None:
            self.next_time = m.get('NextTime')

        self.policies = []
        if m.get('Policies') is not None:
            for k1 in m.get('Policies'):
                temp_model = main_models.ListArtifactLifecycleRuleResponseBodyRulesPolicies()
                self.policies.append(temp_model.from_map(k1))

        if m.get('RepoName') is not None:
            self.repo_name = m.get('RepoName')

        if m.get('RetentionTagCount') is not None:
            self.retention_tag_count = m.get('RetentionTagCount')

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        if m.get('ScheduleTime') is not None:
            self.schedule_time = m.get('ScheduleTime')

        if m.get('Scope') is not None:
            self.scope = m.get('Scope')

        if m.get('TagRegexp') is not None:
            self.tag_regexp = m.get('TagRegexp')

        return self

class ListArtifactLifecycleRuleResponseBodyRulesPolicies(DaraModel):
    def __init__(
        self,
        condition: main_models.ListArtifactLifecycleRuleResponseBodyRulesPoliciesCondition = None,
        filter: main_models.ListArtifactLifecycleRuleResponseBodyRulesPoliciesFilter = None,
        type: str = None,
    ):
        self.condition = condition
        self.filter = filter
        self.type = type

    def validate(self):
        if self.condition:
            self.condition.validate()
        if self.filter:
            self.filter.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.condition is not None:
            result['Condition'] = self.condition.to_map()

        if self.filter is not None:
            result['Filter'] = self.filter.to_map()

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Condition') is not None:
            temp_model = main_models.ListArtifactLifecycleRuleResponseBodyRulesPoliciesCondition()
            self.condition = temp_model.from_map(m.get('Condition'))

        if m.get('Filter') is not None:
            temp_model = main_models.ListArtifactLifecycleRuleResponseBodyRulesPoliciesFilter()
            self.filter = temp_model.from_map(m.get('Filter'))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class ListArtifactLifecycleRuleResponseBodyRulesPoliciesFilter(DaraModel):
    def __init__(
        self,
        tag_wildcard: str = None,
    ):
        self.tag_wildcard = tag_wildcard

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tag_wildcard is not None:
            result['TagWildcard'] = self.tag_wildcard

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagWildcard') is not None:
            self.tag_wildcard = m.get('TagWildcard')

        return self

class ListArtifactLifecycleRuleResponseBodyRulesPoliciesCondition(DaraModel):
    def __init__(
        self,
        last_pull_older_than_days: int = None,
        last_push_older_than_days: int = None,
        latest_tag_count: int = None,
    ):
        self.last_pull_older_than_days = last_pull_older_than_days
        self.last_push_older_than_days = last_push_older_than_days
        self.latest_tag_count = latest_tag_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.last_pull_older_than_days is not None:
            result['LastPullOlderThanDays'] = self.last_pull_older_than_days

        if self.last_push_older_than_days is not None:
            result['LastPushOlderThanDays'] = self.last_push_older_than_days

        if self.latest_tag_count is not None:
            result['LatestTagCount'] = self.latest_tag_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LastPullOlderThanDays') is not None:
            self.last_pull_older_than_days = m.get('LastPullOlderThanDays')

        if m.get('LastPushOlderThanDays') is not None:
            self.last_push_older_than_days = m.get('LastPushOlderThanDays')

        if m.get('LatestTagCount') is not None:
            self.latest_tag_count = m.get('LatestTagCount')

        return self

