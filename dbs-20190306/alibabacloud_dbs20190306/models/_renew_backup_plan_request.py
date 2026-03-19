# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RenewBackupPlanRequest(DaraModel):
    def __init__(
        self,
        backup_plan_id: str = None,
        client_token: str = None,
        owner_id: str = None,
        period: str = None,
        used_time: int = None,
    ):
        # The ID of the backup schedule.
        # 
        # This parameter is required.
        self.backup_plan_id = backup_plan_id
        # The client token that is used to ensure the idempotence of the request.
        self.client_token = client_token
        self.owner_id = owner_id
        # Specifies whether to use yearly subscription or monthly subscription for the instance. Valid values:
        # 
        # - Year
        # 
        # - Month
        # 
        # This parameter is required.
        self.period = period
        # The subscription duration of the instance. Valid values:
        # 
        # - If the Period parameter is set to Year, the value of the UsedTime parameter ranges from 1 to 9.
        # 
        # - If the Period parameter is set to Month, the value of the UsedTime parameter ranges from 1 to 11.
        # 
        # This parameter is required.
        self.used_time = used_time

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

        if self.period is not None:
            result['Period'] = self.period

        if self.used_time is not None:
            result['UsedTime'] = self.used_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupPlanId') is not None:
            self.backup_plan_id = m.get('BackupPlanId')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('UsedTime') is not None:
            self.used_time = m.get('UsedTime')

        return self

