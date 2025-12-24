# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class DescribeStorageCapacityUnitsResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        storage_capacity_units: main_models.DescribeStorageCapacityUnitsResponseBodyStorageCapacityUnits = None,
        total_count: int = None,
    ):
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # Details about the SCUs.
        self.storage_capacity_units = storage_capacity_units
        # The total number of SCUs.
        self.total_count = total_count

    def validate(self):
        if self.storage_capacity_units:
            self.storage_capacity_units.validate()

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

        if self.storage_capacity_units is not None:
            result['StorageCapacityUnits'] = self.storage_capacity_units.to_map()

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

        if m.get('StorageCapacityUnits') is not None:
            temp_model = main_models.DescribeStorageCapacityUnitsResponseBodyStorageCapacityUnits()
            self.storage_capacity_units = temp_model.from_map(m.get('StorageCapacityUnits'))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeStorageCapacityUnitsResponseBodyStorageCapacityUnits(DaraModel):
    def __init__(
        self,
        storage_capacity_unit: List[main_models.DescribeStorageCapacityUnitsResponseBodyStorageCapacityUnitsStorageCapacityUnit] = None,
    ):
        self.storage_capacity_unit = storage_capacity_unit

    def validate(self):
        if self.storage_capacity_unit:
            for v1 in self.storage_capacity_unit:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['StorageCapacityUnit'] = []
        if self.storage_capacity_unit is not None:
            for k1 in self.storage_capacity_unit:
                result['StorageCapacityUnit'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.storage_capacity_unit = []
        if m.get('StorageCapacityUnit') is not None:
            for k1 in m.get('StorageCapacityUnit'):
                temp_model = main_models.DescribeStorageCapacityUnitsResponseBodyStorageCapacityUnitsStorageCapacityUnit()
                self.storage_capacity_unit.append(temp_model.from_map(k1))

        return self

class DescribeStorageCapacityUnitsResponseBodyStorageCapacityUnitsStorageCapacityUnit(DaraModel):
    def __init__(
        self,
        allocation_status: str = None,
        capacity: int = None,
        creation_time: str = None,
        description: str = None,
        expired_time: str = None,
        name: str = None,
        region_id: str = None,
        start_time: str = None,
        status: str = None,
        storage_capacity_unit_id: str = None,
        tags: main_models.DescribeStorageCapacityUnitsResponseBodyStorageCapacityUnitsStorageCapacityUnitTags = None,
    ):
        # Indicates the allocation state of the SCU when the AllocationType parameter is set to Shared. Valid values:
        # 
        # *   allocated: The SCU is allocated to other accounts.
        # *   BeAllocated: The SCU is allocated from another account.
        self.allocation_status = allocation_status
        # The capacity of the SCU.
        self.capacity = capacity
        # The time when the SCU was created.
        self.creation_time = creation_time
        # The description of the SCU.
        self.description = description
        # The time when the SCU expires.
        self.expired_time = expired_time
        # The name of the SCU.
        self.name = name
        # The region ID of the SCU.
        self.region_id = region_id
        # The time when the SCU took effect.
        self.start_time = start_time
        # The status of the SCU. Valid values:
        # 
        # *   Creating: The SCUs are being created.
        # *   Active: The SCUs are in effect.
        # *   Expired: The SCUs have expired.
        # *   Pending: The SCUs have not taken effect.
        self.status = status
        # The ID of the SCU.
        self.storage_capacity_unit_id = storage_capacity_unit_id
        # The tag key-value pairs of the SCU.
        self.tags = tags

    def validate(self):
        if self.tags:
            self.tags.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allocation_status is not None:
            result['AllocationStatus'] = self.allocation_status

        if self.capacity is not None:
            result['Capacity'] = self.capacity

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.description is not None:
            result['Description'] = self.description

        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time

        if self.name is not None:
            result['Name'] = self.name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        if self.storage_capacity_unit_id is not None:
            result['StorageCapacityUnitId'] = self.storage_capacity_unit_id

        if self.tags is not None:
            result['Tags'] = self.tags.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllocationStatus') is not None:
            self.allocation_status = m.get('AllocationStatus')

        if m.get('Capacity') is not None:
            self.capacity = m.get('Capacity')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StorageCapacityUnitId') is not None:
            self.storage_capacity_unit_id = m.get('StorageCapacityUnitId')

        if m.get('Tags') is not None:
            temp_model = main_models.DescribeStorageCapacityUnitsResponseBodyStorageCapacityUnitsStorageCapacityUnitTags()
            self.tags = temp_model.from_map(m.get('Tags'))

        return self

class DescribeStorageCapacityUnitsResponseBodyStorageCapacityUnitsStorageCapacityUnitTags(DaraModel):
    def __init__(
        self,
        tag: List[main_models.DescribeStorageCapacityUnitsResponseBodyStorageCapacityUnitsStorageCapacityUnitTagsTag] = None,
    ):
        self.tag = tag

    def validate(self):
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.DescribeStorageCapacityUnitsResponseBodyStorageCapacityUnitsStorageCapacityUnitTagsTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class DescribeStorageCapacityUnitsResponseBodyStorageCapacityUnitsStorageCapacityUnitTagsTag(DaraModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # The key of tag N.
        self.tag_key = tag_key
        # The value of tag N.
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key

        if self.tag_value is not None:
            result['TagValue'] = self.tag_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')

        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')

        return self

