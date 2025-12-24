# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecd20200930 import models as main_models
from darabonba.model import DaraModel

class ModifyDesktopSpecRequest(DaraModel):
    def __init__(
        self,
        auto_pay: bool = None,
        desktop_id: str = None,
        desktop_type: str = None,
        promotion_id: str = None,
        region_id: str = None,
        reseller_owner_uid: int = None,
        resource_specs: List[main_models.ModifyDesktopSpecRequestResourceSpecs] = None,
        resource_type: str = None,
        root_disk_size_gib: int = None,
        user_disk_performance_level: str = None,
        user_disk_size_gib: int = None,
    ):
        # Specifies whether to enable the auto-payment feature.
        # 
        # Default value: true. Valid values:
        # 
        # *   true: enables the auto-payment feature.
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     Make sure that you have sufficient balance in your Alibaba Cloud account. Otherwise, an exception occurs on your order.
        # 
        #     <!-- -->
        # 
        # *   false: disables the auto-payment feature. In this case, an order is generated, and no payment is automatically made.
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     You can log on to the Elastic Desktop Service console and complete the payment based on the order ID on the Orders page.
        # 
        #     <!-- -->
        self.auto_pay = auto_pay
        # The ID of a cloud computer.
        self.desktop_id = desktop_id
        # The destination instance type. You can call the [DescribeDesktopTypes](https://help.aliyun.com/document_detail/188882.html) operation to query the instance types supported by cloud computers.
        # 
        # This parameter is required.
        self.desktop_type = desktop_type
        # The ID of the promotional activity.
        self.promotion_id = promotion_id
        # The region ID. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/196646.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.reseller_owner_uid = reseller_owner_uid
        # The array of resource specification templates.
        self.resource_specs = resource_specs
        # The resource type.
        # 
        # > This parameter is optional for non-subscribed cloud computers.
        self.resource_type = resource_type
        # The size of the new system disk. Unit: GiB. Valid values: 80 to 500 GiB. The value must be a multiple of 10.
        self.root_disk_size_gib = root_disk_size_gib
        # The performance level (PL) of the data disk. Default value: PL0.
        # 
        # Valid values:
        # 
        # *   PL1
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   PL0
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   PL3
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   PL2
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.user_disk_performance_level = user_disk_performance_level
        # The destination data disk size. Unit: GiB.
        # 
        # *   The data disk size of a non-graphical cloud computer ranges from 20 to 1020 GiB and must be a multiple of 10.
        # *   The data disk size of a graphical cloud computer ranges from 40 to 1020 GiB and must be a multiple of 10.
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
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay

        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id

        if self.desktop_type is not None:
            result['DesktopType'] = self.desktop_type

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

        if self.root_disk_size_gib is not None:
            result['RootDiskSizeGib'] = self.root_disk_size_gib

        if self.user_disk_performance_level is not None:
            result['UserDiskPerformanceLevel'] = self.user_disk_performance_level

        if self.user_disk_size_gib is not None:
            result['UserDiskSizeGib'] = self.user_disk_size_gib

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')

        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')

        if m.get('DesktopType') is not None:
            self.desktop_type = m.get('DesktopType')

        if m.get('PromotionId') is not None:
            self.promotion_id = m.get('PromotionId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResellerOwnerUid') is not None:
            self.reseller_owner_uid = m.get('ResellerOwnerUid')

        self.resource_specs = []
        if m.get('ResourceSpecs') is not None:
            for k1 in m.get('ResourceSpecs'):
                temp_model = main_models.ModifyDesktopSpecRequestResourceSpecs()
                self.resource_specs.append(temp_model.from_map(k1))

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('RootDiskSizeGib') is not None:
            self.root_disk_size_gib = m.get('RootDiskSizeGib')

        if m.get('UserDiskPerformanceLevel') is not None:
            self.user_disk_performance_level = m.get('UserDiskPerformanceLevel')

        if m.get('UserDiskSizeGib') is not None:
            self.user_disk_size_gib = m.get('UserDiskSizeGib')

        return self

class ModifyDesktopSpecRequestResourceSpecs(DaraModel):
    def __init__(
        self,
        desktop_id: str = None,
        root_disk_size_gib: int = None,
        user_disk_size_gib: int = None,
    ):
        # The ID of the cloud computer.
        self.desktop_id = desktop_id
        # The target size of the system disk. Valid values: 80-500 GiB. The value must be a multiple of 10.
        self.root_disk_size_gib = root_disk_size_gib
        # The target size of the data disk. Valid values: 80-500 GiB. The value must be a multiple of 10.
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

