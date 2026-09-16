# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateRepoSyncTaskByRuleRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        priority: int = None,
        repo_id: str = None,
        sync_rule_id: str = None,
        tag: str = None,
    ):
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The execution priority of the synchronization task. Synchronization tasks are executed in descending order of priority. Synchronization tasks with the same priority are executed in random order.
        # 
        # Valid values: 1 to 5.
        # 
        # Default value: 3.
        self.priority = priority
        # The image repository ID.
        # 
        # This parameter is required.
        self.repo_id = repo_id
        # The synchronization rule ID.
        # 
        # This parameter is required.
        self.sync_rule_id = sync_rule_id
        # The image version to be synchronized.
        # 
        # This parameter is required.
        self.tag = tag

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.repo_id is not None:
            result['RepoId'] = self.repo_id

        if self.sync_rule_id is not None:
            result['SyncRuleId'] = self.sync_rule_id

        if self.tag is not None:
            result['Tag'] = self.tag

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')

        if m.get('SyncRuleId') is not None:
            self.sync_rule_id = m.get('SyncRuleId')

        if m.get('Tag') is not None:
            self.tag = m.get('Tag')

        return self

