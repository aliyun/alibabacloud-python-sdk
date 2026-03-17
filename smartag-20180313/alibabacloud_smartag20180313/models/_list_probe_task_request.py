# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListProbeTaskRequest(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        probe_task_id: str = None,
        protocol: str = None,
        region_id: str = None,
        sag_id: str = None,
        sag_name: str = None,
        sn: str = None,
        task_name: str = None,
    ):
        # The number of the page to return. Default value: **1**.
        self.page_number = page_number
        # The number of entries to return on each page. Maximum value: **50**. Default value: **10**.
        self.page_size = page_size
        # The ID of the probe task.
        self.probe_task_id = probe_task_id
        # The protocol of the probe task. Valid values:
        # 
        # *   **ICMP**
        # *   **TCP**
        # *   **HTTP**
        # 
        # >  Tasks that probe private networks support only ICMP and TCP.
        self.protocol = protocol
        # The region ID of the SAG instance.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/69813.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the SAG instance.
        self.sag_id = sag_id
        # The name of the SAG instance.
        self.sag_name = sag_name
        # The serial number of the SAG device.
        self.sn = sn
        # The name of the probe task.
        self.task_name = task_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.probe_task_id is not None:
            result['ProbeTaskId'] = self.probe_task_id

        if self.protocol is not None:
            result['Protocol'] = self.protocol

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.sag_id is not None:
            result['SagId'] = self.sag_id

        if self.sag_name is not None:
            result['SagName'] = self.sag_name

        if self.sn is not None:
            result['Sn'] = self.sn

        if self.task_name is not None:
            result['TaskName'] = self.task_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ProbeTaskId') is not None:
            self.probe_task_id = m.get('ProbeTaskId')

        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SagId') is not None:
            self.sag_id = m.get('SagId')

        if m.get('SagName') is not None:
            self.sag_name = m.get('SagName')

        if m.get('Sn') is not None:
            self.sn = m.get('Sn')

        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')

        return self

