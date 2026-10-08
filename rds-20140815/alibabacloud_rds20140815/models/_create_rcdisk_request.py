# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rds20140815 import models as main_models
from darabonba.model import DaraModel

class CreateRCDiskRequest(DaraModel):
    def __init__(
        self,
        auto_pay: bool = None,
        auto_renew: bool = None,
        description: str = None,
        disk_category: str = None,
        disk_name: str = None,
        instance_charge_type: str = None,
        instance_id: str = None,
        performance_level: str = None,
        period: int = None,
        period_unit: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        size: int = None,
        snapshot_id: str = None,
        tag: List[main_models.CreateRCDiskRequestTag] = None,
        zone_id: str = None,
    ):
        # Specifies whether to enable automatic payment. Valid values:
        # 
        # - **true** (default): enables automatic payment. Make sure that your account balance is sufficient.
        # - **false**: generates an order without charging.
        # 
        # 
        # 
        # 
        # > If your payment method has insufficient balance, set this parameter to false. An unpaid order is generated, and you can log on to the ApsaraDB RDS console to complete the payment.
        # >
        self.auto_pay = auto_pay
        # Specifies whether to enable auto-renewal. This parameter is valid only when you create a subscription data cloud disk. Valid values:
        # - **true**: enables auto-renewal.
        # - **false**: disables auto-renewal.
        # 
        #  > If you purchase the cloud disk on a monthly basis, the auto-renewal epoch is one month.
        #  If you purchase the cloud disk on a yearly basis, the auto-renewal epoch is one year.
        self.auto_renew = auto_renew
        # The description of the cloud disk. The description must be 2 to 256 characters in length and cannot start with `http://` or `https://`.
        self.description = description
        # The category of the data cloud disk. Valid values:
        # 
        # - **cloud_efficiency**: ultra cloud disk.
        # - **cloud_ssd**: standard SSD.
        # - **cloud_essd**: ESSD.
        # - **cloud_auto** (default): premium performance disk.
        self.disk_category = disk_category
        # The name of the cloud disk. The name must be 2 to 128 characters in length and can contain characters that are categorized as letter in Unicode, including Chinese characters, English letters, and digits. The name can also contain colons (:), underscores (_), periods (.), and hyphens (-).
        self.disk_name = disk_name
        # The billing method. Valid values:
        # 
        # - **Postpaid**: pay-as-you-go. Cloud disks with this billing method do not need to be mounted to an instance. You can also mount them to an instance of any billing method during creation as needed.
        # - **Prepaid**: subscription. Cloud disks with this billing method must be mounted to a subscription instance. You must specify the **InstanceId** (instance ID) of a subscription instance.
        self.instance_charge_type = instance_charge_type
        # Instance ID of the instance to which the cloud disk is attached. If **InstanceChargeType** is set to **Prepaid** (subscription), you must specify instance ID of a subscription instance.
        self.instance_id = instance_id
        # The performance level (PL) of the ESSD cloud disk. Valid values:
        # 
        # - **PL0**: A single cloud disk can deliver up to 10,000 random read/write IOPS.
        # - **PL1** (default): A single cloud disk can deliver up to 50,000 random read/write IOPS.
        # - **PL2**: A single cloud disk can deliver up to 100,000 random read/write IOPS.
        # - **PL3**: A single cloud disk can deliver up to 1,000,000 random read/write IOPS.
        # 
        # For more information about how to select an ESSD performance level, see [ESSD cloud disk](https://help.aliyun.com/document_detail/2859916.html).
        self.performance_level = performance_level
        # A reserved parameter. You do not need to specify this parameter.
        self.period = period
        # A reserved parameter. You do not need to specify this parameter.
        self.period_unit = period_unit
        # The region ID. You can call the DescribeRegions operation to query region IDs.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The capacity size. Unit: GiB. You must specify a value for this parameter. Valid values:
        # 
        # - **cloud_efficiency**: 20 to 32,768.
        # - **cloud_ssd**: 20 to 32,768.
        # - **cloud_auto**: 1 to 65,536.
        # - **cloud_essd**: The valid value range depends on the value of **PerformanceLevel**.
        #   - PL0: 1 to 65,536.
        #   - PL1: 20 to 65,536.
        #   - PL2: 461 to 65,536.
        #   - PL3: 1,261 to 65,536.
        # 
        # If **SnapshotId** is specified and the capacity of the corresponding snapshot is greater than the value of **Size**, snapshot size of the created cloud disk is the same as the snapshot capacity. If the snapshot capacity is less than the value of **Size**, snapshot size of the created cloud disk is the value of **Size**.
        self.size = size
        # The snapshot that is used to create the cloud disk.
        # 
        # - RDS Custom snapshots and ECS snapshots (non-shared type) are supported.
        # - If the capacity of the snapshot specified by **SnapshotId** is greater than the value of **Size**, snapshot size of the created cloud disk is the same as the snapshot capacity. If the snapshot capacity is less than the value of **Size**, snapshot size of the created cloud disk is the value of **Size**.
        # - Creating elastic ephemeral disks from snapshots is not supported.
        # - Snapshots created on or before July 15, 2013 cannot be used to create cloud disks.
        self.snapshot_id = snapshot_id
        # The tags.
        self.tag = tag
        # The zone ID.
        # 
        # This parameter is required if the **InstanceId** parameter (the instance ID of the instance to which the cloud disk is mounted) is not specified.
        self.zone_id = zone_id

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
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay

        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew

        if self.description is not None:
            result['Description'] = self.description

        if self.disk_category is not None:
            result['DiskCategory'] = self.disk_category

        if self.disk_name is not None:
            result['DiskName'] = self.disk_name

        if self.instance_charge_type is not None:
            result['InstanceChargeType'] = self.instance_charge_type

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.performance_level is not None:
            result['PerformanceLevel'] = self.performance_level

        if self.period is not None:
            result['Period'] = self.period

        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.size is not None:
            result['Size'] = self.size

        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')

        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DiskCategory') is not None:
            self.disk_category = m.get('DiskCategory')

        if m.get('DiskName') is not None:
            self.disk_name = m.get('DiskName')

        if m.get('InstanceChargeType') is not None:
            self.instance_charge_type = m.get('InstanceChargeType')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('PerformanceLevel') is not None:
            self.performance_level = m.get('PerformanceLevel')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.CreateRCDiskRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class CreateRCDiskRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key. You can specify up to N tag keys at a time. Valid values of N: **1 to 20**. The tag key cannot be an empty string.
        self.key = key
        # The tag value that corresponds to the tag key. You can specify up to N tag values at a time. Valid values of N: **1** to **20**. The tag value can be an empty string.
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

