# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyDBInstanceNetworkTypeRequest(DaraModel):
    def __init__(
        self,
        classic_expired_days: int = None,
        dbinstance_id: str = None,
        network_type: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        retain_classic: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
        zone_id: str = None,
    ):
        # The retention period of the original classic network address when you switch the network type to VPC. Settings. Valid values: **14**, **30**, **60**, and **120**. Unit: days.
        # 
        # > This parameter is required when the **NetworkType** parameter settings is set to **VPC** and the **RetainClassic** parameter settings is set to **True**.
        self.classic_expired_days = classic_expired_days
        # The instance ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The target network type to which you want to switch the instance. Valid values:
        # - **VPC**: switches the network type to VPC.
        # 
        # This parameter is required.
        self.network_type = network_type
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # Specifies whether to retain the original classic network address when you switch the network type to VPC. Settings. Valid values:
        # - **True**: retains the original classic network address.
        # - **False**: does not retain the original classic network address.
        # 
        # > - This parameter is required when the **NetworkType** parameter settings is set to **VPC**.
        # > - If this parameter settings is set to **True**, you must also specify the **ClassicExpiredDays** parameter.
        self.retain_classic = retain_classic
        # The vSwitch ID in the VPC.
        # > This parameter is required when the **NetworkType** parameter settings is set to **VPC**.
        self.v_switch_id = v_switch_id
        # The VPC ID.
        # 
        # > This parameter is required when the **NetworkType** parameter settings is set to **VPC**.
        self.vpc_id = vpc_id
        # The zone ID. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/61933.html) operation to query the zone ID.
        # 
        # This parameter is required.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.classic_expired_days is not None:
            result['ClassicExpiredDays'] = self.classic_expired_days

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.network_type is not None:
            result['NetworkType'] = self.network_type

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.retain_classic is not None:
            result['RetainClassic'] = self.retain_classic

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClassicExpiredDays') is not None:
            self.classic_expired_days = m.get('ClassicExpiredDays')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('RetainClassic') is not None:
            self.retain_classic = m.get('RetainClassic')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

