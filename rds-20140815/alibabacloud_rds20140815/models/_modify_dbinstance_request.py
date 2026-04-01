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
        self.auto_use_coupon = auto_use_coupon
        self.bursting_enabled = bursting_enabled
        self.category = category
        self.cold_data_enabled = cold_data_enabled
        self.dbinstance_class = dbinstance_class
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        self.dbinstance_storage = dbinstance_storage
        self.dbinstance_storage_type = dbinstance_storage_type
        self.dbnodes = dbnodes
        self.direction = direction
        self.effective_time = effective_time
        self.io_acceleration_enabled = io_acceleration_enabled
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.parameter_group_id = parameter_group_id
        self.parameters = parameters
        self.promotion_code = promotion_code
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.switch_time = switch_time
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
        self.node_id = node_id
        self.role = role
        self.v_switch_id = v_switch_id
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

