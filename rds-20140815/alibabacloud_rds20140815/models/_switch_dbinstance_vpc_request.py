# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SwitchDBInstanceVpcRequest(DaraModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        private_ip_address: str = None,
        resource_owner_id: int = None,
        vpcid: str = None,
        v_switch_id: str = None,
    ):
        # The instance ID. You can call DescribeDBInstances to query the instance ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The private IP address of the instance. The IP address must be within the CIDR block of the vSwitch specified by the **VSwitchId** parameter.
        # > You can call DescribeVSwitches to query the CIDR block of the target vSwitch.
        self.private_ip_address = private_ip_address
        self.resource_owner_id = resource_owner_id
        # The VPC ID.
        # 
        # > The VPC must be in the same region as the ApsaraDB RDS instance.
        # 
        # This parameter is required.
        self.vpcid = vpcid
        # The vSwitch ID.
        # 
        # > The vSwitch must be in the same zone as the ApsaraDB RDS instance.
        # 
        # This parameter is required.
        self.v_switch_id = v_switch_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.private_ip_address is not None:
            result['PrivateIpAddress'] = self.private_ip_address

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.vpcid is not None:
            result['VPCId'] = self.vpcid

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('PrivateIpAddress') is not None:
            self.private_ip_address = m.get('PrivateIpAddress')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('VPCId') is not None:
            self.vpcid = m.get('VPCId')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        return self

