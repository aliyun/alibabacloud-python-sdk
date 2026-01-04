# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ens20171110 import models as main_models
from darabonba.model import DaraModel

class DescribeSDGSharedDisksResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        shared_disks: List[main_models.DescribeSDGSharedDisksResponseBodySharedDisks] = None,
        total_count: int = None,
    ):
        # Current page number when paging
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # Shared disk list
        self.shared_disks = shared_disks
        # The total number of entries returned.
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
                temp_model = main_models.DescribeSDGSharedDisksResponseBodySharedDisks()
                self.shared_disks.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeSDGSharedDisksResponseBodySharedDisks(DaraModel):
    def __init__(
        self,
        creation_time: str = None,
        disk_id: str = None,
        disk_type: str = None,
        namespace: str = None,
        region_id: str = None,
        sdg_id: str = None,
        shared_num: int = None,
        status: str = None,
    ):
        # The time when the shared disk was created.
        self.creation_time = creation_time
        # shared disk id
        self.disk_id = disk_id
        # Shared disk type
        self.disk_type = disk_type
        # The namespace of the service.
        self.namespace = namespace
        # The node ID.
        self.region_id = region_id
        # SdgId of the shared disk
        self.sdg_id = sdg_id
        # Number of shared mounts
        self.shared_num = shared_num
        # Shared disk status
        self.status = status

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

        if self.disk_type is not None:
            result['DiskType'] = self.disk_type

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.sdg_id is not None:
            result['SdgId'] = self.sdg_id

        if self.shared_num is not None:
            result['SharedNum'] = self.shared_num

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('DiskId') is not None:
            self.disk_id = m.get('DiskId')

        if m.get('DiskType') is not None:
            self.disk_type = m.get('DiskType')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SdgId') is not None:
            self.sdg_id = m.get('SdgId')

        if m.get('SharedNum') is not None:
            self.shared_num = m.get('SharedNum')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

