# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class AttachDBInstancesRequest(DaraModel):
    def __init__(
        self,
        attach_mode: str = None,
        client_token: str = None,
        dbinstances: List[str] = None,
        force_attach: bool = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        scaling_group_id: str = None,
        type: str = None,
    ):
        # The mode in which you want to attach the database to the scaling group. Valid values:
        # 
        # *   SecurityIp: adds the private IP addresses of scaled out ECS instances to the IP address whitelist of the database. Take note that you can choose this mode only when the database that you want to attach is an ApsaraDB RDS instance.
        # *   SecurityGroup: adds the security group of the scaling configuration based on which ECS instances are created in the scaling group to the security group whitelist of the database for registration.
        # 
        # Default value: SecurityIp.
        self.attach_mode = attach_mode
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must ensure that the value is unique among different requests.
        # 
        # The token can only contain ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure the idempotence of a request](https://help.aliyun.com/document_detail/25965.html).
        self.client_token = client_token
        # The IDs of the ApsaraDB RDS instances that you want to attach to the scaling group.
        # 
        # This parameter is required.
        self.dbinstances = dbinstances
        # Specifies whether to add the private IP addresses of all ECS instances in the scaling group to the IP address whitelist of the ApsaraDB RDS instance that you want to attach to the scaling group. Valid values:
        # 
        # *   true
        # *   false
        # 
        # Default value: false.
        self.force_attach = force_attach
        self.owner_id = owner_id
        # The region ID of the scaling group.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        # The ID of the scaling group.
        # 
        # This parameter is required.
        self.scaling_group_id = scaling_group_id
        # The type of the database that you want to attach to the scaling group. Valid values:
        # 
        # *   RDS
        # *   Redis
        # *   MongoDB
        # 
        # Default value: RDS.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attach_mode is not None:
            result['AttachMode'] = self.attach_mode

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.dbinstances is not None:
            result['DBInstances'] = self.dbinstances

        if self.force_attach is not None:
            result['ForceAttach'] = self.force_attach

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttachMode') is not None:
            self.attach_mode = m.get('AttachMode')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DBInstances') is not None:
            self.dbinstances = m.get('DBInstances')

        if m.get('ForceAttach') is not None:
            self.force_attach = m.get('ForceAttach')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

