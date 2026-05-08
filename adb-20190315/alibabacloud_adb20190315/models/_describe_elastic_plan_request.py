# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeElasticPlanRequest(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        elastic_plan_enable: bool = None,
        elastic_plan_name: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        resource_pool_name: str = None,
    ):
        # The ID of the AnalyticDB for MySQL Data Warehouse Edition (V3.0) cluster.
        # 
        # > You can call the [DescribeDBClusters](https://help.aliyun.com/document_detail/129857.html) operation to query the IDs of all AnalyticDB for MySQL Data Warehouse Edition (V3.0) clusters within a region.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # Specifies whether the scaling plan takes effect. Valid values:
        # 
        # *   **true** (default)
        # *   **false**
        self.elastic_plan_enable = elastic_plan_enable
        # The name of the scaling plan.
        # 
        # *   The name must be 2 to 30 characters in length.
        # *   The name can contain letters, digits, and underscores (_).
        # 
        # > If you do not specify this parameter, the information about all scaling plans for the specified cluster is returned.
        self.elastic_plan_name = elastic_plan_name
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The name of the resource group.
        # 
        # > You can call the [DescribeDBResourceGroup](https://help.aliyun.com/document_detail/466685.html) operation to query the resource group name.
        self.resource_pool_name = resource_pool_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.elastic_plan_enable is not None:
            result['ElasticPlanEnable'] = self.elastic_plan_enable

        if self.elastic_plan_name is not None:
            result['ElasticPlanName'] = self.elastic_plan_name

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.resource_pool_name is not None:
            result['ResourcePoolName'] = self.resource_pool_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('ElasticPlanEnable') is not None:
            self.elastic_plan_enable = m.get('ElasticPlanEnable')

        if m.get('ElasticPlanName') is not None:
            self.elastic_plan_name = m.get('ElasticPlanName')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('ResourcePoolName') is not None:
            self.resource_pool_name = m.get('ResourcePoolName')

        return self

