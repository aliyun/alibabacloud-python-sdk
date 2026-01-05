# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class FailoverDBClusterRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        dbcluster_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        roll_back_for_disaster: bool = None,
        target_dbnode_id: str = None,
        target_zone_type: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. The token is case-sensitive.
        self.client_token = client_token
        # The ID of the cluster.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # Specifies whether to switch back services to the original primary zone when the original primary zone recovers.
        # 
        # *   true
        # *   false
        self.roll_back_for_disaster = roll_back_for_disaster
        # The ID of the read-only node that you want to promote to the primary node. You can call the [DescribeDBClusters](https://help.aliyun.com/document_detail/98094.html) operation to query node information, such as node IDs.
        # 
        # > *   If you leave this parameter empty, the system selects one or more available read-only nodes that have the highest failover priority as candidate primary nodes. If the failover to the first read-only node fails due to network issues, abnormal replication status, or other reasons, the system attempts to fail over your applications to the next read-only node until the failover is successful.
        # >*  This parameter is required for PolarDB for Oracle and PolarDB for PostgreSQL clusters. This parameter is optional for PolarDB for MySQL clusters.
        self.target_dbnode_id = target_dbnode_id
        # Whether it is a primary-standby switch within the primary availability zone, with the following values:
        # 
        # Primary: Primary-standby switch within the primary availability zone.
        # Standby: Switch to the storage hot backup cluster.
        self.target_zone_type = target_zone_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.roll_back_for_disaster is not None:
            result['RollBackForDisaster'] = self.roll_back_for_disaster

        if self.target_dbnode_id is not None:
            result['TargetDBNodeId'] = self.target_dbnode_id

        if self.target_zone_type is not None:
            result['TargetZoneType'] = self.target_zone_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('RollBackForDisaster') is not None:
            self.roll_back_for_disaster = m.get('RollBackForDisaster')

        if m.get('TargetDBNodeId') is not None:
            self.target_dbnode_id = m.get('TargetDBNodeId')

        if m.get('TargetZoneType') is not None:
            self.target_zone_type = m.get('TargetZoneType')

        return self

