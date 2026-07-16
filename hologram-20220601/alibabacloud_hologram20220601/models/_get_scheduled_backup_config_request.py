# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetScheduledBackupConfigRequest(DaraModel):
    def __init__(
        self,
        region_id: str = None,
        instance_id: str = None,
        schedule_type: str = None,
    ):
        self.region_id = region_id
        self.instance_id = instance_id
        self.schedule_type = schedule_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.instance_id is not None:
            result['instanceId'] = self.instance_id

        if self.schedule_type is not None:
            result['scheduleType'] = self.schedule_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')

        if m.get('scheduleType') is not None:
            self.schedule_type = m.get('scheduleType')

        return self

