# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribePriceRequest(DaraModel):
    def __init__(
        self,
        amount: int = None,
        bandwidth: int = None,
        duration: int = None,
        group_desktop_count: int = None,
        instance_type: str = None,
        internet_charge_type: str = None,
        os_type: str = None,
        period: int = None,
        period_unit: str = None,
        promotion_id: str = None,
        region_id: str = None,
        reseller_owner_uid: int = None,
        resource_type: str = None,
        root_disk_category: str = None,
        root_disk_performance_level: str = None,
        root_disk_size_gib: int = None,
        user_disk_category: str = None,
        user_disk_performance_level: str = None,
        user_disk_size_gib: int = None,
    ):
        # The resource count. Default value: 1.
        self.amount = amount
        # The peak Internet bandwidth. Unit: Mbit/s.
        # 
        # - For pay-by-bandwidth, valid values are 10 to 1000.
        # - For pay-by-traffic, valid values are 10 to 200.
        self.bandwidth = bandwidth
        # The duration package type for monthly cloud desktop purchases. If ResourceType is set to DesktopMonthPackage, this parameter is required.
        self.duration = duration
        # The number of shared cloud desktops. Default value: 1.
        # 
        # > This parameter takes effect only when ResourceType is set to DesktopGroup.
        self.group_desktop_count = group_desktop_count
        # The resource specification.
        # 
        # - If ResourceType is set to Desktop, this parameter is required. You can call [DescribeDesktopTypes](~~DescribeDesktopTypes~~) to query available values (corresponding to the DesktopTypeId value).
        # 
        # - If ResourceType is set to DesktopGroup, set this parameter to `large`.
        # 
        # - If ResourceType is set to Bandwidth, you do not need to specify this parameter.
        self.instance_type = instance_type
        # The billing method of the Internet access package.
        self.internet_charge_type = internet_charge_type
        # The operating system type.
        self.os_type = os_type
        # The subscription duration. Valid values are determined by the PeriodUnit parameter.
        # 
        # - If PeriodUnit is set to Hour, the valid value is 1.
        # - If PeriodUnit is set to Month, valid values are 1, 2, 3, and 6.
        # - If PeriodUnit is set to Year, valid values are 1, 2, and 3.
        # 
        # Default value: 1.
        self.period = period
        # The billing cycle.
        self.period_unit = period_unit
        # The promotion ID.
        self.promotion_id = promotion_id
        # The region ID. You can call [DescribeRegions](~~DescribeRegions~~) to query the regions supported by Elastic Desktop Service.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The user ID for resource ownership in reseller mode. You do not need to specify this parameter in non-reseller mode.
        self.reseller_owner_uid = reseller_owner_uid
        # The resource type.
        self.resource_type = resource_type
        # The system cloud disk type.
        self.root_disk_category = root_disk_category
        # The performance level (PL) of the system cloud disk. You can set the disk performance level when the cloud desktop specification is set to Graphics or High Frequency. For more information about the differences between performance levels, see [ESSD cloud disks](https://help.aliyun.com/document_detail/122389.html).
        self.root_disk_performance_level = root_disk_performance_level
        # The system cloud disk size. Unit: GiB. If ResourceType is set to Desktop, this parameter is required.
        self.root_disk_size_gib = root_disk_size_gib
        # The data cloud disk type.
        self.user_disk_category = user_disk_category
        # The performance level (PL) of the data cloud disk. You can set the disk performance level when the cloud desktop specification is set to Graphics or High Frequency. For more information about the differences between performance levels, see [ESSD cloud disks](https://help.aliyun.com/document_detail/122389.html).
        self.user_disk_performance_level = user_disk_performance_level
        # The data cloud disk size. Unit: GiB.
        self.user_disk_size_gib = user_disk_size_gib

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.amount is not None:
            result['Amount'] = self.amount

        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.group_desktop_count is not None:
            result['GroupDesktopCount'] = self.group_desktop_count

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.internet_charge_type is not None:
            result['InternetChargeType'] = self.internet_charge_type

        if self.os_type is not None:
            result['OsType'] = self.os_type

        if self.period is not None:
            result['Period'] = self.period

        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit

        if self.promotion_id is not None:
            result['PromotionId'] = self.promotion_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.reseller_owner_uid is not None:
            result['ResellerOwnerUid'] = self.reseller_owner_uid

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.root_disk_category is not None:
            result['RootDiskCategory'] = self.root_disk_category

        if self.root_disk_performance_level is not None:
            result['RootDiskPerformanceLevel'] = self.root_disk_performance_level

        if self.root_disk_size_gib is not None:
            result['RootDiskSizeGib'] = self.root_disk_size_gib

        if self.user_disk_category is not None:
            result['UserDiskCategory'] = self.user_disk_category

        if self.user_disk_performance_level is not None:
            result['UserDiskPerformanceLevel'] = self.user_disk_performance_level

        if self.user_disk_size_gib is not None:
            result['UserDiskSizeGib'] = self.user_disk_size_gib

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')

        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('GroupDesktopCount') is not None:
            self.group_desktop_count = m.get('GroupDesktopCount')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('InternetChargeType') is not None:
            self.internet_charge_type = m.get('InternetChargeType')

        if m.get('OsType') is not None:
            self.os_type = m.get('OsType')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')

        if m.get('PromotionId') is not None:
            self.promotion_id = m.get('PromotionId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResellerOwnerUid') is not None:
            self.reseller_owner_uid = m.get('ResellerOwnerUid')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('RootDiskCategory') is not None:
            self.root_disk_category = m.get('RootDiskCategory')

        if m.get('RootDiskPerformanceLevel') is not None:
            self.root_disk_performance_level = m.get('RootDiskPerformanceLevel')

        if m.get('RootDiskSizeGib') is not None:
            self.root_disk_size_gib = m.get('RootDiskSizeGib')

        if m.get('UserDiskCategory') is not None:
            self.user_disk_category = m.get('UserDiskCategory')

        if m.get('UserDiskPerformanceLevel') is not None:
            self.user_disk_performance_level = m.get('UserDiskPerformanceLevel')

        if m.get('UserDiskSizeGib') is not None:
            self.user_disk_size_gib = m.get('UserDiskSizeGib')

        return self

