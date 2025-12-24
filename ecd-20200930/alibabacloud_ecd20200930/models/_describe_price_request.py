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
        # The number of resources. Default value: 1.
        self.amount = amount
        # The maximum public bandwidth. Unit: Mbit/s.
        # 
        # *   Valid values if you set InternetChargeType to PayByBandwidth: 10 to 1000.
        # *   Valid values if you set InternetChargeType to InternetChargeType: 10 to 200.
        self.bandwidth = bandwidth
        # The type of hourly plan if you use the Monthly Subscription billing method. If you set `ResourceType` to `DesktopMonthPackage`, you must specify this parameter.
        # 
        # Valid values:
        # 
        # *   120: the 120-hour computing plan.
        # *   250: the 250-hour computing plan.
        self.duration = duration
        # The number of cloud computer shares. Default value: 1.
        # 
        # >  This parameter takes effect only if you set `ResourceType` to `DesktopGroup`.
        self.group_desktop_count = group_desktop_count
        # The specifications of the resource.
        # 
        # *   This parameter is required if you set `ResourceType` to `Desktop`. You can call the [DescribeDesktopTypes](~~DescribeDesktopTypes~~) to query the available cloud computer types that correspond to the value of `DesktopTypeId`.
        # *   If you set `ResourceType` to `DesktopGroup`, set the value of this parameter to `large`.
        # *   If you set `ResourceType` to `Bandwidth`, you can leave this parameter empty.
        self.instance_type = instance_type
        # The metering method for network traffic.
        # 
        # Valid values:
        # 
        # *   PayByTraffic: You are charged for the actually consumed traffic.
        # *   PayByBandwidth: You are charged by a fixed bandwidth.
        self.internet_charge_type = internet_charge_type
        # The OS type.
        # 
        # Valid values:
        # 
        # *   Linux
        # *   Windows (default)
        self.os_type = os_type
        # The subscription duration. The valid values of this parameter vary based on the value of `PeriodUnit`.
        # 
        # *   If you set `PeriodUnit` to `Hour`, set the value of this parameter to 1.
        # *   If you set `PeriodUnit` to `Month`, set the value of this parameter to 1, 2, 3, or 6.
        # *   If you set `PeriodUnit` to `Year`, set the value of this parameter to 1, 2, or 3.
        # 
        # Default value: 1.
        self.period = period
        # The billing cycle.
        # 
        # Valid values:
        # 
        # *   Month
        # *   Year
        # *   Hour (default)
        self.period_unit = period_unit
        # The promotion ID.
        self.promotion_id = promotion_id
        # The region ID. You can call the [DescribeRegions](~~DescribeRegions~~) operation to query the regions supported by EDS.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.reseller_owner_uid = reseller_owner_uid
        # The type of the resource.
        # 
        # Valid values:
        # 
        # *   DesktopMonthPackage: monthly subscription cloud computers that use hourly limit plans.
        # *   Desktop (default): pay-as-you-go cloud computers/monthly subscription cloud computers that use unlimited plans.
        # *   Bandwidth: premium bandwidth plans.
        # *   DesktopGroup: cloud computer shares.
        self.resource_type = resource_type
        # The category of the system disk.
        # 
        # Valid values:
        # 
        # *   cloud_efficiency: the ultra disk
        # *   cloud_auto: the standard SSD.
        # *   cloud_essd: the Enterprise SSD (ESSD). Take note that only specific cloud computer types support ESSDs.
        self.root_disk_category = root_disk_category
        self.root_disk_performance_level = root_disk_performance_level
        # The size of the system disk. Unit: GiB. If you set `ResourceType` to `Desktop`, you must specify this parameter.
        self.root_disk_size_gib = root_disk_size_gib
        # The category of the data disk.
        # 
        # Valid values:
        # 
        # *   cloud_efficiency: the ultra disk
        # *   cloud_auto: the standard SSD.
        # *   cloud_essd: the ESSD. Take note that only specific cloud computer types support ESSDs.
        self.user_disk_category = user_disk_category
        self.user_disk_performance_level = user_disk_performance_level
        # The size of the data disk. Unit: GiB.
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

