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
        # *   **true** (default): enables automatic payment. Make sure that your account balance is sufficient.
        # *   **false**: does not automatically complete the payment. An unpaid order is generated.
        # 
        # >  If your account balance is insufficient, you can set the parameter to false. In this case, an unpaid order is generated. You can complete the payment in the Expenses and Costs console.
        self.auto_pay = auto_pay
        # Specifies whether to enable auto-renewal. You must specify this parameter only when the data disk uses the subscription billing method. Valid values:
        # 
        # *   **true**
        # *   **false**
        # 
        # >  The auto-renewal cycle is one month for a monthly subscription. The auto-renewal cycle is one year for a yearly subscription.
        self.auto_renew = auto_renew
        # The disk description. The description must be 2 to 256 characters in length and cannot start with `http://` or `https://`.
        self.description = description
        # The data disk type. Valid values:
        # 
        # *   **cloud_efficiency**: ultra disk.
        # *   **cloud_ssd**: standard SSD
        # *   **cloud_essd**: ESSD
        # *   **cloud_auto** (default): Premium ESSD
        self.disk_category = disk_category
        # The name of the data disk. The name must be 2 to 128 characters in length and can contain letters and digits. The name can contain colons (:), underscores (_), periods (.), and hyphens (-).
        self.disk_name = disk_name
        # The billing method. Valid values:
        # 
        # *   **Postpaid**: pay-as-you-go Pay-as-you-go disks do not require to be attached. You can also attach the pay-as-you-go disk to an instance of any billing method based on your business requirements.
        # *   **Prepaid**: subscription Subscription disks must be attached to a subscription instance. Set **InstanceId** to the ID of a subscription instance.
        self.instance_charge_type = instance_charge_type
        # The ID of the instance to which you want to attach the disk. If you set **InstanceChargeType** to **Prepaid**, you must set InstanceId to the ID of a subscription instance.
        self.instance_id = instance_id
        # The performance level (PL) of ESSDs. Valid values:
        # 
        # *   **PL0**: A single ESSD delivers up to 10,000 random read/write IOPS.
        # *   **PL1: An ESSD delivers up to 50,000 random read/write IOPS.**
        # *   **PL2**: A single ESSD delivers up to 100,000 random read/write IOPS.
        # *   **PL3**: A single ESSD delivers up to 1,000,000 random read/write IOPS.
        # 
        # For information about ESSD PLs, see [ESSDs](https://help.aliyun.com/document_detail/2859916.html).
        self.performance_level = performance_level
        # A reserved parameter. You do not need to specify this parameter.
        self.period = period
        # A reserved parameter. You do not need to specify this parameter.
        self.period_unit = period_unit
        # The region ID. You can call the DescribeRegions operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The disk size. Unit: GiB. This parameter is required. Valid values:
        # 
        # *   Valid values if you set DiskCategory to **cloud_efficiency**: 20 to 32768.
        # 
        # *   Valid values if you set DiskCategory to **cloud_ssd**: 20 to 32768.
        # 
        # *   Valid values if you set DiskCategory to **cloud_auto**: 1 to 65536.
        # 
        # *   Valid values when DiskCategory is set to cloud_essd: depending on the value of **PerformanceLevel**.****
        # 
        #     *   Valid values if PerformanceLevel is set to PL0: 1 to 65536
        #     *   Valid values if PerformanceLevel is set to PL1: 20 to 65536
        #     *   Valid values if PerformanceLevel is set to PL2: 461 to 65536
        #     *   Valid values if PerformanceLevel is set to PL3: 1261 to 65536
        # 
        # If **SnapshotId** is specified and the size of the corresponding snapshot is greater than the **Size** value, the size of the created disk is the same as that of the snapshot. If the snapshot size is less than the **Size** value, the size of the created disk is equal to the **Size** value.
        self.size = size
        # The snapshot that you want to use to create the disk.
        # 
        # *   The snapshots of RDS Custom instances and the non-shared snapshots of ECS instances are supported.
        # *   If the size of the snapshot specified by **SnapshotId** is greater than the value of **Size**, the size of the created disk is equal to the specified snapshot size. If the snapshot size is less than the **Size** value, the size of the created disk is equal to the **Size** value.
        # *   You cannot create elastic ephemeral disks from snapshots.
        # *   Snapshots that were created on or before July 15, 2013 cannot be used to create disks.
        self.snapshot_id = snapshot_id
        # The list of tags.
        self.tag = tag
        # The zone ID.
        # 
        # This parameter is required if you do not specify **InstanceId**.
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
        # The tag key. You can create N tag keys at a time. Valid values of N: **1 to 20**. The tag key cannot be an empty string.
        self.key = key
        # The tag value. You can query N values at a time. Valid values of N: **1** to **20**. The tag value can be an empty string.
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

