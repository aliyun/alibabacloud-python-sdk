# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateBackupRequest(DaraModel):
    def __init__(
        self,
        region_id: str = None,
        backup_task_id: str = None,
        description: str = None,
    ):
        self.region_id = region_id
        self.backup_task_id = backup_task_id
        self.description = description

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.backup_task_id is not None:
            result['backupTaskId'] = self.backup_task_id

        if self.description is not None:
            result['description'] = self.description

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('backupTaskId') is not None:
            self.backup_task_id = m.get('backupTaskId')

        if m.get('description') is not None:
            self.description = m.get('description')

        return self

