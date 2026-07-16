# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ehpc20240730 import models as main_models
from darabonba.model import DaraModel

class NodeTemplate(DaraModel):
    def __init__(
        self,
        auto_renew: bool = None,
        auto_renew_period: int = None,
        data_disks: List[main_models.NodeTemplateDataDisks] = None,
        duration: int = None,
        enable_ht: bool = None,
        image_id: str = None,
        instance_charge_type: str = None,
        instance_type: str = None,
        period: int = None,
        period_unit: str = None,
        spot_price_limit: float = None,
        spot_strategy: str = None,
        system_disk: main_models.NodeTemplateSystemDisk = None,
    ):
        # Specifies whether to enable auto-renewal. This parameter takes effect only when InstanceChargeType is set to PrePaid. Valid values:
        # 
        # *   true
        # *   false
        # 
        # Default value: false.
        self.auto_renew = auto_renew
        # The auto-renewal period. Valid values:
        # 
        # *   Valid values when PeriodUnit is set to Week: 1, 2, and 3
        # *   Valid values when PeriodUnit is set to Month: 1, 2, 3, 6, 12, 24, 36, 48, and 60
        # 
        # Default value: 1.
        self.auto_renew_period = auto_renew_period
        # The data disks.
        # 
        # >  You can specify up to 16 data disks.
        self.data_disks = data_disks
        # The protection period for the preemptible instance. Unit: hours. Default value: 1. Valid values:
        # 
        # *   1: After a preemptible instance is created, Alibaba Cloud ensures that the instance is not automatically released within one hour. After the one-hour protection period ends, the system compares the bid price with the market price and checks the resource inventory to determine whether to retain or release the instance.
        # *   0: After a preemptible instance is created, Alibaba Cloud does not ensure that the instance runs for one hour. The system compares the bid price with the market price and checks the resource inventory to determine whether to retain or release the instance.
        # 
        # Alibaba Cloud sends an ECS system event to notify you five minutes before the instance is released. The preemptible instance is billed by second. We recommend that you specify an appropriate protection period based on your business requirements.
        self.duration = duration
        # Specifies whether to enable hyper-threading for the node. Valid values:
        # 
        # *   true
        # *   false
        self.enable_ht = enable_ht
        # The ID of the image to be used for instance booting. You can call the [DescribeImages](https://help.aliyun.com/zh/ecs/developer-reference/api-ecs-2014-05-26-describeimages?spm=api-workbench.API%20Document.0.0.7e5caef0GBcMYX) operation to query the available image resources.
        self.image_id = image_id
        # The billing method. Valid values:
        # 
        # *   PrePaid: subscription
        # *   PostPaid: pay-as-you-go
        # 
        # Default value: PostPaid.
        # 
        # If you set this parameter to PrePaid, you must make sure that your account supports payment by balance or credit. Otherwise, the InvalidPayMethod error message will be returned.
        self.instance_charge_type = instance_charge_type
        # The ECS instance type.
        # 
        # *   To select an appropriate instance type, you can see [Instance families](https://help.aliyun.com/zh/ecs/user-guide/overview-of-instance-families?spm=api-workbench.API%20Document.0.0.7e5caef0GBcMYX) or call the [DescribeInstanceTypes](https://help.aliyun.com/zh/ecs/developer-reference/api-ecs-2014-05-26-describeinstancetypes?spm=api-workbench.API%20Document.0.0.7e5caef0GBcMYX) operation to learn the performance data about instance types.
        # *   To query the inventory of instance types in specified region or zone, you can call the [DescribeAvailableResource](https://help.aliyun.com/zh/ecs/developer-reference/api-ecs-2014-05-26-describeavailableresource?spm=api-workbench.API%20Document.0.0.7e5caef0GBcMYX) operation.
        self.instance_type = instance_type
        # The subscription period of the instance. The unit is specified by the PeriodUnit parameter. This parameter takes effect and is required only when InstanceChargeType is set to PrePaid. If the DedicatedHostId parameter is specified, the subscription duration of the instance must be no longer than that of the dedicated host. Valid values:
        # 
        # *   Valid values when PeriodUnit is set to Week: 1, 2, 3, and 4
        # *   Valid values when PeriodUnit is set to Month: 1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 24, 36, 48, and 60
        self.period = period
        # The unit of the subscription period. Valid values:
        # 
        # *   Week
        # *   Month (default)
        self.period_unit = period_unit
        # The maximum hourly price of the preemptible instance. This parameter takes effect only when SpotStrategy is set to SpotWithPriceLimit. A maximum of three decimal places can be specified.
        self.spot_price_limit = spot_price_limit
        # The bidding policy for the pay-as-you-go instance. This parameter is valid only when InstanceChargeType is set to PostPaid. Valid values:
        # 
        # *   NoSpot: The instance is created as a pay-as-you-go instance.
        # *   SpotWithPriceLimit: The instance is created as a preemptible instance with a user-defined maximum hourly price.
        # *   SpotAsPriceGo: The instance is created as a preemptible instance for which the market price at the time of purchase is automatically used as the bidding price.
        # 
        # Default value: NoSpot.
        self.spot_strategy = spot_strategy
        # The system disk configurations of the node.
        self.system_disk = system_disk

    def validate(self):
        if self.data_disks:
            for v1 in self.data_disks:
                 if v1:
                    v1.validate()
        if self.system_disk:
            self.system_disk.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew

        if self.auto_renew_period is not None:
            result['AutoRenewPeriod'] = self.auto_renew_period

        result['DataDisks'] = []
        if self.data_disks is not None:
            for k1 in self.data_disks:
                result['DataDisks'].append(k1.to_map() if k1 else None)

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.enable_ht is not None:
            result['EnableHT'] = self.enable_ht

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.instance_charge_type is not None:
            result['InstanceChargeType'] = self.instance_charge_type

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.period is not None:
            result['Period'] = self.period

        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit

        if self.spot_price_limit is not None:
            result['SpotPriceLimit'] = self.spot_price_limit

        if self.spot_strategy is not None:
            result['SpotStrategy'] = self.spot_strategy

        if self.system_disk is not None:
            result['SystemDisk'] = self.system_disk.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')

        if m.get('AutoRenewPeriod') is not None:
            self.auto_renew_period = m.get('AutoRenewPeriod')

        self.data_disks = []
        if m.get('DataDisks') is not None:
            for k1 in m.get('DataDisks'):
                temp_model = main_models.NodeTemplateDataDisks()
                self.data_disks.append(temp_model.from_map(k1))

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('EnableHT') is not None:
            self.enable_ht = m.get('EnableHT')

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('InstanceChargeType') is not None:
            self.instance_charge_type = m.get('InstanceChargeType')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')

        if m.get('SpotPriceLimit') is not None:
            self.spot_price_limit = m.get('SpotPriceLimit')

        if m.get('SpotStrategy') is not None:
            self.spot_strategy = m.get('SpotStrategy')

        if m.get('SystemDisk') is not None:
            temp_model = main_models.NodeTemplateSystemDisk()
            self.system_disk = temp_model.from_map(m.get('SystemDisk'))

        return self

