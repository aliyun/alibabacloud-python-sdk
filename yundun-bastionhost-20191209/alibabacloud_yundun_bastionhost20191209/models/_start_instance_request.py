# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class StartInstanceRequest(DaraModel):
    def __init__(
        self,
        client_security_group_ids: List[str] = None,
        enable_portal_private_access: bool = None,
        instance_id: str = None,
        region_id: str = None,
        security_group_ids: List[str] = None,
        slave_vswitch_id: str = None,
        vswitch_id: str = None,
    ):
        self.client_security_group_ids = client_security_group_ids
        self.enable_portal_private_access = enable_portal_private_access
        # The ID of the bastion host that you want to enable.
        # 
        # > You can call the [DescribeInstances](https://help.aliyun.com/document_detail/153281.html) operation to query the ID of the bastion host.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The region ID of the bastion host.
        self.region_id = region_id
        # An array consisting of the IDs of security groups to which the bastion host is added.
        # 
        # This parameter is required.
        self.security_group_ids = security_group_ids
        self.slave_vswitch_id = slave_vswitch_id
        # The ID of the vSwitch to which the bastion host belongs.
        self.vswitch_id = vswitch_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_security_group_ids is not None:
            result['ClientSecurityGroupIds'] = self.client_security_group_ids

        if self.enable_portal_private_access is not None:
            result['EnablePortalPrivateAccess'] = self.enable_portal_private_access

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.security_group_ids is not None:
            result['SecurityGroupIds'] = self.security_group_ids

        if self.slave_vswitch_id is not None:
            result['SlaveVswitchId'] = self.slave_vswitch_id

        if self.vswitch_id is not None:
            result['VswitchId'] = self.vswitch_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientSecurityGroupIds') is not None:
            self.client_security_group_ids = m.get('ClientSecurityGroupIds')

        if m.get('EnablePortalPrivateAccess') is not None:
            self.enable_portal_private_access = m.get('EnablePortalPrivateAccess')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SecurityGroupIds') is not None:
            self.security_group_ids = m.get('SecurityGroupIds')

        if m.get('SlaveVswitchId') is not None:
            self.slave_vswitch_id = m.get('SlaveVswitchId')

        if m.get('VswitchId') is not None:
            self.vswitch_id = m.get('VswitchId')

        return self

