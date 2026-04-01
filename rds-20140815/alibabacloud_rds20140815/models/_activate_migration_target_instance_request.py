# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ActivateMigrationTargetInstanceRequest(DaraModel):
    def __init__(
        self,
        dbinstance_name: str = None,
        force_switch: str = None,
        resource_owner_id: int = None,
        switch_time: str = None,
        switch_time_mode: str = None,
    ):
        # The instance ID. You can call the DescribeDBInstances operation to query the instance ID.
        # 
        # This parameter is required.
        self.dbinstance_name = dbinstance_name
        # Specifies whether to forcefully perform a switchover. Set the value to 1. The value 1 specifies a forceful switchover.
        self.force_switch = force_switch
        self.resource_owner_id = resource_owner_id
        # A reserved parameter. This parameter does not take effect.
        self.switch_time = switch_time
        # The time when you want to perform the switchover.
        # 
        # Set the value to 0. The value 0 specifies an immediate switchover.
        self.switch_time_mode = switch_time_mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name

        if self.force_switch is not None:
            result['ForceSwitch'] = self.force_switch

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.switch_time is not None:
            result['SwitchTime'] = self.switch_time

        if self.switch_time_mode is not None:
            result['SwitchTimeMode'] = self.switch_time_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')

        if m.get('ForceSwitch') is not None:
            self.force_switch = m.get('ForceSwitch')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SwitchTime') is not None:
            self.switch_time = m.get('SwitchTime')

        if m.get('SwitchTimeMode') is not None:
            self.switch_time_mode = m.get('SwitchTimeMode')

        return self