class NodeTemplateSystemDisk(DaraModel):
    def __init__(
        self,
        category: str = None,
        level: str = None,
        size: int = None,
    ):
        # The category of the system disk. Valid values:
        # 
        # *   cloud_efficiency: utra disk
        # *   cloud_ssd: standard SSD
        # *   cloud_essd: Enterprise SSD (ESSD)
        # *   cloud: basic disk
        self.category = category
        # The performance level of the ESSD that is used as the system disk. Valid values:
        # 
        # *   PL0: A single ESSD can deliver up to 10,000 random read/write IOPS.
        # *   PL1 (default): A single ESSD can deliver up to 50,000 random read/write IOPS.
        # *   PL2: A single ESSD can deliver up to 100,000 random read/write IOPS.
        # *   PL3: A single ESSD can deliver up to 1,000,000 random read/write IOPS. For more information about ESSD performance levels, see [ESSDs](https://help.aliyun.com/zh/ecs/user-guide/essds?spm=api-workbench.API%20Document.0.0.7e5caef0GBcMYX).
        self.level = level
        # The disk size. Unit: GiB. Valid values:
        # 
        # *   cloud_efficiency: 40 to 32,768
        # 
        # *   cloud_ssd: 40 to 32,768
        # 
        # *   Valid values when Category is set to cloud_essd depends on the value of the DataDisk.N.PerformanceLevel parameter. Specifically:
        # 
        #     *   PL0: 40 to 65,536
        #     *   PL1: 40 to 65,536
        #     *   PL2: 461 to 65,536
        #     *   PL3: 1,261 to 65,536
        # 
        # *   cloud: 40 to 500
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['Category'] = self.category

        if self.level is not None:
            result['Level'] = self.level

        if self.size is not None:
            result['Size'] = self.size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('Level') is not None:
            self.level = m.get('Level')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        return self

