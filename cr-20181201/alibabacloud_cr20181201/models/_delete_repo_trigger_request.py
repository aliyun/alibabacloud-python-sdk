# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteRepoTriggerRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        repo_id: str = None,
        trigger_id: str = None,
    ):
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The ID of the image repository.
        # 
        # This parameter is required.
        self.repo_id = repo_id
        # The ID of the trigger.
        # 
        # This parameter is required.
        self.trigger_id = trigger_id

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

        if self.trigger_id is not None:
            result['TriggerId'] = self.trigger_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')

        if m.get('TriggerId') is not None:
            self.trigger_id = m.get('TriggerId')

        return self

