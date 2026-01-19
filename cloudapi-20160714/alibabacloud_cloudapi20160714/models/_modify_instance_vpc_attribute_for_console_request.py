# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyInstanceVpcAttributeForConsoleRequest(DaraModel):
    def __init__(
        self,
        delete_vpc_access: bool = None,
        instance_id: str = None,
        token: str = None,
        vpc_id: str = None,
        vpc_owner_id: int = None,
        vswitch_id: str = None,
    ):
        # Whether delete instance client VPC.
        # - FALSE: set or modify instance client VPC
        # - TRUE: delete instance client VPC
        self.delete_vpc_access = delete_vpc_access
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The token of the request.
        self.token = token
        # The ID of the VPC.
        # 
        # This parameter is required.
        self.vpc_id = vpc_id
        # The ID of the Alibaba Cloud account to which the VPC belongs.
        self.vpc_owner_id = vpc_owner_id
        # The ID of the vSwitch.
        self.vswitch_id = vswitch_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.delete_vpc_access is not None:
            result['DeleteVpcAccess'] = self.delete_vpc_access

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.token is not None:
            result['Token'] = self.token

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.vpc_owner_id is not None:
            result['VpcOwnerId'] = self.vpc_owner_id

        if self.vswitch_id is not None:
            result['VswitchId'] = self.vswitch_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeleteVpcAccess') is not None:
            self.delete_vpc_access = m.get('DeleteVpcAccess')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Token') is not None:
            self.token = m.get('Token')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('VpcOwnerId') is not None:
            self.vpc_owner_id = m.get('VpcOwnerId')

        if m.get('VswitchId') is not None:
            self.vswitch_id = m.get('VswitchId')

        return self

