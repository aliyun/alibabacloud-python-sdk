# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class StopBackupPlanRequest(DaraModel):
    def __init__(
        self,
        backup_plan_id: str = None,
        client_token: str = None,
        owner_id: str = None,
        stop_method: str = None,
    ):
        # The ID of the backup plan.
        # 
        # This parameter is required.
        self.backup_plan_id = backup_plan_id
        # A client token to ensure the idempotence of the request. This prevents the same request from being sent repeatedly.
        self.client_token = client_token
        self.owner_id = owner_id
        # The method used to pause the backup plan. Valid values:
        # 
        # - ALL: Pauses the backup schedule, full data backup jobs, incremental log backup jobs, and restore jobs.
        # 
        # - PLAN: Pauses only the backup schedule.
        # 
        # This parameter is required.
        self.stop_method = stop_method

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

        if self.stop_method is not None:
            result['StopMethod'] = self.stop_method

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupPlanId') is not None:
            self.backup_plan_id = m.get('BackupPlanId')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('StopMethod') is not None:
            self.stop_method = m.get('StopMethod')

        return self

