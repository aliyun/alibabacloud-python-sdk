# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ebs20210730 import models as main_models
from darabonba.model import DaraModel

class DescribeDiskMonitorDataResponseBody(DaraModel):
    def __init__(
        self,
        monitor_data: List[main_models.DescribeDiskMonitorDataResponseBodyMonitorData] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The near real-time monitoring data of the disk.
        self.monitor_data = monitor_data
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
                temp_model = main_models.DescribeDiskMonitorDataResponseBodyMonitorData()
                self.monitor_data.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeDiskMonitorDataResponseBodyMonitorData(DaraModel):
    def __init__(
        self,
        bpspercent: int = None,
        burst_iocount: int = None,
        disk_id: str = None,
        iopspercent: int = None,
        read_bps: int = None,
        read_block_size: int = None,
        read_iops: int = None,
        read_latency: int = None,
        timestamp: str = None,
        write_bps: int = None,
        write_block_size: int = None,
        write_iops: int = None,
        write_latency: int = None,
    ):
        # The percentage of BPS.
        self.bpspercent = bpspercent
        # The number of burst I/O operations.
        self.burst_iocount = burst_iocount
        # The ID of the disk.
        self.disk_id = disk_id
        # The percentage of IOPS.
        self.iopspercent = iopspercent
        # The read bandwidth of the disk. Unit: MByte/s.
        self.read_bps = read_bps
        # Read IO block size. Unit: Bytes
        self.read_block_size = read_block_size
        # The maximum number of read IOPS.
        self.read_iops = read_iops
        # Read IO latency. Unit:  microsecond
        self.read_latency = read_latency
        # The timestamp that is used to query the near real-time monitoring data of the disk. The time follows the [ISO 8601](https://help.aliyun.com/document_detail/25696.html) standard in the `yyyy-MM-ddTHH:mm:ssZ` format. The time is displayed in UTC.
        self.timestamp = timestamp
        # The write bandwidth of the disk. Unit: MByte/s.
        self.write_bps = write_bps
        # Write IO block size. Unit: Bytes
        self.write_block_size = write_block_size
        # The maximum number of write IOPS.
        self.write_iops = write_iops
        # Write IO latency. Unit: microsecond
        self.write_latency = write_latency

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bpspercent is not None:
            result['BPSPercent'] = self.bpspercent

        if self.burst_iocount is not None:
            result['BurstIOCount'] = self.burst_iocount

        if self.disk_id is not None:
            result['DiskId'] = self.disk_id

        if self.iopspercent is not None:
            result['IOPSPercent'] = self.iopspercent

        if self.read_bps is not None:
            result['ReadBPS'] = self.read_bps

        if self.read_block_size is not None:
            result['ReadBlockSize'] = self.read_block_size

        if self.read_iops is not None:
            result['ReadIOPS'] = self.read_iops

        if self.read_latency is not None:
            result['ReadLatency'] = self.read_latency

        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp

        if self.write_bps is not None:
            result['WriteBPS'] = self.write_bps

        if self.write_block_size is not None:
            result['WriteBlockSize'] = self.write_block_size

        if self.write_iops is not None:
            result['WriteIOPS'] = self.write_iops

        if self.write_latency is not None:
            result['WriteLatency'] = self.write_latency

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BPSPercent') is not None:
            self.bpspercent = m.get('BPSPercent')

        if m.get('BurstIOCount') is not None:
            self.burst_iocount = m.get('BurstIOCount')

        if m.get('DiskId') is not None:
            self.disk_id = m.get('DiskId')

        if m.get('IOPSPercent') is not None:
            self.iopspercent = m.get('IOPSPercent')

        if m.get('ReadBPS') is not None:
            self.read_bps = m.get('ReadBPS')

        if m.get('ReadBlockSize') is not None:
            self.read_block_size = m.get('ReadBlockSize')

        if m.get('ReadIOPS') is not None:
            self.read_iops = m.get('ReadIOPS')

        if m.get('ReadLatency') is not None:
            self.read_latency = m.get('ReadLatency')

        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')

        if m.get('WriteBPS') is not None:
            self.write_bps = m.get('WriteBPS')

        if m.get('WriteBlockSize') is not None:
            self.write_block_size = m.get('WriteBlockSize')

        if m.get('WriteIOPS') is not None:
            self.write_iops = m.get('WriteIOPS')

        if m.get('WriteLatency') is not None:
            self.write_latency = m.get('WriteLatency')

        return self

