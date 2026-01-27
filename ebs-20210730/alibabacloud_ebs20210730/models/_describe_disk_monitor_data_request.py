# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDiskMonitorDataRequest(DaraModel):
    def __init__(
        self,
        disk_id: str = None,
        end_time: str = None,
        period: int = None,
        region_id: str = None,
        start_time: str = None,
        type: str = None,
    ):
        # The ID of the disk.
        # 
        # This parameter is required.
        self.disk_id = disk_id
        # The end of the time range during which you want to query the near real-time monitoring data of the disk. Specify the time in the [ISO 8601](https://help.aliyun.com/document_detail/25696.html) standard in the `yyyy-MM-ddTHH:mm:ssZ` format. The time must be in UTC.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The interval at which the near real-time monitoring data is collected. Unit: seconds. Valid values:
        # 
        # *   5
        # *   60
        # 
        # Default value: 5.
        self.period = period
        # The region ID of the disk.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The beginning of the time range during which you want to query the near real-time monitoring data of the disk. Specify the time in the [ISO 8601](https://help.aliyun.com/document_detail/25696.html) standard in the `yyyy-MM-ddTHH:mm:ssZ` format. The time must be in UTC.
        # 
        # This parameter is required.
        self.start_time = start_time
        # The type of the monitoring data. Valid values:
        # 
        # *   basic: baseline performance data.
        # *   pro: burst performance data, such as burst I/O operations.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.disk_id is not None:
            result['DiskId'] = self.disk_id

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.period is not None:
            result['Period'] = self.period

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DiskId') is not None:
            self.disk_id = m.get('DiskId')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

