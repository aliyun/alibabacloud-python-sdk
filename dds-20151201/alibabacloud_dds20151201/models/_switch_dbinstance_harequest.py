# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SwitchDBInstanceHARequest(DaraModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        node_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        role_ids: str = None,
        switch_mode: int = None,
    ):
        # The ID of the instance
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The ID of the shard node in the sharded cluster instance.
        # 
        # > You must specify this parameter if you set the **DBInstanceId** parameter to the ID of a sharded cluster instance.
        self.node_id = node_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The IDs of the roles who switch the primary and secondary nodes for the instance. You can call the [DescribeRoleZoneInfo](https://help.aliyun.com/document_detail/123802.html) operation to view the IDs and information of roles of nodes.
        # 
        # > 
        # 
        # *   Separate role IDs with commas (,). If this parameter is not specified, the primary and secondary nodes are switched.
        # 
        # *   If you set the **DBInstanceId** parameter to the ID of a sharded cluster instance, the roles who switch the primary and secondary nodes for the instance must belong to one shard node.
        self.role_ids = role_ids
        # The time when the primary and secondary nodes are switched. Valid values:
        # 
        # *   0: The primary and secondary nodes are immediately switched.
        # *   1: The primary and secondary nodes are switched during the O\\&M time period.
        self.switch_mode = switch_mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.role_ids is not None:
            result['RoleIds'] = self.role_ids

        if self.switch_mode is not None:
            result['SwitchMode'] = self.switch_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('RoleIds') is not None:
            self.role_ids = m.get('RoleIds')

        if m.get('SwitchMode') is not None:
            self.switch_mode = m.get('SwitchMode')

        return self

