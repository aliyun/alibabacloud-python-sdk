# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyBackupPlanNameRequest(DaraModel):
    def __init__(
        self,
        backup_plan_id: str = None,
        backup_plan_name: str = None,
        client_token: str = None,
        owner_id: str = None,
    ):
        # The ID of the backup plan.
        # 
        # This parameter is required.
        self.backup_plan_id = backup_plan_id
        # The name of the backup plan.
        # 
        # This parameter is required.
        self.backup_plan_name = backup_plan_name
        # The client token that is used to ensure the idempotence of the request. This prevents the same request from being submitted multiple times.
        self.client_token = client_token
        self.owner_id = owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backup_plan_id is not None:
            result['BackupPlanId'] = self.backup_plan_id

        if self.backup_plan_name is not None:
            result['BackupPlanName'] = self.backup_plan_name

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupPlanId') is not None:
            self.backup_plan_id = m.get('BackupPlanId')

        if m.get('BackupPlanName') is not None:
            self.backup_plan_name = m.get('BackupPlanName')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        return self

