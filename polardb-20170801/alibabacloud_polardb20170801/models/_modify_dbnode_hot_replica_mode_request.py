# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyDBNodeHotReplicaModeRequest(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        dbnode_id: str = None,
        hot_replica_mode: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The cluster ID.
        # > You can call the [DescribeDBClusters](https://help.aliyun.com/document_detail/98094.html) operation to query the details of all clusters under your account, including the cluster ID.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The ID of the database cluster node.
        # 
        # This parameter is required.
        self.dbnode_id = dbnode_id
        # Specifies whether to enable hot standby. Valid values:
        # - **ON**: Enabled.
        # - **OFF**: Disabled.
        # Limits: This operation is supported only for non-serverless MySQL clusters. The target node must be a read-only node. Each cluster allows only one node to have HotReplicaMode (ON). Usage notes: Append the following limits to the end of the HotReplicaMode parameter description: this operation is supported only for non-serverless MySQL clusters. The target node must be a read-only node. Each cluster allows only one node to have HotReplicaMode (ON).
        # 
        # This parameter is required.
        self.hot_replica_mode = hot_replica_mode
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.dbnode_id is not None:
            result['DBNodeId'] = self.dbnode_id

        if self.hot_replica_mode is not None:
            result['HotReplicaMode'] = self.hot_replica_mode

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('DBNodeId') is not None:
            self.dbnode_id = m.get('DBNodeId')

        if m.get('HotReplicaMode') is not None:
            self.hot_replica_mode = m.get('HotReplicaMode')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

