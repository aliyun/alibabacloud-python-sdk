# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class DescribeDiskMonitorDataResponseBody(DaraModel):
    def __init__(
        self,
        monitor_data: main_models.DescribeDiskMonitorDataResponseBodyMonitorData = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The monitoring data of the disk.
        self.monitor_data = monitor_data
        # The request ID.
        self.request_id = request_id
        # The total number of monitoring data entries returned.
        self.total_count = total_count

    def validate(self):
        if self.monitor_data:
            self.monitor_data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.monitor_data is not None:
            result['MonitorData'] = self.monitor_data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MonitorData') is not None:
            temp_model = main_models.DescribeDiskMonitorDataResponseBodyMonitorData()
            self.monitor_data = temp_model.from_map(m.get('MonitorData'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeDiskMonitorDataResponseBodyMonitorData(DaraModel):
    def __init__(
        self,
        disk_monitor_data: List[main_models.DescribeDiskMonitorDataResponseBodyMonitorDataDiskMonitorData] = None,
    ):
        self.disk_monitor_data = disk_monitor_data

    def validate(self):
        if self.disk_monitor_data:
            for v1 in self.disk_monitor_data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DiskMonitorData'] = []
        if self.disk_monitor_data is not None:
            for k1 in self.disk_monitor_data:
                result['DiskMonitorData'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.disk_monitor_data = []
        if m.get('DiskMonitorData') is not None:
            for k1 in m.get('DiskMonitorData'):
                temp_model = main_models.DescribeDiskMonitorDataResponseBodyMonitorDataDiskMonitorData()
                self.disk_monitor_data.append(temp_model.from_map(k1))

        return self

class DescribeDiskMonitorDataResponseBodyMonitorDataDiskMonitorData(DaraModel):
    def __init__(
        self,
        bpsread: int = None,
        bpstotal: int = None,
        bpswrite: int = None,
        disk_id: str = None,
        iopsread: int = None,
        iopstotal: int = None,
        iopswrite: int = None,
        latency_read: int = None,
        latency_write: int = None,
        time_stamp: str = None,
    ):
        # The read bandwidth of the disk. Unit: byte/s.
        self.bpsread = bpsread
        # The total read and write bandwidth of the disk. Unit: byte/s.
        self.bpstotal = bpstotal
        # The write bandwidth of the disk. Unit: byte/s.
        self.bpswrite = bpswrite
        # The ID of the disk.
        self.disk_id = disk_id
        # The number of read I/O operations per second on the disk.
        self.iopsread = iopsread
        # The total number of read and write I/O operations per second on the disk.
        self.iopstotal = iopstotal
        # The number of write I/O operations per second on the disk.
        self.iopswrite = iopswrite
        # The read latency of the disk. Unit: microseconds.
        self.latency_read = latency_read
        # The write latency of the disk. Unit: microseconds.
        self.latency_write = latency_write
        # The timestamp of the monitoring data. The time follows the [ISO 8601](https://help.aliyun.com/document_detail/25696.html) standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.time_stamp = time_stamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bpsread is not None:
            result['BPSRead'] = self.bpsread

        if self.bpstotal is not None:
            result['BPSTotal'] = self.bpstotal

        if self.bpswrite is not None:
            result['BPSWrite'] = self.bpswrite

        if self.disk_id is not None:
            result['DiskId'] = self.disk_id

        if self.iopsread is not None:
            result['IOPSRead'] = self.iopsread

        if self.iopstotal is not None:
            result['IOPSTotal'] = self.iopstotal

        if self.iopswrite is not None:
            result['IOPSWrite'] = self.iopswrite

        if self.latency_read is not None:
            result['LatencyRead'] = self.latency_read

        if self.latency_write is not None:
            result['LatencyWrite'] = self.latency_write

        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BPSRead') is not None:
            self.bpsread = m.get('BPSRead')

        if m.get('BPSTotal') is not None:
            self.bpstotal = m.get('BPSTotal')

        if m.get('BPSWrite') is not None:
            self.bpswrite = m.get('BPSWrite')

        if m.get('DiskId') is not None:
            self.disk_id = m.get('DiskId')

        if m.get('IOPSRead') is not None:
            self.iopsread = m.get('IOPSRead')

        if m.get('IOPSTotal') is not None:
            self.iopstotal = m.get('IOPSTotal')

        if m.get('IOPSWrite') is not None:
            self.iopswrite = m.get('IOPSWrite')

        if m.get('LatencyRead') is not None:
            self.latency_read = m.get('LatencyRead')

        if m.get('LatencyWrite') is not None:
            self.latency_write = m.get('LatencyWrite')

        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')

        return self

