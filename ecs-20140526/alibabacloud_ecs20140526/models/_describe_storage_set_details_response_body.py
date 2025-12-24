# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class DescribeStorageSetDetailsResponseBody(DaraModel):
    def __init__(
        self,
        disks: main_models.DescribeStorageSetDetailsResponseBodyDisks = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # Details about the disks or Shared Block Storage devices in the storage set.
        self.disks = disks
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The total number of storage sets.
        self.total_count = total_count

    def validate(self):
        if self.disks:
            self.disks.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.disks is not None:
            result['Disks'] = self.disks.to_map()

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Disks') is not None:
            temp_model = main_models.DescribeStorageSetDetailsResponseBodyDisks()
            self.disks = temp_model.from_map(m.get('Disks'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeStorageSetDetailsResponseBodyDisks(DaraModel):
    def __init__(
        self,
        disk: List[main_models.DescribeStorageSetDetailsResponseBodyDisksDisk] = None,
    ):
        self.disk = disk

    def validate(self):
        if self.disk:
            for v1 in self.disk:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Disk'] = []
        if self.disk is not None:
            for k1 in self.disk:
                result['Disk'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.disk = []
        if m.get('Disk') is not None:
            for k1 in m.get('Disk'):
                temp_model = main_models.DescribeStorageSetDetailsResponseBodyDisksDisk()
                self.disk.append(temp_model.from_map(k1))

        return self

class DescribeStorageSetDetailsResponseBodyDisksDisk(DaraModel):
    def __init__(
        self,
        category: str = None,
        creation_time: str = None,
        disk_id: str = None,
        disk_name: str = None,
        region_id: str = None,
        storage_set_id: str = None,
        storage_set_partition_number: int = None,
        zone_id: str = None,
    ):
        # The category of the disk or Shared Block Storage device.
        self.category = category
        # The time when the disk or Shared Block Storage device was created.
        self.creation_time = creation_time
        # The ID of the disk or Shared Block Storage device.
        self.disk_id = disk_id
        # The name of the disk or Shared Block Storage device.
        self.disk_name = disk_name
        # The region to which the disk or Shared Block Storage device belongs.
        self.region_id = region_id
        # The ID of the storage set.
        self.storage_set_id = storage_set_id
        # The number of partitions in the storage set.
        self.storage_set_partition_number = storage_set_partition_number
        # The zone to which the disk or Shared Block Storage device belongs.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['Category'] = self.category

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.disk_id is not None:
            result['DiskId'] = self.disk_id

        if self.disk_name is not None:
            result['DiskName'] = self.disk_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.storage_set_id is not None:
            result['StorageSetId'] = self.storage_set_id

        if self.storage_set_partition_number is not None:
            result['StorageSetPartitionNumber'] = self.storage_set_partition_number

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('DiskId') is not None:
            self.disk_id = m.get('DiskId')

        if m.get('DiskName') is not None:
            self.disk_name = m.get('DiskName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('StorageSetId') is not None:
            self.storage_set_id = m.get('StorageSetId')

        if m.get('StorageSetPartitionNumber') is not None:
            self.storage_set_partition_number = m.get('StorageSetPartitionNumber')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

