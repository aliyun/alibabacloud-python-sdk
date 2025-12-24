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
        # The disk categories of the data disks. The disk categories that do not match the specified criteria are returned after you call this operation.
        # 
        # >  If you do not specify the scaling group ID, you must specify this parameter.
        self.data_disk_categories = data_disk_categories
        # The name of the image family. You can specify the ImageFamily request parameter to obtain the most recent available images in the current image family for instance creation. If you specify ImageId, you cannot specify ImageFamily.
        # 
        # >  If you do not specify the scaling group ID, you must specify at least one of ImageId, ImageName, and ImageFamily.
        self.image_family = image_family
        # The ID of the image file that provides the image resource for Auto Scaling to create instances.
        # 
        # >  If you do not specify the scaling group ID, you must specify at least one of ImageId, ImageName, and ImageFamily.
        self.image_id = image_id
        # The name of the image. Each image name must be unique in a region. If you specify ImageId, ImageName is ignored.
        # 
        # You cannot use ImageName to specify an Alibaba Cloud Marketplace image.
        # 
        # >  If you do not specify the scaling group ID, you must specify at least one of ImageId, ImageName, and ImageFamily.
        self.image_name = image_name
        # The instance types. The instance types specified by this parameter overwrite the instance types specified in the scaling configuration.
        self.instance_types = instance_types
        # The number of IPv6 addresses. If the instance type that you specified does meet the requirement for the number of IPv6 addresses, the scaling strength is weak.
        # 
        # >  If you do not specify the scaling group ID, you must specify this parameter.
        self.ipv_6address_count = ipv_6address_count
        # **
        # 
        # **Warning** This parameter is deprecated. We recommend that you use SpotStrategy.
        # 
        # The preemption policy that you want to apply to pay-as-you-go instances. The preemption policy specified by this parameter overwrites the preemption policy specified in the scaling configuration. Valid values:
        # 
        # *   NoSpot: The instances are created as regular pay-as-you-go instances.
        # *   SpotWithPriceLimit: The instances are created as preemptible instances with a user-defined maximum hourly price.
        # *   SpotAsPriceGo: The instances are created as preemptible instances for which the market price at the time of purchase is automatically used as the bidding price.
        # 
        # Default value: NoSpot.
        self.priority_strategy = priority_strategy
        # The region ID of the scaling group.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the scaling group.
        self.scaling_group_id = scaling_group_id
        # The IDs of the scaling groups that you want to query.
        self.scaling_group_ids = scaling_group_ids
        # The instance bidding policy. Valid values:
        # 
        # *   NoSpot: The instances are created as pay-as-you-go instances.
        # *   SpotWithPriceLimit: The instances are created as preemptible instances with a user-defined maximum hourly price.
        # *   SpotAsPriceGo: The instances are created as preemptible instances for which the market price at the time of purchase is used as the bid price.
        # 
        # Default value: NoSpot.
        self.spot_strategy = spot_strategy
        # The categories of the system disks. The categories of the system disks specified by this parameter overwrite the categories of the system disks specified in the scaling configuration. Valid values:
        # 
        # *   cloud: basic disk.
        # *   cloud_efficiency: ultra disk.
        # *   cloud_ssd: standard SSD.
        # *   cloud_essd: Enterprise SSD (ESSD).
        # 
        # >  If you do not specify the scaling group ID, you must specify this parameter.
        self.system_disk_categories = system_disk_categories
        # The vSwitch IDs.
        # 
        # >  If you do not specify the scaling group ID, you must specify this parameter.
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

