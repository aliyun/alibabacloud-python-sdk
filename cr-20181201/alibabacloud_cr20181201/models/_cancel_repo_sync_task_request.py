# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CancelRepoSyncTaskRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        sync_task_id: str = None,
    ):
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The ID of the replication task.
        # 
        # This parameter is required.
        self.sync_task_id = sync_task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.sync_task_id is not None:
            result['SyncTaskId'] = self.sync_task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('SyncTaskId') is not None:
            self.sync_task_id = m.get('SyncTaskId')

        return self

