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
        # The ID of the ECS instance.
        # 
        # >  When you call this operation, the ECS instance must be in the **Stopped** (`Stopped`) state. For other limits on the ECS instance, see the **Usage notes** section of this topic.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The new private IP address of the ECS instance.
        # 
        # >  The value of `PrivateIpAddress` depends on the value of `VSwitchId`. The specified IP address must be within the CIDR block of the specified vSwitch.
        # 
        # By default, if this parameter is empty, a private IP address is randomly assigned from the CIDR block of the specified vSwitch.
        self.private_ip_address = private_ip_address
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The IDs of new security groups to which the ECS instance belongs after the VPC is changed. This parameter is required only if `VpcId` is specified.
        # 
        # *   The security groups that you specify must belong to the new VPC.
        # *   You can specify one or more security groups. The valid values of N vary based on the maximum number of security groups to which an ECS instance can belong. For more information, see [Limits](~~25412#SecurityGroupQuota1~~).
        # *   The specified security groups must be of the same type.
        # *   You can switch the ECS instance to security groups of a different type. To ensure network connectivity, we recommend that you understand the differences in rule configurations of the two security group types before you switch the ECS instance to security groups of a different type. For more information, see [Overview of security groups](https://help.aliyun.com/document_detail/25387.html).
        self.security_group_id = security_group_id
        # The ID of the new vSwitch.
        # 
        # *   If you set this parameter to the ID of the current vSwitch, the vSwitch of the ECS instance remains unchanged.
        # *   If you set this parameter to the ID of a different vSwitch and leave `VpcId` empty, the new vSwitch must belong to the same zone and VPC as the current vSwitch.
        # *   If you specify `VpcId`, the vSwitch specified by this parameter must belong to the specified VPC and the same zone as the current vSwitch.
        # 
        # This parameter is required.
        self.v_switch_id = v_switch_id
        # The ID of the new VPC.
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

