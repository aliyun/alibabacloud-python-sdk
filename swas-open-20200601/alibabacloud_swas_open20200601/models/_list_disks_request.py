# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_swas_open20200601 import models as main_models
from darabonba.model import DaraModel

class ListDisksRequest(DaraModel):
    def __init__(
        self,
        disk_ids: str = None,
        disk_type: str = None,
        instance_id: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        tag: List[main_models.ListDisksRequestTag] = None,
    ):
        # The IDs of the disks. The value can be a JSON array that consists of up to 100 disk IDs. Separate multiple disk IDs with commas (,).
        self.disk_ids = disk_ids
        # The disk type. Valid values:
        # 
        # - system: system disk
        # 
        # - data: data disk
        # 
        # By default, system disks and data disks are both queried.
        self.disk_type = disk_type
        # The ID of the simple application server.
        self.instance_id = instance_id
        # The page number.
        # 
        # Default value: 1.
        self.page_number = page_number
        # The number of entries per page.
        # 
        # Maximum value: 100.
        # 
        # Default value: 10.
        self.page_size = page_size
        # The region ID of the disks.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The tags that are added to the disks.
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
        if self.disk_ids is not None:
            result['DiskIds'] = self.disk_ids

        if self.disk_type is not None:
            result['DiskType'] = self.disk_type

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DiskIds') is not None:
            self.disk_ids = m.get('DiskIds')

        if m.get('DiskType') is not None:
            self.disk_type = m.get('DiskType')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.ListDisksRequestTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class ListDisksRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key. The tag key can be up to 64 characters in length. Valid values of N: 1 to 20.
        self.key = key
        # The tag value. The tag value can be up to 64 characters in length. Valid values of N: 1 to 20.
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

