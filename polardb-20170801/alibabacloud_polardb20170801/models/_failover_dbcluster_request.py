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
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, and you must make sure that the value is unique among different requests. The token is case-sensitive and cannot exceed 64 ASCII characters in length.
        self.client_token = client_token
        # The cluster ID.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # Specifies whether to switch back to the original primary zone after a failover. Valid values:
        # 
        # - true: Switch back to the original primary zone.
        # - false: Do not switch back to the original primary zone.
        self.roll_back_for_disaster = roll_back_for_disaster
        # The ID of the node that you want to promote to the primary node. If you leave this parameter empty, the system automatically elects a node. You can call the [DescribeDBClusters](https://help.aliyun.com/document_detail/98094.html) operation to query node IDs and other information.
        # 
        # > - Automatic election of the primary node: The system identifies all read-only nodes that are eligible for election. The system selects one or more read-only nodes with the highest priority. If the switchover to the first node fails due to reasons such as network issues or abnormal replication status, the system attempts to switch to the next node until the switchover succeeds.
        # >- This parameter is required when the cluster is a PolarDB for PostgreSQL (Compatible with Oracle) or PolarDB for PostgreSQL cluster. This parameter is optional when the cluster is a PolarDB for MySQL cluster.
        self.target_dbnode_id = target_dbnode_id
        # Specifies whether the primary/secondary switchover is performed within the primary zone. Valid values:
        # - Primary: The primary/secondary switchover is performed within the primary zone.
        # - Standby: The switchover is performed to the hot standby storage cluster.
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

