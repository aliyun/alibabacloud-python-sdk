# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribePreCheckProgressListRequest(DaraModel):
    def __init__(
        self,
        backup_plan_id: str = None,
        client_token: str = None,
        owner_id: str = None,
        restore_task_id: str = None,
    ):
        # The ID of the backup plan.
        # 
        # > Specify either BackupPlanId or RestoreTaskId.
        self.backup_plan_id = backup_plan_id
        # The client token that is used to ensure the idempotence of the request.
        self.client_token = client_token
        self.owner_id = owner_id
        # The ID of the restore job.
        self.restore_task_id = restore_task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backup_plan_id is not None:
            result['BackupPlanId'] = self.backup_plan_id

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.restore_task_id is not None:
            result['RestoreTaskId'] = self.restore_task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupPlanId') is not None:
            self.backup_plan_id = m.get('BackupPlanId')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RestoreTaskId') is not None:
            self.restore_task_id = m.get('RestoreTaskId')

        return self

