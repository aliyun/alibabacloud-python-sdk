# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListExperimentGroupsRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        layer_id: str = None,
        region_id: str = None,
        status: str = None,
        time_range_end: str = None,
        time_range_start: str = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id
        self.layer_id = layer_id
        self.region_id = region_id
        self.status = status
        self.time_range_end = time_range_end
        self.time_range_start = time_range_start

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.layer_id is not None:
            result['LayerId'] = self.layer_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.status is not None:
            result['Status'] = self.status

        if self.time_range_end is not None:
            result['TimeRangeEnd'] = self.time_range_end

        if self.time_range_start is not None:
            result['TimeRangeStart'] = self.time_range_start

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('LayerId') is not None:
            self.layer_id = m.get('LayerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TimeRangeEnd') is not None:
            self.time_range_end = m.get('TimeRangeEnd')

        if m.get('TimeRangeStart') is not None:
            self.time_range_start = m.get('TimeRangeStart')

        return self

