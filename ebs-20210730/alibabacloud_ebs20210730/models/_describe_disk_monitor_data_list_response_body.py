# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ebs20210730 import models as main_models
from darabonba.model import DaraModel

class DescribeDiskMonitorDataListResponseBody(DaraModel):
    def __init__(
        self,
        monitor_data: List[main_models.DescribeDiskMonitorDataListResponseBodyMonitorData] = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The near real-time monitoring data of the disks.
        self.monitor_data = monitor_data
        # A pagination token. It can be used in the next request to retrieve a new page of results. If NextToken is empty, no next page exists.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.monitor_data:
            for v1 in self.monitor_data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['MonitorData'] = []
        if self.monitor_data is not None:
            for k1 in self.monitor_data:
                result['MonitorData'].append(k1.to_map() if k1 else None)

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.monitor_data = []
        if m.get('MonitorData') is not None:
            for k1 in m.get('MonitorData'):
                temp_model = main_models.DescribeDiskMonitorDataListResponseBodyMonitorData()
                self.monitor_data.append(temp_model.from_map(k1))

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeDiskMonitorDataListResponseBodyMonitorData(DaraModel):
    def __init__(
        self,
        burst_iocount: int = None,
        disk_id: str = None,
        timestamp: str = None,
    ):
        # The number of burst I/O operations.
        self.burst_iocount = burst_iocount
        # The ID of the disk.
        self.disk_id = disk_id
        # The beginning of the time range during which the performance of the disk bursts. The time follows the [ISO 8601](https://help.aliyun.com/document_detail/25696.html) standard in the `yyyy-MM-ddTHH:mm:ssZ` format. The time is displayed in UTC.
        self.timestamp = timestamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.burst_iocount is not None:
            result['BurstIOCount'] = self.burst_iocount

        if self.disk_id is not None:
            result['DiskId'] = self.disk_id

        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BurstIOCount') is not None:
            self.burst_iocount = m.get('BurstIOCount')

        if m.get('DiskId') is not None:
            self.disk_id = m.get('DiskId')

        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')

        return self

