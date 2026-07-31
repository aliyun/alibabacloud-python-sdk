# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ModifyInstanceVpcAttributeRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        private_ip_address: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        security_group_id: List[str] = None,
        v_switch_id: str = None,
        vpc_id: str = None,
    ):
        # The instance ID.
        # 
        # > When you call this operation, the ECS instance must be in the **Stopped** state. For other restrictions on the instance, carefully read the **operation description** section.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The new private IP address.
        # 
        # > The `PrivateIpAddress` parameter depends on `VSwitchId`. The specified IP address must be within the CIDR block of the vSwitch.
        # 
        # Default value: If this parameter is not specified, a private IP address is randomly assigned from the CIDR block of the vSwitch.
        self.private_ip_address = private_ip_address
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The IDs of the security groups to which the instance is added after the VPC is changed. This parameter is required only when the `VpcId` parameter is specified.
        # 
        # - The security groups must belong to the destination VPC.
        # - You can specify one or more security groups. The number of security groups is subject to the limits on the number of security groups to which an instance can belong. For more information, see [Limits](~~25412#SecurityGroupQuota1~~).
        # - All security groups in the list must be of the same type.
        # - Switching between security group types is supported. When you switch an ECS instance between security group types, make sure that you understand the differences in security group rule configurations between the two types to avoid impacts on instance networking. For more information, see [Security group overview](https://help.aliyun.com/document_detail/25387.html).
        self.security_group_id = security_group_id
        # The vSwitch ID.
        # 
        # - If the specified ID is the current vSwitch of the instance, the vSwitch remains unchanged.
        # - If the specified ID is a new vSwitch and the `VpcId` parameter is empty, the new and old vSwitches must belong to the same zone and the same VPC.
        # - If the `VpcId` parameter is not empty, the vSwitch specified by this parameter must belong to the specified VPC and must be in the same zone as the original vSwitch.
        # 
        # This parameter is required.
        self.v_switch_id = v_switch_id
        # The ID of the destination VPC.
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.private_ip_address is not None:
            result['PrivateIpAddress'] = self.private_ip_address

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PrivateIpAddress') is not None:
            self.private_ip_address = m.get('PrivateIpAddress')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

