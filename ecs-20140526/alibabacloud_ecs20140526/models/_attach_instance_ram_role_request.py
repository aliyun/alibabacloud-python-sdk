# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AttachInstanceRamRoleRequest(DaraModel):
    def __init__(
        self,
        instance_ids: str = None,
        owner_id: int = None,
        policy: str = None,
        ram_role_name: str = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The instance ID array. Array length: 1 to 100.
        # 
        # This parameter is required.
        self.instance_ids = instance_ids
        self.owner_id = owner_id
        # The additional access policy. You can specify an additional access policy to further restrict the permissions of the RAM role. For more information, see [Overview of access policies](https://help.aliyun.com/document_detail/93732.html). Length: 1 to 1,024 characters.
        self.policy = policy
        # The name of the instance RAM role. You can call the RAM API [ListRoles](https://help.aliyun.com/document_detail/28713.html) to query the instance RAM roles that you have created.
        # 
        # This parameter is required.
        self.ram_role_name = ram_role_name
        # The region ID. You can call [DescribeRegions](https://help.aliyun.com/document_detail/25609.html) to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.policy is not None:
            result['Policy'] = self.policy

        if self.ram_role_name is not None:
            result['RamRoleName'] = self.ram_role_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Policy') is not None:
            self.policy = m.get('Policy')

        if m.get('RamRoleName') is not None:
            self.ram_role_name = m.get('RamRoleName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

