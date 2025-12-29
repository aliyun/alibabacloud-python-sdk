# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ReleaseNodePrivateNetworkAddressRequest(DaraModel):
    def __init__(
        self,
        connection_type: str = None,
        dbinstance_id: str = None,
        network_type: str = None,
        node_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The public endpoint type. Valid values:
        # 
        # *   **SRV**
        # *   **Normal**
        # 
        # >  This parameter is valid only when you want to release an SRV endpoint.
        self.connection_type = connection_type
        # The ID of the sharded cluster instance.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The network type of the internal endpoint. Valid values:
        # 
        # *   **VPC**: virtual private cloud (VPC).
        # *   **Classic**: classic network.
        # 
        # >  You can call the [DescribeShardingNetworkAddress](https://help.aliyun.com/document_detail/62135.html) operation to query the network type of the internal endpoint.
        self.network_type = network_type
        # The ID of the shard or Configserver node.
        # 
        # >  You can call the [DescribeDBInstanceAttribute](https://help.aliyun.com/document_detail/62010.html) operation to query the ID of the shard or Configserver node.
        self.node_id = node_id
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
        if self.connection_type is not None:
            result['ConnectionType'] = self.connection_type

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.network_type is not None:
            result['NetworkType'] = self.network_type

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectionType') is not None:
            self.connection_type = m.get('ConnectionType')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')

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

        return self

