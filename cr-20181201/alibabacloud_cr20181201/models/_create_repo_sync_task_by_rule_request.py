# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateRepoSyncTaskByRuleRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        repo_id: str = None,
        sync_rule_id: str = None,
        tag: str = None,
    ):
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The ID of the image repository.
        # 
        # This parameter is required.
        self.repo_id = repo_id
        # The ID of the synchronization rule.
        # 
        # This parameter is required.
        self.sync_rule_id = sync_rule_id
        # The version of the image to be synchronized.
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

        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')

        if m.get('SyncRuleId') is not None:
            self.sync_rule_id = m.get('SyncRuleId')

        if m.get('Tag') is not None:
            self.tag = m.get('Tag')

        return self

