# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecd20200930 import models as main_models
from darabonba.model import DaraModel

class DescribeModificationPriceRequest(DaraModel):
    def __init__(
        self,
        bandwidth: int = None,
        instance_id: str = None,
        instance_type: str = None,
        promotion_id: str = None,
        region_id: str = None,
        reseller_owner_uid: int = None,
        resource_specs: List[main_models.DescribeModificationPriceRequestResourceSpecs] = None,
        resource_type: str = None,
        root_disk_performance_level: str = None,
        root_disk_size_gib: int = None,
        user_disk_performance_level: str = None,
        user_disk_size_gib: int = None,
    ):
        # The peak Internet bandwidth. Unit: Mbit/s.
        # 
        # > If you use the pay-by-bandwidth billing method, the valid values range from 10 to 1000.
        self.bandwidth = bandwidth
        # The instance ID. The value can be the ID of a monthly-subscribed (unlimited-duration) cloud computer or the ID of a premium Internet bandwidth instance.
        self.instance_id = instance_id
        # The resource specification.
        # 
        # - If `ResourceType` is set to `Desktop`, valid values include:
        #     - ecd.basic.small
        #     - ecd.basic.large
        #     - ecd.advanced.large
        #     - ecd.advanced.xlarge
        #     - ecd.performance.2xlarge
        #     - ecd.graphics.xlarge
        #     - ecd.graphics.2xlarge
        #     - ecd.advanced.xlarge_s8d2
        #     - ecd.advanced.xlarge_s8d7
        #     - ecd.graphics.1g72c
        #     - eds.general.2c2g
        #     - eds.general.2c4g
        #     - eds.general.2c8g
        #     - eds.general.4c8g
        #     - eds.general.4c16g
        #     - eds.general.8c16g
        #     - eds.general.8c32g
        #     - eds.general.16c32g
        # 
        # - If `ResourceType` is set to `NetworkPackage`, you do not need to specify this parameter.
        self.instance_type = instance_type
        # The promotion ID.
        self.promotion_id = promotion_id
        # The region ID. You can call [DescribeRegions](~~DescribeRegions~~) to query the regions supported by Elastic Desktop Service.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The user ID for resource ownership in the reseller pattern. You do not need to specify this parameter in non-reseller pattern.
        self.reseller_owner_uid = reseller_owner_uid
        # The list of resource specification templates.
        self.resource_specs = resource_specs
        # The resource type. The required parameters vary based on the resource type for which you want to query the specification change price:
        # 
        # - If `ResourceType` is set to `Desktop`, you must specify the `InstanceType`, `RootDiskSizeGib`, and `UserDiskSizeGib` parameters.
        # - If `ResourceType` is set to `NetworkPackage`, you must specify the `Bandwidth` parameter.
        self.resource_type = resource_type
        # The performance level of the system cloud disk. You can configure the disk performance level in Settings when the cloud computer specification is set to graphics-accelerated or high frequency. For more information about the differences between performance levels, see [ESSDs](https://help.aliyun.com/document_detail/122389.html). standard SSD does not support performance level configuration.
        self.root_disk_performance_level = root_disk_performance_level
        # The system cloud disk size. Unit: GiB.
        self.root_disk_size_gib = root_disk_size_gib
        # The performance level of the data cloud disk. You can configure the disk performance level in Settings when the cloud computer specification is set to graphics-accelerated or high frequency. For more information about the differences between performance levels, see [ESSDs](https://help.aliyun.com/document_detail/122389.html). standard SSD does not support performance level configuration.
        self.user_disk_performance_level = user_disk_performance_level
        # The data cloud disk size. Unit: GiB.
        self.user_disk_size_gib = user_disk_size_gib

    def validate(self):
        if self.resource_specs:
            for v1 in self.resource_specs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.promotion_id is not None:
            result['PromotionId'] = self.promotion_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.reseller_owner_uid is not None:
            result['ResellerOwnerUid'] = self.reseller_owner_uid

        result['ResourceSpecs'] = []
        if self.resource_specs is not None:
            for k1 in self.resource_specs:
                result['ResourceSpecs'].append(k1.to_map() if k1 else None)

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.root_disk_performance_level is not None:
            result['RootDiskPerformanceLevel'] = self.root_disk_performance_level

        if self.root_disk_size_gib is not None:
            result['RootDiskSizeGib'] = self.root_disk_size_gib

        if self.user_disk_performance_level is not None:
            result['UserDiskPerformanceLevel'] = self.user_disk_performance_level

        if self.user_disk_size_gib is not None:
            result['UserDiskSizeGib'] = self.user_disk_size_gib

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('PromotionId') is not None:
            self.promotion_id = m.get('PromotionId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResellerOwnerUid') is not None:
            self.reseller_owner_uid = m.get('ResellerOwnerUid')

        self.resource_specs = []
        if m.get('ResourceSpecs') is not None:
            for k1 in m.get('ResourceSpecs'):
                temp_model = main_models.DescribeModificationPriceRequestResourceSpecs()
                self.resource_specs.append(temp_model.from_map(k1))

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('RootDiskPerformanceLevel') is not None:
            self.root_disk_performance_level = m.get('RootDiskPerformanceLevel')

        if m.get('RootDiskSizeGib') is not None:
            self.root_disk_size_gib = m.get('RootDiskSizeGib')

        if m.get('UserDiskPerformanceLevel') is not None:
            self.user_disk_performance_level = m.get('UserDiskPerformanceLevel')

        if m.get('UserDiskSizeGib') is not None:
            self.user_disk_size_gib = m.get('UserDiskSizeGib')

        return self

class DescribeModificationPriceRequestResourceSpecs(DaraModel):
    def __init__(
        self,
        desktop_id: str = None,
        root_disk_size_gib: int = None,
        user_disk_size_gib: int = None,
    ):
        # The cloud computer ID.
        self.desktop_id = desktop_id
        # The system cloud disk size. Unit: GiB.
        self.root_disk_size_gib = root_disk_size_gib
        # The data cloud disk size. Unit: GiB.
        self.user_disk_size_gib = user_disk_size_gib

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id

        if self.root_disk_size_gib is not None:
            result['RootDiskSizeGib'] = self.root_disk_size_gib

        if self.user_disk_size_gib is not None:
            result['UserDiskSizeGib'] = self.user_disk_size_gib

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')

        if m.get('RootDiskSizeGib') is not None:
            self.root_disk_size_gib = m.get('RootDiskSizeGib')

        if m.get('UserDiskSizeGib') is not None:
            self.user_disk_size_gib = m.get('UserDiskSizeGib')

        return self

