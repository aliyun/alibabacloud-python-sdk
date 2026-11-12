# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ens20171110 import models as main_models
from darabonba.model import DaraModel

class DescribeSharedDiskRecordsResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        shared_disks: List[main_models.DescribeSharedDiskRecordsResponseBodySharedDisks] = None,
        total_count: int = None,
    ):
        # The current page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The shared disk billing records.
        self.shared_disks = shared_disks
        # The total number of entries.
        self.total_count = total_count

    def validate(self):
        if self.shared_disks:
            for v1 in self.shared_disks:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['SharedDisks'] = []
        if self.shared_disks is not None:
            for k1 in self.shared_disks:
                result['SharedDisks'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.shared_disks = []
        if m.get('SharedDisks') is not None:
            for k1 in m.get('SharedDisks'):
                temp_model = main_models.DescribeSharedDiskRecordsResponseBodySharedDisks()
                self.shared_disks.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeSharedDiskRecordsResponseBodySharedDisks(DaraModel):
    def __init__(
        self,
        creation_time: str = None,
        disk_id: str = None,
        disk_size: int = None,
        last_detach_instance_id: str = None,
        last_detach_time: str = None,
        namespace: str = None,
        performance_level: int = None,
        recycle_time: str = None,
        region_id: str = None,
        sdg_id: str = None,
    ):
        # The creation time of the shared disk.
        self.creation_time = creation_time
        # The shared disk ID.
        self.disk_id = disk_id
        # The disk size. Unit: GB.
        self.disk_size = disk_size
        # The ID of the instance from which the shared disk was last detached.
        self.last_detach_instance_id = last_detach_instance_id
        # The time when the shared disk was last detached.
        self.last_detach_time = last_detach_time
        # The namespace.
        self.namespace = namespace
        # The SDG sharing ratio parameter, which supports cloud disks with different maximum sharing ratios.
        self.performance_level = performance_level
        # The reclamation time of the shared disk.
        self.recycle_time = recycle_time
        # The region ID.
        self.region_id = region_id
        # The SDG ID of the shared disk.
        self.sdg_id = sdg_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.disk_id is not None:
            result['DiskId'] = self.disk_id

        if self.disk_size is not None:
            result['DiskSize'] = self.disk_size

        if self.last_detach_instance_id is not None:
            result['LastDetachInstanceId'] = self.last_detach_instance_id

        if self.last_detach_time is not None:
            result['LastDetachTime'] = self.last_detach_time

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.performance_level is not None:
            result['PerformanceLevel'] = self.performance_level

        if self.recycle_time is not None:
            result['RecycleTime'] = self.recycle_time

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.sdg_id is not None:
            result['SdgId'] = self.sdg_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('DiskId') is not None:
            self.disk_id = m.get('DiskId')

        if m.get('DiskSize') is not None:
            self.disk_size = m.get('DiskSize')

        if m.get('LastDetachInstanceId') is not None:
            self.last_detach_instance_id = m.get('LastDetachInstanceId')

        if m.get('LastDetachTime') is not None:
            self.last_detach_time = m.get('LastDetachTime')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('PerformanceLevel') is not None:
            self.performance_level = m.get('PerformanceLevel')

        if m.get('RecycleTime') is not None:
            self.recycle_time = m.get('RecycleTime')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SdgId') is not None:
            self.sdg_id = m.get('SdgId')

        return self

