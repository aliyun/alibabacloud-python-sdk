# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class CreateDBEndpointAddressRequest(DaraModel):
    def __init__(
        self,
        connection_string_prefix: str = None,
        dbcluster_id: str = None,
        dbendpoint_id: str = None,
        net_type: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        security_group_id: str = None,
        vpcid: str = None,
        zone_info: List[main_models.CreateDBEndpointAddressRequestZoneInfo] = None,
    ):
        # The prefix of the new endpoint. The prefix of the endpoint must meet the following requirements:
        # 
        # *   The prefix can contain lowercase letters, digits, and hyphens (-).
        # *   The prefix must start with a letter and end with a digit or a letter.
        # *   The prefix must be 6 to 40 characters in length.
        self.connection_string_prefix = connection_string_prefix
        # The ID of the cluster.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The ID of the endpoint.
        # 
        # >  You can call the [DescribeDBClusterEndpoints](https://help.aliyun.com/document_detail/98205.html) operation to query endpoint details.
        # 
        # This parameter is required.
        self.dbendpoint_id = dbendpoint_id
        # The network type of the endpoint. Set the value to **Public**.
        # 
        # This parameter is required.
        self.net_type = net_type
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The ID of the ECS security group.
        self.security_group_id = security_group_id
        # The ID of the virtual private cloud (VPC).
        self.vpcid = vpcid
        # The details of the zones.
        self.zone_info = zone_info

    def validate(self):
        if self.zone_info:
            for v1 in self.zone_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.connection_string_prefix is not None:
            result['ConnectionStringPrefix'] = self.connection_string_prefix

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.dbendpoint_id is not None:
            result['DBEndpointId'] = self.dbendpoint_id

        if self.net_type is not None:
            result['NetType'] = self.net_type

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id

        if self.vpcid is not None:
            result['VPCId'] = self.vpcid

        result['ZoneInfo'] = []
        if self.zone_info is not None:
            for k1 in self.zone_info:
                result['ZoneInfo'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectionStringPrefix') is not None:
            self.connection_string_prefix = m.get('ConnectionStringPrefix')

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('DBEndpointId') is not None:
            self.dbendpoint_id = m.get('DBEndpointId')

        if m.get('NetType') is not None:
            self.net_type = m.get('NetType')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')

        if m.get('VPCId') is not None:
            self.vpcid = m.get('VPCId')

        self.zone_info = []
        if m.get('ZoneInfo') is not None:
            for k1 in m.get('ZoneInfo'):
                temp_model = main_models.CreateDBEndpointAddressRequestZoneInfo()
                self.zone_info.append(temp_model.from_map(k1))

        return self

class CreateDBEndpointAddressRequestZoneInfo(DaraModel):
    def __init__(
        self,
        v_switch_id: str = None,
        zone_id: str = None,
    ):
        # The ID of the vSwitch.
        self.v_switch_id = v_switch_id
        # The ID of the zone.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

