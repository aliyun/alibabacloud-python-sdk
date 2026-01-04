# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ens20171110 import models as main_models
from darabonba.model import DaraModel

class DescribeDiskIopsListResponseBody(DaraModel):
    def __init__(
        self,
        disk_iops_list: List[main_models.DescribeDiskIopsListResponseBodyDiskIopsList] = None,
        request_id: str = None,
    ):
        # The IOPS monitoring data of the cloud disk.
        self.disk_iops_list = disk_iops_list
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.disk_iops_list:
            for v1 in self.disk_iops_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DiskIopsList'] = []
        if self.disk_iops_list is not None:
            for k1 in self.disk_iops_list:
                result['DiskIopsList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.disk_iops_list = []
        if m.get('DiskIopsList') is not None:
            for k1 in m.get('DiskIopsList'):
                temp_model = main_models.DescribeDiskIopsListResponseBodyDiskIopsList()
                self.disk_iops_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeDiskIopsListResponseBodyDiskIopsList(DaraModel):
    def __init__(
        self,
        biz_time: str = None,
        disk_id: str = None,
        read_bytes: int = None,
        read_latency: int = None,
        read_ops: int = None,
        region_id: str = None,
        write_bytes: int = None,
        write_latency: int = None,
        write_ops: int = None,
    ):
        # The business time . The time is displayed in the yyyy-MM-dd HH:mm:ss.
        self.biz_time = biz_time
        # The ID of the disk.
        self.disk_id = disk_id
        # The read throughput. Unit: bytes.
        self.read_bytes = read_bytes
        # The read latency. Unit: ms.
        self.read_latency = read_latency
        # The read IOPS.
        self.read_ops = read_ops
        # The ID of the node.
        self.region_id = region_id
        # The write throughput. Unit: bytes.
        self.write_bytes = write_bytes
        # The write latency. Unit: microseconds.
        self.write_latency = write_latency
        # The write IOPS.
        self.write_ops = write_ops

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_time is not None:
            result['BizTime'] = self.biz_time

        if self.disk_id is not None:
            result['DiskId'] = self.disk_id

        if self.read_bytes is not None:
            result['ReadBytes'] = self.read_bytes

        if self.read_latency is not None:
            result['ReadLatency'] = self.read_latency

        if self.read_ops is not None:
            result['ReadOps'] = self.read_ops

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.write_bytes is not None:
            result['WriteBytes'] = self.write_bytes

        if self.write_latency is not None:
            result['WriteLatency'] = self.write_latency

        if self.write_ops is not None:
            result['WriteOps'] = self.write_ops

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizTime') is not None:
            self.biz_time = m.get('BizTime')

        if m.get('DiskId') is not None:
            self.disk_id = m.get('DiskId')

        if m.get('ReadBytes') is not None:
            self.read_bytes = m.get('ReadBytes')

        if m.get('ReadLatency') is not None:
            self.read_latency = m.get('ReadLatency')

        if m.get('ReadOps') is not None:
            self.read_ops = m.get('ReadOps')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('WriteBytes') is not None:
            self.write_bytes = m.get('WriteBytes')

        if m.get('WriteLatency') is not None:
            self.write_latency = m.get('WriteLatency')

        if m.get('WriteOps') is not None:
            self.write_ops = m.get('WriteOps')

        return self

