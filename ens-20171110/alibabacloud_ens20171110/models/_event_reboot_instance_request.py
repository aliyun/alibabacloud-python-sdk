# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class EventRebootInstanceRequest(DaraModel):
    def __init__(
        self,
        event_id: str = None,
        ops_type: str = None,
        plan_time: int = None,
        plan_utc_time: str = None,
        resource_id: str = None,
    ):
        # The ID of the system Event.
        # 
        # This parameter is required.
        self.event_id = event_id
        # The type of the operation. Valid values:
        # 
        # - immediate: Executes the operation immediately.
        # 
        # - scheduled: Executes the operation at the specified time.
        # 
        # This parameter is required.
        self.ops_type = ops_type
        # The scheduled execution time, as a Timestamp in milliseconds. This parameter is required when OpsType is set to scheduled.
        self.plan_time = plan_time
        # Reserved parameter.
        self.plan_utc_time = plan_utc_time
        # The ID of the Resource.
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
        if self.event_id is not None:
            result['EventId'] = self.event_id

        if self.ops_type is not None:
            result['OpsType'] = self.ops_type

        if self.plan_time is not None:
            result['PlanTime'] = self.plan_time

        if self.plan_utc_time is not None:
            result['PlanUtcTime'] = self.plan_utc_time

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')

        if m.get('OpsType') is not None:
            self.ops_type = m.get('OpsType')

        if m.get('PlanTime') is not None:
            self.plan_time = m.get('PlanTime')

        if m.get('PlanUtcTime') is not None:
            self.plan_utc_time = m.get('PlanUtcTime')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        return self

