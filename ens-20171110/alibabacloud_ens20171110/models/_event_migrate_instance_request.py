# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class EventMigrateInstanceRequest(DaraModel):
    def __init__(
        self,
        data_policy: str = None,
        event_id: str = None,
        ops_type: str = None,
        password: str = None,
        plan_time: int = None,
        resource_id: str = None,
    ):
        # The data migration policy. Valid values:
        # 
        # *   abandon: does not migrate data. This is the default value.
        # *   force_transfer: forcibly migrates data.
        # *   try_transfer: Migrate data as much as possible.
        self.data_policy = data_policy
        # The ID of the system event.
        # 
        # This parameter is required.
        self.event_id = event_id
        # The type of the O\\&M task. Valid values:
        # 
        # *   immediate
        # *   scheduled
        # 
        # This parameter is required.
        self.ops_type = ops_type
        # The password of the instance. This parameter is optional. If you do not specify this parameter, a random password is used.
        # 
        # The password must be 8 to 30 characters in length. The password must contain uppercase letters, lowercase letters, digits, and special characters.
        # 
        # Note that you cannot enter a password for scheduled execution.
        self.password = password
        # The execution time of the reservation. The timestamp is measured in milliseconds. If the OpsType parameter is set to scheduled, this parameter is required.
        self.plan_time = plan_time
        # The ID of the resource.
        # 
        # This parameter is required.
        self.resource_id = resource_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_policy is not None:
            result['DataPolicy'] = self.data_policy

        if self.event_id is not None:
            result['EventId'] = self.event_id

        if self.ops_type is not None:
            result['OpsType'] = self.ops_type

        if self.password is not None:
            result['Password'] = self.password

        if self.plan_time is not None:
            result['PlanTime'] = self.plan_time

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataPolicy') is not None:
            self.data_policy = m.get('DataPolicy')

        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')

        if m.get('OpsType') is not None:
            self.ops_type = m.get('OpsType')

        if m.get('Password') is not None:
            self.password = m.get('Password')

        if m.get('PlanTime') is not None:
            self.plan_time = m.get('PlanTime')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        return self

