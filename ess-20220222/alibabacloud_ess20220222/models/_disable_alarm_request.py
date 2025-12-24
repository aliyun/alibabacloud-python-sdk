# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DisableAlarmRequest(DaraModel):
    def __init__(
        self,
        alarm_task_id: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
    ):
        # The ID of the event-triggered task.
        # 
        # This parameter is required.
        self.alarm_task_id = alarm_task_id
        self.owner_id = owner_id
        # The ID of the region.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alarm_task_id is not None:
            result['AlarmTaskId'] = self.alarm_task_id

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlarmTaskId') is not None:
            self.alarm_task_id = m.get('AlarmTaskId')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        return self