class NodeTemplateDataDisks(DaraModel):
    def __init__(
        self,
        category: str = None,
        delete_with_instance: bool = None,
        device: str = None,
        level: str = None,
        mount_dir: str = None,
        size: int = None,
        snapshot_id: str = None,
    ):
        # The disk category. Valid values:
        # 
        # *   cloud_efficiency: utra disk
        # *   cloud_ssd: standard SSD
        # *   cloud_essd: ESSD
        self.category = category
        # Specifies whether to release data disk N when the instance is released. Valid values:
        # 
        # *   true
        # *   false
        # 
        # Default value: true.
        self.delete_with_instance = delete_with_instance
        # Device
        self.device = device
        # The performance level of the ESSD that is used as a data disk. Valid values:
        # 
        # *   PL0: A single ESSD can deliver up to 10,000 random read/write IOPS.
        # *   PL1 (default): A single ESSD can deliver up to 50,000 random read/write IOPS.
        # *   PL2: A single ESSD can deliver up to 100,000 random read/write IOPS.
        # *   PL3: A single ESSD can deliver up to 1,000,000 random read/write IOPS. For more information about ESSD performance levels, see [ESSDs](https://help.aliyun.com/zh/ecs/user-guide/essds?spm=api-workbench.API%20Document.0.0.7e5caef0GBcMYX).
        self.level = level
        # MountDir
        self.mount_dir = mount_dir
        # The disk size. Valid values of N: 1 to 16. Unit: GiB. Valid values:
        # 
        # *   cloud_efficiency: 40 to 32,768
        # 
        # *   cloud_ssd: 40 to 32,768
        # 
        # *   Valid values when Category is set to cloud_essd depends on the value of the DataDisk.N.PerformanceLevel parameter. Specifically:
        # 
        #     *   PL0: 40 to 65,536
        #     *   PL1: 40 to 65,536
        #     *   PL2: 461 to 65,536
        #     *   PL3: 1,261 to 65,536
        self.size = size
        # SnapshotId
        self.snapshot_id = snapshot_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['Category'] = self.category

        if self.delete_with_instance is not None:
            result['DeleteWithInstance'] = self.delete_with_instance

        if self.device is not None:
            result['Device'] = self.device

        if self.level is not None:
            result['Level'] = self.level

        if self.mount_dir is not None:
            result['MountDir'] = self.mount_dir

        if self.size is not None:
            result['Size'] = self.size

        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('DeleteWithInstance') is not None:
            self.delete_with_instance = m.get('DeleteWithInstance')

        if m.get('Device') is not None:
            self.device = m.get('Device')

        if m.get('Level') is not None:
            self.level = m.get('Level')

        if m.get('MountDir') is not None:
            self.mount_dir = m.get('MountDir')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')

        return self

