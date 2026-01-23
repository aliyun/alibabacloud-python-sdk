# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateArtifactLifecycleRuleRequest(DaraModel):
    def __init__(
        self,
        auto: bool = None,
        enable_delete_tag: bool = None,
        instance_id: str = None,
        namespace_name: str = None,
        repo_name: str = None,
        retention_tag_count: int = None,
        schedule_time: str = None,
        scope: str = None,
        tag_regexp: str = None,
    ):
        # Specify whether to automatically execute the lifecycle management rule.
        self.auto = auto
        # Specify whether to enable lifecycle management for the artifact.
        self.enable_delete_tag = enable_delete_tag
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The name of the namespace.
        self.namespace_name = namespace_name
        # The name of the image repository.
        self.repo_name = repo_name
        # The number of images that you want to retain.
        self.retention_tag_count = retention_tag_count
        # The execution cycle of the lifecycle management rule.
        self.schedule_time = schedule_time
        # The deletion scope.
        self.scope = scope
        # The regular expression that is used to indicate which image tags are retained.
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

        if self.enable_delete_tag is not None:
            result['EnableDeleteTag'] = self.enable_delete_tag

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.namespace_name is not None:
            result['NamespaceName'] = self.namespace_name

        if self.repo_name is not None:
            result['RepoName'] = self.repo_name

        if self.retention_tag_count is not None:
            result['RetentionTagCount'] = self.retention_tag_count

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

        if m.get('EnableDeleteTag') is not None:
            self.enable_delete_tag = m.get('EnableDeleteTag')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('NamespaceName') is not None:
            self.namespace_name = m.get('NamespaceName')

        if m.get('RepoName') is not None:
            self.repo_name = m.get('RepoName')

        if m.get('RetentionTagCount') is not None:
            self.retention_tag_count = m.get('RetentionTagCount')

        if m.get('ScheduleTime') is not None:
            self.schedule_time = m.get('ScheduleTime')

        if m.get('Scope') is not None:
            self.scope = m.get('Scope')

        if m.get('TagRegexp') is not None:
            self.tag_regexp = m.get('TagRegexp')

        return self

