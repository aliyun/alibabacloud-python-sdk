# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeCandidateInstanceTypeRequest(DaraModel):
    def __init__(
        self,
        allow_cross_az: bool = None,
        allow_different_generation: bool = None,
        data_disk_categories: List[str] = None,
        image_family: str = None,
        image_id: str = None,
        image_name: str = None,
        instance_types: List[str] = None,
        ipv_6address_count: int = None,
        max_price: float = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        spot_strategy: str = None,
        system_disk_categories: List[str] = None,
        zone_ids: List[str] = None,
    ):
        self.allow_cross_az = allow_cross_az
        self.allow_different_generation = allow_different_generation
        self.data_disk_categories = data_disk_categories
        self.image_family = image_family
        self.image_id = image_id
        self.image_name = image_name
        self.instance_types = instance_types
        self.ipv_6address_count = ipv_6address_count
        self.max_price = max_price
        self.owner_id = owner_id
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.spot_strategy = spot_strategy
        self.system_disk_categories = system_disk_categories
        self.zone_ids = zone_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allow_cross_az is not None:
            result['AllowCrossAz'] = self.allow_cross_az

        if self.allow_different_generation is not None:
            result['AllowDifferentGeneration'] = self.allow_different_generation

        if self.data_disk_categories is not None:
            result['DataDiskCategories'] = self.data_disk_categories

        if self.image_family is not None:
            result['ImageFamily'] = self.image_family

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.image_name is not None:
            result['ImageName'] = self.image_name

        if self.instance_types is not None:
            result['InstanceTypes'] = self.instance_types

        if self.ipv_6address_count is not None:
            result['Ipv6AddressCount'] = self.ipv_6address_count

        if self.max_price is not None:
            result['MaxPrice'] = self.max_price

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.spot_strategy is not None:
            result['SpotStrategy'] = self.spot_strategy

        if self.system_disk_categories is not None:
            result['SystemDiskCategories'] = self.system_disk_categories

        if self.zone_ids is not None:
            result['ZoneIds'] = self.zone_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowCrossAz') is not None:
            self.allow_cross_az = m.get('AllowCrossAz')

        if m.get('AllowDifferentGeneration') is not None:
            self.allow_different_generation = m.get('AllowDifferentGeneration')

        if m.get('DataDiskCategories') is not None:
            self.data_disk_categories = m.get('DataDiskCategories')

        if m.get('ImageFamily') is not None:
            self.image_family = m.get('ImageFamily')

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')

        if m.get('InstanceTypes') is not None:
            self.instance_types = m.get('InstanceTypes')

        if m.get('Ipv6AddressCount') is not None:
            self.ipv_6address_count = m.get('Ipv6AddressCount')

        if m.get('MaxPrice') is not None:
            self.max_price = m.get('MaxPrice')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SpotStrategy') is not None:
            self.spot_strategy = m.get('SpotStrategy')

        if m.get('SystemDiskCategories') is not None:
            self.system_disk_categories = m.get('SystemDiskCategories')

        if m.get('ZoneIds') is not None:
            self.zone_ids = m.get('ZoneIds')

        return self

