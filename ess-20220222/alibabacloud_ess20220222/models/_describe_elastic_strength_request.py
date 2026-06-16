# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeElasticStrengthRequest(DaraModel):
    def __init__(
        self,
        data_disk_categories: List[str] = None,
        image_family: str = None,
        image_id: str = None,
        image_name: str = None,
        instance_types: List[str] = None,
        ipv_6address_count: int = None,
        priority_strategy: str = None,
        region_id: str = None,
        scaling_group_id: str = None,
        scaling_group_ids: List[str] = None,
        spot_strategy: str = None,
        system_disk_categories: List[str] = None,
        v_switch_ids: List[str] = None,
    ):
        # A list of data disk categories used to evaluate elastic strength. If a category is incompatible, the response identifies the specific mismatched category.
        # 
        # > You can specify this parameter if `ScalingGroupId` is not specified.
        self.data_disk_categories = data_disk_categories
        # The name of the image family. You can set this parameter to use the latest available image from the specified image family to create instances. If you specify ImageId, this parameter is ignored.
        # 
        # > If `ScalingGroupId` is not specified, you must specify at least one of `ImageId`, `ImageName`, or `ImageFamily`.
        self.image_family = image_family
        # The ID of the image used to create instances.
        # 
        # > If `ScalingGroupId` is not specified, you must specify at least one of `ImageId`, `ImageName`, or `ImageFamily`.
        self.image_id = image_id
        # The name of the image. The name must be unique within a region. If you specify `ImageId`, this parameter is ignored.
        # 
        # You cannot use this parameter to specify a Marketplace image.
        # 
        # > If `ScalingGroupId` is not specified, you must specify at least one of `ImageId`, `ImageName`, or `ImageFamily`.
        self.image_name = image_name
        # A list of ECS instance types. If specified, this parameter overrides the instance types in the scaling configuration.
        self.instance_types = instance_types
        # The number of IPv6 addresses to be configured for each instance. The elastic strength is lowered for instance types that do not support the specified number of IPv6 addresses.
        # 
        # > You can specify this parameter if `ScalingGroupId` is not specified.
        self.ipv_6address_count = ipv_6address_count
        # >Warning: This parameter is deprecated. Use `SpotStrategy` instead.
        # The spot strategy for pay-as-you-go instances. If specified, this parameter overrides the spot strategy in the scaling configuration. Valid values:
        # 
        # - `NoSpot`: A regular pay-as-you-go instance.
        # 
        # - `SpotWithPriceLimit`: A spot instance with a specified maximum price.
        # 
        # - `SpotAsPriceGo`: A spot instance where the system automatically bids at the current market price.
        # 
        # Default value: `NoSpot`.
        self.priority_strategy = priority_strategy
        # The ID of the region where the scaling group is located.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the scaling group.
        self.scaling_group_id = scaling_group_id
        # The IDs of one or more scaling groups to query in a batch operation.
        self.scaling_group_ids = scaling_group_ids
        # The spot strategy for instances. Valid values:
        # 
        # - `NoSpot`: A regular pay-as-you-go instance.
        # 
        # - `SpotWithPriceLimit`: A spot instance with a specified maximum price.
        # 
        # - `SpotAsPriceGo`: A spot instance where the system automatically bids at the current market price.
        # 
        # Default value: `NoSpot`.
        self.spot_strategy = spot_strategy
        # A list of system disk categories. If specified, this parameter overrides the system disk categories in the scaling configuration. Valid values:
        # 
        # - `cloud`: Basic Cloud Disk.
        # 
        # - `cloud_efficiency`: Ultra Cloud Disk.
        # 
        # - `cloud_ssd`: Standard SSD.
        # 
        # - `cloud_essd`: ESSD.
        # 
        # > This parameter is required if `ScalingGroupId` is not specified.
        self.system_disk_categories = system_disk_categories
        # A list of VSwitch IDs.
        # 
        # > This parameter is required if `ScalingGroupId` is not specified.
        self.v_switch_ids = v_switch_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

        if self.priority_strategy is not None:
            result['PriorityStrategy'] = self.priority_strategy

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id

        if self.scaling_group_ids is not None:
            result['ScalingGroupIds'] = self.scaling_group_ids

        if self.spot_strategy is not None:
            result['SpotStrategy'] = self.spot_strategy

        if self.system_disk_categories is not None:
            result['SystemDiskCategories'] = self.system_disk_categories

        if self.v_switch_ids is not None:
            result['VSwitchIds'] = self.v_switch_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
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

        if m.get('PriorityStrategy') is not None:
            self.priority_strategy = m.get('PriorityStrategy')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')

        if m.get('ScalingGroupIds') is not None:
            self.scaling_group_ids = m.get('ScalingGroupIds')

        if m.get('SpotStrategy') is not None:
            self.spot_strategy = m.get('SpotStrategy')

        if m.get('SystemDiskCategories') is not None:
            self.system_disk_categories = m.get('SystemDiskCategories')

        if m.get('VSwitchIds') is not None:
            self.v_switch_ids = m.get('VSwitchIds')

        return self

