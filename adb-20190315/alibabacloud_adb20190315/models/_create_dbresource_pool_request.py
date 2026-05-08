# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateDBResourcePoolRequest(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        node_num: int = None,
        owner_account: str = None,
        owner_id: int = None,
        pool_name: str = None,
        query_type: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The ID of the AnalyticDB for MySQL Data Warehouse Edition (V3.0) cluster.
        # 
        # >  You can call the [DescribeDBClusters](https://help.aliyun.com/document_detail/129857.html) operation to query the cluster IDs of all AnalyticDB for MySQL Data Warehouse Edition (V3.0) clusters within a specific region.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The number of nodes. Default value: 0.
        # 
        # *   Each node provides 16 cores and 64 GB memory.
        # *   The total amount of resources provided by the nodes (number of nodes × 16 cores, number of nodes × 64 GB memory) cannot exceed the total amount of resources in the cluster. Set this parameter to a proper value.
        self.node_num = node_num
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The name of the resource group.
        # 
        # *   The name can be up to 255 characters in length.
        # *   The name must start with a letter or a digit.
        # *   The name can contain letters, digits, hyphens (_), and underscores (_).
        # 
        # This parameter is required.
        self.pool_name = pool_name
        # The mode in which to execute SQL statements.
        # 
        # *   **batch**
        # 
        # *   **interactive**
        # 
        # > For more information, see [Query execution modes](https://help.aliyun.com/document_detail/189502.html).
        self.query_type = query_type
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

        if self.node_num is not None:
            result['NodeNum'] = self.node_num

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.pool_name is not None:
            result['PoolName'] = self.pool_name

        if self.query_type is not None:
            result['QueryType'] = self.query_type

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('NodeNum') is not None:
            self.node_num = m.get('NodeNum')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PoolName') is not None:
            self.pool_name = m.get('PoolName')

        if m.get('QueryType') is not None:
            self.query_type = m.get('QueryType')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

