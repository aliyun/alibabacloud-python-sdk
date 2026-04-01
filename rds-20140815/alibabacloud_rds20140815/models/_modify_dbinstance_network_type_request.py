# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyDBInstanceNetworkTypeRequest(DaraModel):
    def __init__(
        self,
        classic_expired_days: str = None,
        dbinstance_id: str = None,
        instance_network_type: str = None,
        owner_account: str = None,
        owner_id: int = None,
        private_ip_address: str = None,
        read_write_splitting_classic_expired_days: int = None,
        read_write_splitting_private_ip_address: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        retain_classic: str = None,
        vpcid: str = None,
        v_switch_id: str = None,
    ):
        # The number of days for which you want to retain the classic network endpoint. Valid values: **1 to 120**. Default value: **7**.
        # 
        # > If you set the **RetainClassic** parameter to **True**, you must also specify this parameter.
        self.classic_expired_days = classic_expired_days
        # The instance ID. You can call the DescribeDBInstances operation to query the instance ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The network type after the modification. Set the value to **VPC**.
        # 
        # This parameter is required.
        self.instance_network_type = instance_network_type
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The internal IP address of the instance. The internal IP address must be within the CIDR block supported by the specified vSwitch. The system automatically assigns a private IP address to an instance based on the values of **VPCId** and **VSwitchId**.
        self.private_ip_address = private_ip_address
        # The number of days for which you want to retain the read/write splitting endpoint of the classic network type. Valid values: **1 to 120**. Default value: **7**.
        # 
        # >  This parameter takes effect only when a read/write splitting endpoint of the classic network type exists and the **RetainClassic** parameter is set to **True**.
        self.read_write_splitting_classic_expired_days = read_write_splitting_classic_expired_days
        # The internal IP address that corresponds to the read/write splitting endpoint of the instance. The internal IP address must be within the CIDR block supported by the specified vSwitch. The system automatically assigns a private IP address to an instance based on the values of **VPCId** and **VSwitchId**.
        # 
        # >  This parameter is valid when a read/write splitting endpoint of the classic network type exists.
        self.read_write_splitting_private_ip_address = read_write_splitting_private_ip_address
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # Specifies whether to retain the classic network endpoint. Valid values:
        # 
        # *   **True**: retains the classic network endpoint.
        # *   **False** (default): does not retain the classic network endpoint.
        self.retain_classic = retain_classic
        # The VPC ID.
        self.vpcid = vpcid
        # The ID of the vSwitch. This parameter is required if the **VPCId** parameter is specified.
        self.v_switch_id = v_switch_id

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

        if self.instance_network_type is not None:
            result['InstanceNetworkType'] = self.instance_network_type

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.private_ip_address is not None:
            result['PrivateIpAddress'] = self.private_ip_address

        if self.read_write_splitting_classic_expired_days is not None:
            result['ReadWriteSplittingClassicExpiredDays'] = self.read_write_splitting_classic_expired_days

        if self.read_write_splitting_private_ip_address is not None:
            result['ReadWriteSplittingPrivateIpAddress'] = self.read_write_splitting_private_ip_address

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.retain_classic is not None:
            result['RetainClassic'] = self.retain_classic

        if self.vpcid is not None:
            result['VPCId'] = self.vpcid

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClassicExpiredDays') is not None:
            self.classic_expired_days = m.get('ClassicExpiredDays')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('InstanceNetworkType') is not None:
            self.instance_network_type = m.get('InstanceNetworkType')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PrivateIpAddress') is not None:
            self.private_ip_address = m.get('PrivateIpAddress')

        if m.get('ReadWriteSplittingClassicExpiredDays') is not None:
            self.read_write_splitting_classic_expired_days = m.get('ReadWriteSplittingClassicExpiredDays')

        if m.get('ReadWriteSplittingPrivateIpAddress') is not None:
            self.read_write_splitting_private_ip_address = m.get('ReadWriteSplittingPrivateIpAddress')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('RetainClassic') is not None:
            self.retain_classic = m.get('RetainClassic')

        if m.get('VPCId') is not None:
            self.vpcid = m.get('VPCId')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        return self

