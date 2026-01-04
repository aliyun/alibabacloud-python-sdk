# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ens20171110 import models as main_models
from darabonba.model import DaraModel

class DescribeCloudDiskAvailableResourceInfoResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        support_resources: main_models.DescribeCloudDiskAvailableResourceInfoResponseBodySupportResources = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The specifications of resources that you can purchase.
        self.support_resources = support_resources

    def validate(self):
        if self.support_resources:
            self.support_resources.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.support_resources is not None:
            result['SupportResources'] = self.support_resources.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SupportResources') is not None:
            temp_model = main_models.DescribeCloudDiskAvailableResourceInfoResponseBodySupportResources()
            self.support_resources = temp_model.from_map(m.get('SupportResources'))

        return self

class DescribeCloudDiskAvailableResourceInfoResponseBodySupportResources(DaraModel):
    def __init__(
        self,
        support_resource: List[main_models.DescribeCloudDiskAvailableResourceInfoResponseBodySupportResourcesSupportResource] = None,
    ):
        self.support_resource = support_resource

    def validate(self):
        if self.support_resource:
            for v1 in self.support_resource:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['SupportResource'] = []
        if self.support_resource is not None:
            for k1 in self.support_resource:
                result['SupportResource'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.support_resource = []
        if m.get('SupportResource') is not None:
            for k1 in m.get('SupportResource'):
                temp_model = main_models.DescribeCloudDiskAvailableResourceInfoResponseBodySupportResourcesSupportResource()
                self.support_resource.append(temp_model.from_map(k1))

        return self

class DescribeCloudDiskAvailableResourceInfoResponseBodySupportResourcesSupportResource(DaraModel):
    def __init__(
        self,
        ability: main_models.DescribeCloudDiskAvailableResourceInfoResponseBodySupportResourcesSupportResourceAbility = None,
        can_buy_count: int = None,
        category: str = None,
        default_disk_size: int = None,
        disk_max_size: int = None,
        disk_min_size: int = None,
        ens_region_id: str = None,
        ens_region_name: str = None,
    ):
        # Node product capability.
        self.ability = ability
        # The number of disks that you can purchase.
        self.can_buy_count = can_buy_count
        # The type of the disk.
        # 
        # *   cloud_efficiency:ultra disk.
        # *   cloud_ssd:all-flash disk.
        # *   local_hdd:local HDD.
        # *   local_ssd:local SSD.
        self.category = category
        # The default size of the disk. Unit: GiB.
        self.default_disk_size = default_disk_size
        # The maximum size of the disk. Unit: GiB.
        self.disk_max_size = disk_max_size
        # The minimum size of the disk size. Unit: GiB.
        self.disk_min_size = disk_min_size
        # The ID of the edge node.
        self.ens_region_id = ens_region_id
        # The name of the task node.
        self.ens_region_name = ens_region_name

    def validate(self):
        if self.ability:
            self.ability.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ability is not None:
            result['Ability'] = self.ability.to_map()

        if self.can_buy_count is not None:
            result['CanBuyCount'] = self.can_buy_count

        if self.category is not None:
            result['Category'] = self.category

        if self.default_disk_size is not None:
            result['DefaultDiskSize'] = self.default_disk_size

        if self.disk_max_size is not None:
            result['DiskMaxSize'] = self.disk_max_size

        if self.disk_min_size is not None:
            result['DiskMinSize'] = self.disk_min_size

        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id

        if self.ens_region_name is not None:
            result['EnsRegionName'] = self.ens_region_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ability') is not None:
            temp_model = main_models.DescribeCloudDiskAvailableResourceInfoResponseBodySupportResourcesSupportResourceAbility()
            self.ability = temp_model.from_map(m.get('Ability'))

        if m.get('CanBuyCount') is not None:
            self.can_buy_count = m.get('CanBuyCount')

        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('DefaultDiskSize') is not None:
            self.default_disk_size = m.get('DefaultDiskSize')

        if m.get('DiskMaxSize') is not None:
            self.disk_max_size = m.get('DiskMaxSize')

        if m.get('DiskMinSize') is not None:
            self.disk_min_size = m.get('DiskMinSize')

        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')

        if m.get('EnsRegionName') is not None:
            self.ens_region_name = m.get('EnsRegionName')

        return self

class DescribeCloudDiskAvailableResourceInfoResponseBodySupportResourcesSupportResourceAbility(DaraModel):
    def __init__(
        self,
        ability: List[str] = None,
    ):
        self.ability = ability

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ability is not None:
            result['Ability'] = self.ability

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ability') is not None:
            self.ability = m.get('Ability')

        return self

