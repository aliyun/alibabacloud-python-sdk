# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DetachDBInstancesRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        dbinstances: List[str] = None,
        force_detach: bool = None,
        owner_id: int = None,
        region_id: str = None,
        remove_security_group: bool = None,
        resource_owner_account: str = None,
        scaling_group_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must ensure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [Ensure idempotence](https://help.aliyun.com/document_detail/25965.html).
        self.client_token = client_token
        # The IDs of the ApsaraDB RDS instances. You can remove up to five ApsaraDB RDS instances at a time.
        # 
        # This parameter is required.
        self.dbinstances = dbinstances
        # Specifies whether to remove the private IP addresses of the instances in the scaling group from the IP whitelist of the RDS instance. Valid values:
        # 
        # - true: removes the private IP addresses of the instances.
        # 
        # - false: does not remove the private IP addresses of the instances.
        # 
        # Default value: false.
        self.force_detach = force_detach
        self.owner_id = owner_id
        # The region ID of the scaling group.
        self.region_id = region_id
        # This parameter is valid only for databases whose `AttachMode` is set to `SecurityGroup`. Valid values:
        # 
        # - true: removes the security group ID that was added when the scaling group was associated with the database.
        # - false: retains the security group ID that was added when the scaling group was associated with the database.
        # 
        # Default value: false.
        self.remove_security_group = remove_security_group
        self.resource_owner_account = resource_owner_account
        # The ID of the scaling group.
        # 
        # This parameter is required.
        self.scaling_group_id = scaling_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.dbinstances is not None:
            result['DBInstances'] = self.dbinstances

        if self.force_detach is not None:
            result['ForceDetach'] = self.force_detach

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.remove_security_group is not None:
            result['RemoveSecurityGroup'] = self.remove_security_group

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DBInstances') is not None:
            self.dbinstances = m.get('DBInstances')

        if m.get('ForceDetach') is not None:
            self.force_detach = m.get('ForceDetach')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RemoveSecurityGroup') is not None:
            self.remove_security_group = m.get('RemoveSecurityGroup')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')

        return self

