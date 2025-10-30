# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyDBInstanceNetworkTypeRequest(DaraModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        instance_network_type: str = None,
        private_ip_address: str = None,
        vpcid: str = None,
        v_switch_id: str = None,
    ):
        # The instance ID.
        # 
        # > You can call the [DescribeDBInstances](https://help.aliyun.com/document_detail/86911.html) operation to query the information about all AnalyticDB for PostgreSQL instances within a region, including instance IDs.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The new network type of the instance. Valid values:
        # 
        # *   VPC
        # *   Classic
        # 
        # This parameter is required.
        self.instance_network_type = instance_network_type
        # The internal IP address of the instance.
        self.private_ip_address = private_ip_address
        # The virtual private cloud (VPC) ID of the instance.
        self.vpcid = vpcid
        # The vSwitch ID of the instance. This parameter must be specified when VPCId is specified.
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

        if self.instance_network_type is not None:
            result['InstanceNetworkType'] = self.instance_network_type

        if self.private_ip_address is not None:
            result['PrivateIpAddress'] = self.private_ip_address

        if self.vpcid is not None:
            result['VPCId'] = self.vpcid

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('InstanceNetworkType') is not None:
            self.instance_network_type = m.get('InstanceNetworkType')

        if m.get('PrivateIpAddress') is not None:
            self.private_ip_address = m.get('PrivateIpAddress')

        if m.get('VPCId') is not None:
            self.vpcid = m.get('VPCId')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        return self

