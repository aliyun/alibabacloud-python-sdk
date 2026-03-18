# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteBackupRequest(DaraModel):
    def __init__(
        self,
        backup_task_id: str = None,
        instance_id: str = None,
        region_id: str = None,
    ):
        # This parameter is required.
        self.backup_task_id = backup_task_id
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backup_task_id is not None:
            result['BackupTaskId'] = self.backup_task_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupTaskId') is not None:
            self.backup_task_id = m.get('BackupTaskId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

