# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class DescribeStorageSetsResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        storage_sets: main_models.DescribeStorageSetsResponseBodyStorageSets = None,
        total_count: int = None,
    ):
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # Details about the storage sets. The value of this parameter is an array that consists of StorageSet data.
        self.storage_sets = storage_sets
        # The total number of storage sets.
        self.total_count = total_count

    def validate(self):
        if self.storage_sets:
            self.storage_sets.validate()

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

        if self.storage_sets is not None:
            result['StorageSets'] = self.storage_sets.to_map()

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

        if m.get('StorageSets') is not None:
            temp_model = main_models.DescribeStorageSetsResponseBodyStorageSets()
            self.storage_sets = temp_model.from_map(m.get('StorageSets'))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeStorageSetsResponseBodyStorageSets(DaraModel):
    def __init__(
        self,
        storage_set: List[main_models.DescribeStorageSetsResponseBodyStorageSetsStorageSet] = None,
    ):
        self.storage_set = storage_set

    def validate(self):
        if self.storage_set:
            for v1 in self.storage_set:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['StorageSet'] = []
        if self.storage_set is not None:
            for k1 in self.storage_set:
                result['StorageSet'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.storage_set = []
        if m.get('StorageSet') is not None:
            for k1 in m.get('StorageSet'):
                temp_model = main_models.DescribeStorageSetsResponseBodyStorageSetsStorageSet()
                self.storage_set.append(temp_model.from_map(k1))

        return self

class DescribeStorageSetsResponseBodyStorageSetsStorageSet(DaraModel):
    def __init__(
        self,
        creation_time: str = None,
        description: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        storage_set_id: str = None,
        storage_set_name: str = None,
        storage_set_partition_number: int = None,
        tags: main_models.DescribeStorageSetsResponseBodyStorageSetsStorageSetTags = None,
        zone_id: str = None,
    ):
        # The time when the storage set was created.
        self.creation_time = creation_time
        # The description of the storage set.
        self.description = description
        # The ID of the region to which the storage set belongs.
        self.region_id = region_id
        self.resource_group_id = resource_group_id
        # The ID of the storage set.
        self.storage_set_id = storage_set_id
        # The name of the storage set.
        self.storage_set_name = storage_set_name
        # The maximum number of partitions supported by the storage set.
        self.storage_set_partition_number = storage_set_partition_number
        self.tags = tags
        # The ID of the zone to which the storage set belongs.
        self.zone_id = zone_id

    def validate(self):
        if self.tags:
            self.tags.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.description is not None:
            result['Description'] = self.description

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.storage_set_id is not None:
            result['StorageSetId'] = self.storage_set_id

        if self.storage_set_name is not None:
            result['StorageSetName'] = self.storage_set_name

        if self.storage_set_partition_number is not None:
            result['StorageSetPartitionNumber'] = self.storage_set_partition_number

        if self.tags is not None:
            result['Tags'] = self.tags.to_map()

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('StorageSetId') is not None:
            self.storage_set_id = m.get('StorageSetId')

        if m.get('StorageSetName') is not None:
            self.storage_set_name = m.get('StorageSetName')

        if m.get('StorageSetPartitionNumber') is not None:
            self.storage_set_partition_number = m.get('StorageSetPartitionNumber')

        if m.get('Tags') is not None:
            temp_model = main_models.DescribeStorageSetsResponseBodyStorageSetsStorageSetTags()
            self.tags = temp_model.from_map(m.get('Tags'))

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class DescribeStorageSetsResponseBodyStorageSetsStorageSetTags(DaraModel):
    def __init__(
        self,
        tag: List[main_models.DescribeStorageSetsResponseBodyStorageSetsStorageSetTagsTag] = None,
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
                temp_model = main_models.DescribeStorageSetsResponseBodyStorageSetsStorageSetTagsTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class DescribeStorageSetsResponseBodyStorageSetsStorageSetTagsTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

