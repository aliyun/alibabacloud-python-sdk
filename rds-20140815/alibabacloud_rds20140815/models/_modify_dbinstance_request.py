# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_rds20140815 import models as main_models
from darabonba.model import DaraModel

class ModifyDBInstanceRequest(DaraModel):
    def __init__(
        self,
        auto_use_coupon: bool = None,
        bursting_enabled: bool = None,
        category: str = None,
        cold_data_enabled: bool = None,
        dbinstance_class: str = None,
        dbinstance_id: str = None,
        dbinstance_storage: int = None,
        dbinstance_storage_type: str = None,
        dbnodes: List[main_models.ModifyDBInstanceRequestDBNodes] = None,
        direction: str = None,
        effective_time: str = None,
        io_acceleration_enabled: str = None,
        owner_account: str = None,
        owner_id: int = None,
        parameter_group_id: str = None,
        parameters: Dict[str, str] = None,
        promotion_code: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        switch_time: str = None,
        target_minor_version: str = None,
    ):
        # Specifies whether to automatically use coupons. Valid values:
        # * **true** (default): Automatically uses coupons.
        # * **false**: Does not automatically use coupons.
        # 
        # > After a coupon is used, the amount deducted by the coupon is not refunded if you downgrade the instance specifications.
        self.auto_use_coupon = auto_use_coupon
        # Specifies whether to enable the [I/O burst feature for premium performance disks](https://help.aliyun.com/document_detail/2340501.html). Valid values:
        # 
        # - **true**: Enabled.
        # - **false**: Disabled.
        self.bursting_enabled = bursting_enabled
        # The instance edition. Valid values:
        # 
        # - **Basic**: Basic Edition
        # - **HighAvailability**: High-availability Edition
        # - **cluster**: Cluster Edition
        self.category = category
        # <props="china">Specifies whether to enable the [cold data archiving feature](https://help.aliyun.com/document_detail/2701832.html) for general-purpose cloud disks. Valid values:
        # 
        # - <props="china">**true**: Enabled.
        # 
        # - <props="china">**false**: Disabled.
        # 
        # <props="intl">Reserved parameter.
        self.cold_data_enabled = cold_data_enabled
        # The instance type. For more information, see [Instance types](https://help.aliyun.com/document_detail/26312.html).
        self.dbinstance_class = dbinstance_class
        # The instance ID. You can call DescribeDBInstances to query the instance ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The [target storage capacity](https://help.aliyun.com/document_detail/26312.html), in GB. You can call the [DescribeAvailableClasses](https://help.aliyun.com/document_detail/610393.html) operation to query the available storage capacity range for the target instance type.
        # 
        # > * You must specify at least one of this parameter and the **DBInstanceClass** parameter.
        # > * You can call [DescribeDBInstanceAttribute](https://help.aliyun.com/document_detail/610394.html) to query the current storage capacity of the instance.
        self.dbinstance_storage = dbinstance_storage
        # The instance storage type. Valid values:
        # 
        # * **general_essd**: premium performance disk (recommended)
        # * **cloud_essd**: PL1 ESSD
        # * **cloud_essd2**: PL2 ESSD
        # * **cloud_essd3**: PL3 ESSD
        self.dbinstance_storage_type = dbinstance_storage_type
        # The node information.
        self.dbnodes = dbnodes
        # The type of specification change. Valid values:
        # 
        # - **Up** (default): Upgrades a subscription instance or upgrades/downgrades a pay-as-you-go instance.
        # - **Down**: Downgrades a subscription instance.
        self.direction = direction
        # The time when the new configurations take effect. Valid values:
        # > **Changing some configurations may affect the instance**. Read the impact section in the [feature documentation](https://help.aliyun.com/document_detail/96061.html) before you configure this parameter. Perform the operation during off-peak hours.
        # * **Immediate** (default): The new configurations take effect immediately.
        # * **MaintainTime**: The new configurations take effect during the [maintenance window](https://help.aliyun.com/document_detail/610402.html).
        # * **ScheduleTime**: The new configurations take effect at a specified time. The specified time must be at least 12 hours later than the current time. The actual switchover time follows the formula: EffectiveTime = ScheduleTime + SwitchTime.
        self.effective_time = effective_time
        # Specifies whether to enable the [Buffer Pool Extension (BPE) feature](https://help.aliyun.com/document_detail/2527067.html) for premium performance disks. Valid values:
        # 
        # - **1**: Enabled.
        # - **0**: Disabled.
        self.io_acceleration_enabled = io_acceleration_enabled
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The parameter template ID.
        self.parameter_group_id = parameter_group_id
        # The parameters and their values. All parameter values are of the STRING type. You can call DescribeParameterTemplates to query parameter names and values.
        # 
        # > If you specify the **ParameterGroupId** parameter and both the ParameterGroupId and Parameters parameters modify the same parameter, the modification specified by the Parameters parameter takes precedence.
        self.parameters = parameters
        # The coupon code.
        self.promotion_code = promotion_code
        # The name of the resource group.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The scheduled time for executing the parameter modification. The EffectiveTime parameter must be set to ScheduleTime. Format: <i>yyyy-MM-dd</i>T<i>HH:mm:ss</i>Z (UTC).
        # > The specified time must be later than the current time (the time when the call is made).
        self.switch_time = switch_time
        # The [minor engine version](https://help.aliyun.com/document_detail/126002.html) of the PostgreSQL instance. If the specification change fails because the current minor engine version is not supported, specify the minor engine version to **upgrade the minor engine version during the specification change**.
        # 
        # Format: `rds_postgres_<major version>00_<minor version>`. Example for version 12 with minor version 20200830: `rds_postgres_1200_20200830`.
        self.target_minor_version = target_minor_version

    def validate(self):
        if self.dbnodes:
            for v1 in self.dbnodes:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_use_coupon is not None:
            result['AutoUseCoupon'] = self.auto_use_coupon

        if self.bursting_enabled is not None:
            result['BurstingEnabled'] = self.bursting_enabled

        if self.category is not None:
            result['Category'] = self.category

        if self.cold_data_enabled is not None:
            result['ColdDataEnabled'] = self.cold_data_enabled

        if self.dbinstance_class is not None:
            result['DBInstanceClass'] = self.dbinstance_class

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.dbinstance_storage is not None:
            result['DBInstanceStorage'] = self.dbinstance_storage

        if self.dbinstance_storage_type is not None:
            result['DBInstanceStorageType'] = self.dbinstance_storage_type

        result['DBNodes'] = []
        if self.dbnodes is not None:
            for k1 in self.dbnodes:
                result['DBNodes'].append(k1.to_map() if k1 else None)

        if self.direction is not None:
            result['Direction'] = self.direction

        if self.effective_time is not None:
            result['EffectiveTime'] = self.effective_time

        if self.io_acceleration_enabled is not None:
            result['IoAccelerationEnabled'] = self.io_acceleration_enabled

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.parameter_group_id is not None:
            result['ParameterGroupId'] = self.parameter_group_id

        if self.parameters is not None:
            result['Parameters'] = self.parameters

        if self.promotion_code is not None:
            result['PromotionCode'] = self.promotion_code

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.switch_time is not None:
            result['SwitchTime'] = self.switch_time

        if self.target_minor_version is not None:
            result['TargetMinorVersion'] = self.target_minor_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoUseCoupon') is not None:
            self.auto_use_coupon = m.get('AutoUseCoupon')

        if m.get('BurstingEnabled') is not None:
            self.bursting_enabled = m.get('BurstingEnabled')

        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('ColdDataEnabled') is not None:
            self.cold_data_enabled = m.get('ColdDataEnabled')

        if m.get('DBInstanceClass') is not None:
            self.dbinstance_class = m.get('DBInstanceClass')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('DBInstanceStorage') is not None:
            self.dbinstance_storage = m.get('DBInstanceStorage')

        if m.get('DBInstanceStorageType') is not None:
            self.dbinstance_storage_type = m.get('DBInstanceStorageType')

        self.dbnodes = []
        if m.get('DBNodes') is not None:
            for k1 in m.get('DBNodes'):
                temp_model = main_models.ModifyDBInstanceRequestDBNodes()
                self.dbnodes.append(temp_model.from_map(k1))

        if m.get('Direction') is not None:
            self.direction = m.get('Direction')

        if m.get('EffectiveTime') is not None:
            self.effective_time = m.get('EffectiveTime')

        if m.get('IoAccelerationEnabled') is not None:
            self.io_acceleration_enabled = m.get('IoAccelerationEnabled')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ParameterGroupId') is not None:
            self.parameter_group_id = m.get('ParameterGroupId')

        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')

        if m.get('PromotionCode') is not None:
            self.promotion_code = m.get('PromotionCode')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SwitchTime') is not None:
            self.switch_time = m.get('SwitchTime')

        if m.get('TargetMinorVersion') is not None:
            self.target_minor_version = m.get('TargetMinorVersion')

        return self

class ModifyDBInstanceRequestDBNodes(DaraModel):
    def __init__(
        self,
        node_id: str = None,
        role: str = None,
        v_switch_id: str = None,
        zone_id: str = None,
    ):
        # The unique identifier of the node, which is used to specify a node.
        # > This parameter is valid only for Cluster Edition instances.
        self.node_id = node_id
        # The node type. Valid values:
        # * **Master**: primary node.
        # * **Slave**: secondary node.
        # 
        # > For Cluster Edition instances, you can leave this parameter empty and specify the NodeId parameter to identify the node.
        self.role = role
        # The vSwitch ID of the instance.
        self.v_switch_id = v_switch_id
        # The zone ID.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.role is not None:
            result['Role'] = self.role

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('Role') is not None:
            self.role = m.get('Role')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

