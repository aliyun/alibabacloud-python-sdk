# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class ModifyPrepayInstanceSpecRequest(DaraModel):
    def __init__(
        self,
        system_disk: main_models.ModifyPrepayInstanceSpecRequestSystemDisk = None,
        auto_pay: bool = None,
        client_token: str = None,
        disk: List[main_models.ModifyPrepayInstanceSpecRequestDisk] = None,
        end_time: str = None,
        instance_id: str = None,
        instance_type: str = None,
        migrate_across_zone: bool = None,
        modify_mode: str = None,
        operator_type: str = None,
        owner_account: str = None,
        owner_id: int = None,
        reboot_time: str = None,
        reboot_when_finished: bool = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.system_disk = system_disk
        # Specifies whether to automatically complete the payment when you upgrade the instance type. Valid values:
        # 
        # - true: The payment is automatically completed.
        # - false: Only an order is created. No payment is made.
        # 
        # Default value: true.
        # > - If automatic payment is enabled, make sure that your payment method has a sufficient balance. Otherwise, an abnormal order is generated, and you can only cancel the order.
        # > - If your payment method balance is insufficient, you can set `AutoPay` to `false` to generate an unpaid order. Then, you can logon to the ECS console to pay for the order.
        # > - When `OperatorType` is set to `downgrade`, the `AutoPay` parameter is ignored.
        self.auto_pay = auto_pay
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but make sure that the token is unique among different requests. The ClientToken value can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](https://help.aliyun.com/document_detail/25693.html).
        self.client_token = client_token
        # > This parameter is not publicly available.
        self.disk = disk
        # The end time of the temporary instance type change. Specify the time in the [ISO 8601](https://help.aliyun.com/document_detail/25696.html) standard in the yyyy-MM-ddTHH:mmZ format. The time must be in UTC.
        self.end_time = end_time
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The target instance type for the Upgrade/Downgrade. For more information, see [Instance family](https://help.aliyun.com/document_detail/25378.html) or invoke [DescribeInstanceTypes](https://help.aliyun.com/document_detail/25620.html).
        # 
        # This parameter is required.
        self.instance_type = instance_type
        # Specifies whether to support cross-cluster instance type changes. Valid values:
        # - true: supported.
        # - false: not supported.
        # 
        # Default value: false.
        # 
        # When the `MigrateAcrossZone` parameter is set to `true`, take note of the following items after you perform the optimization on the Elastic Compute Service instance based on the response:
        # 
        # VPC-type instances: For [retired instance types](https://help.aliyun.com/document_detail/55263.html), when a non-I/O optimized instance is changed to an I/O optimized instance, the disk device names and software authorization codes of the server change. For Linux instances, basic disks (cloud) are identified as xvda or xvdb. Ultra disks (cloud_efficiency) and standard SSDs (cloud_ssd) are identified as vda or vdb.
        self.migrate_across_zone = migrate_across_zone
        # > This parameter is not publicly available.
        self.modify_mode = modify_mode
        # The type of the operation. Valid values:
        # > This parameter is optional. The system can automatically determine whether the operation is an upgrade or a downgrade. If you upload this parameter, follow the rules below.
        # 
        # - upgrade: upgrades the instance type. Make sure that your account payment method has a sufficient balance.
        # 
        # - downgrade: decrease the quota of the instance type. When the instance type specified by `InstanceType` is lower than the current instance type, set `OperatorType` to `downgrade`.
        # 
        # > For precautions about upgrading or downgrading instance types, see the operation description section above.
        self.operator_type = operator_type
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The restart time of the instance. Specify the time in the [ISO 8601](https://help.aliyun.com/document_detail/25696.html) standard in the yyyy-MM-ddTHH:mmZ format. The time must be in UTC.
        self.reboot_time = reboot_time
        # Specifies whether to immediately restart the instance after the instance type change is complete. Valid values:
        # 
        # - true: The instance is immediately restarted.
        # - false: The instance is not restarted.
        # 
        # Default value: false.
        # 
        # > If the instance is in the **Stopped** state, the instance remains stopped even if you set `RebootWhenFinished` to `true`. No operation is performed.
        self.reboot_when_finished = reboot_when_finished
        # The region ID of the instance. You can call [DescribeRegions](https://help.aliyun.com/document_detail/25609.html) to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        if self.system_disk:
            self.system_disk.validate()
        if self.disk:
            for v1 in self.disk:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.system_disk is not None:
            result['SystemDisk'] = self.system_disk.to_map()

        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        result['Disk'] = []
        if self.disk is not None:
            for k1 in self.disk:
                result['Disk'].append(k1.to_map() if k1 else None)

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.migrate_across_zone is not None:
            result['MigrateAcrossZone'] = self.migrate_across_zone

        if self.modify_mode is not None:
            result['ModifyMode'] = self.modify_mode

        if self.operator_type is not None:
            result['OperatorType'] = self.operator_type

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.reboot_time is not None:
            result['RebootTime'] = self.reboot_time

        if self.reboot_when_finished is not None:
            result['RebootWhenFinished'] = self.reboot_when_finished

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SystemDisk') is not None:
            temp_model = main_models.ModifyPrepayInstanceSpecRequestSystemDisk()
            self.system_disk = temp_model.from_map(m.get('SystemDisk'))

        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        self.disk = []
        if m.get('Disk') is not None:
            for k1 in m.get('Disk'):
                temp_model = main_models.ModifyPrepayInstanceSpecRequestDisk()
                self.disk.append(temp_model.from_map(k1))

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('MigrateAcrossZone') is not None:
            self.migrate_across_zone = m.get('MigrateAcrossZone')

        if m.get('ModifyMode') is not None:
            self.modify_mode = m.get('ModifyMode')

        if m.get('OperatorType') is not None:
            self.operator_type = m.get('OperatorType')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RebootTime') is not None:
            self.reboot_time = m.get('RebootTime')

        if m.get('RebootWhenFinished') is not None:
            self.reboot_when_finished = m.get('RebootWhenFinished')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

class ModifyPrepayInstanceSpecRequestDisk(DaraModel):
    def __init__(
        self,
        category: str = None,
        disk_id: str = None,
        performance_level: str = None,
    ):
        # > This parameter is not publicly available.
        self.category = category
        # > This parameter is not publicly available.
        self.disk_id = disk_id
        # > This parameter is not publicly available.
        self.performance_level = performance_level

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['Category'] = self.category

        if self.disk_id is not None:
            result['DiskId'] = self.disk_id

        if self.performance_level is not None:
            result['PerformanceLevel'] = self.performance_level

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('DiskId') is not None:
            self.disk_id = m.get('DiskId')

        if m.get('PerformanceLevel') is not None:
            self.performance_level = m.get('PerformanceLevel')

        return self

class ModifyPrepayInstanceSpecRequestSystemDisk(DaraModel):
    def __init__(
        self,
        category: str = None,
    ):
        # The new system disk category. Valid values:
        # 
        # - cloud_efficiency: ultra disk.
        # - cloud_ssd: standard SSD.
        # > This parameter is valid only when you perform an Increase Quota from a [retired instance type](https://help.aliyun.com/document_detail/55263.html) to a [Normal instance family](https://help.aliyun.com/document_detail/25378.html) and change a non-I/O optimization instance to an I/O optimization instance.
        self.category = category

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['Category'] = self.category

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')

        return self

