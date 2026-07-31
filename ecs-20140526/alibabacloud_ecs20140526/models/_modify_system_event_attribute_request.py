# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifySystemEventAttributeRequest(DaraModel):
    def __init__(
        self,
        event_id: str = None,
        instance_id: str = None,
        not_before: str = None,
        region_id: str = None,
    ):
        # The event ID.
        # 
        # This parameter is required.
        self.event_id = event_id
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The new planned execution time of the system event. Specify the time in the [ISO 8601](https://www.alibabacloud.com/help/en/ecs/developer-reference/iso-8601-time-format) standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
        # 
        # This parameter is required.
        self.not_before = not_before
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.event_id is not None:
            result['EventId'] = self.event_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.not_before is not None:
            result['NotBefore'] = self.not_before

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('NotBefore') is not None:
            self.not_before = m.get('NotBefore')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

