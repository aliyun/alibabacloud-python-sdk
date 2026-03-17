# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteProbeTaskRequest(DaraModel):
    def __init__(
        self,
        probe_task_id: str = None,
        region_id: str = None,
        sag_id: str = None,
        sn: str = None,
    ):
        # The ID of the probe task.
        # 
        # This parameter is required.
        self.probe_task_id = probe_task_id
        # The region ID of the Smart Access Gateway (SAG) instance.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/69813.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the SAG instance.
        # 
        # This parameter is required.
        self.sag_id = sag_id
        # The serial number of the SAG device.
        # 
        # This parameter is required.
        self.sn = sn

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.probe_task_id is not None:
            result['ProbeTaskId'] = self.probe_task_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.sag_id is not None:
            result['SagId'] = self.sag_id

        if self.sn is not None:
            result['Sn'] = self.sn

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProbeTaskId') is not None:
            self.probe_task_id = m.get('ProbeTaskId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SagId') is not None:
            self.sag_id = m.get('SagId')

        if m.get('Sn') is not None:
            self.sn = m.get('Sn')

        return self

