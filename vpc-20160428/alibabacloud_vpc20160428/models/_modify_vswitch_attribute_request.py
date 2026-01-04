# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyVSwitchAttributeRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        enable_ipv_6: bool = None,
        ipv_6cidr_block: int = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        v_switch_id: str = None,
        v_switch_name: str = None,
        vpc_ipv_6cidr_block: str = None,
    ):
        # The new description for the vSwitch.
        # 
        # The description must be 1 to 256 characters in length and cannot start with `http://` or `https://`.
        self.description = description
        # Specifies whether to enable the IPv6 feature for the vSwitch. Valid values:
        # 
        # *   **true**: enables the IPv6 feature.
        # *   **false**: disables the IPv6 feature. This is the default value.
        self.enable_ipv_6 = enable_ipv_6
        # The last eight bits of the IPv6 CIDR block of the vSwitch. Valid values: **0** to **255**.
        # 
        # You can set this parameter only when the IPv6 feature is enabled for the virtual private cloud (VPC) to which the vSwitch belongs.
        self.ipv_6cidr_block = ipv_6cidr_block
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The ID of the region where the vSwitch is deployed. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to query the most recent region list.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The ID of the vSwitch.
        # 
        # This parameter is required.
        self.v_switch_id = v_switch_id
        # The new name for the vSwitch.
        # 
        # The name must be 1 to 128 characters in length, and cannot start with `http://` or `https://`.
        self.v_switch_name = v_switch_name
        # The IPv6 CIDR block of the VPC to which the vSwitch belongs.
        # 
        # You can set this parameter only when the IPv6 feature is enabled for the VPC.
        self.vpc_ipv_6cidr_block = vpc_ipv_6cidr_block

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.enable_ipv_6 is not None:
            result['EnableIPv6'] = self.enable_ipv_6

        if self.ipv_6cidr_block is not None:
            result['Ipv6CidrBlock'] = self.ipv_6cidr_block

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.v_switch_name is not None:
            result['VSwitchName'] = self.v_switch_name

        if self.vpc_ipv_6cidr_block is not None:
            result['VpcIpv6CidrBlock'] = self.vpc_ipv_6cidr_block

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EnableIPv6') is not None:
            self.enable_ipv_6 = m.get('EnableIPv6')

        if m.get('Ipv6CidrBlock') is not None:
            self.ipv_6cidr_block = m.get('Ipv6CidrBlock')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VSwitchName') is not None:
            self.v_switch_name = m.get('VSwitchName')

        if m.get('VpcIpv6CidrBlock') is not None:
            self.vpc_ipv_6cidr_block = m.get('VpcIpv6CidrBlock')

        return self

