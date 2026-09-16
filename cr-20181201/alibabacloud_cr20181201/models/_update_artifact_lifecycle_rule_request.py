# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateArtifactLifecycleRuleRequest(DaraModel):
    def __init__(
        self,
        auto: bool = None,
        dry_run: bool = None,
        enable_delete_tag: bool = None,
        enable_delete_untagged_manifest: bool = None,
        instance_id: str = None,
        namespace_name: str = None,
        repo_name: str = None,
        retention_tag_count: int = None,
        rule_id: str = None,
        schedule_time: str = None,
        scope: str = None,
        tag_regexp: str = None,
    ):
        # Specifies whether to automatically execute the rule.
        self.auto = auto
        # Specifies whether to enable DryRun mode. If DryRun mode is enabled, only the lifecycle task scan is performed and no actual data cleanup is performed. DryRun mode is disabled by default.
        self.dry_run = dry_run
        # Specifies whether to enable lifecycle management.
        # 
        # Only one of this parameter and EnableDeleteUntaggedManifest can be set to true.
        self.enable_delete_tag = enable_delete_tag
        # Specifies whether to enable artifact cleanup.
        # 
        # Only one of this parameter and EnableDeleteTag can be set to true.
        self.enable_delete_untagged_manifest = enable_delete_untagged_manifest
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The namespace name.
        self.namespace_name = namespace_name
        # The image repository name.
        self.repo_name = repo_name
        # The number of images to retain.
        self.retention_tag_count = retention_tag_count
        # The rule ID.
        # 
        # This parameter is required.
        self.rule_id = rule_id
        # The execution cycle.
        self.schedule_time = schedule_time
        # The cleanup scope.
        self.scope = scope
        # The regular expression used to retain image versions.
        self.tag_regexp = tag_regexp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto is not None:
            result['Auto'] = self.auto

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.enable_delete_tag is not None:
            result['EnableDeleteTag'] = self.enable_delete_tag

        if self.enable_delete_untagged_manifest is not None:
            result['EnableDeleteUntaggedManifest'] = self.enable_delete_untagged_manifest

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.namespace_name is not None:
            result['NamespaceName'] = self.namespace_name

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

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('EnableDeleteTag') is not None:
            self.enable_delete_tag = m.get('EnableDeleteTag')

        if m.get('EnableDeleteUntaggedManifest') is not None:
            self.enable_delete_untagged_manifest = m.get('EnableDeleteUntaggedManifest')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('NamespaceName') is not None:
            self.namespace_name = m.get('NamespaceName')

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

