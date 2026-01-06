# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeElasticPlansRequest(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        elastic_plan_name: str = None,
        enabled: bool = None,
        page_number: int = None,
        page_size: int = None,
        resource_group_name: str = None,
        type: str = None,
    ):
        # The cluster ID.
        # 
        # >  You can call the [DescribeDBClusters](https://help.aliyun.com/document_detail/612397.html) operation to query the IDs of all AnalyticDB for MySQL clusters within a region.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The name of the scaling plan.
        # 
        # > If you do not specify this parameter, all scaling plans are queried.
        self.elastic_plan_name = elastic_plan_name
        # Specifies whether to query the scaling plans that are immediately enabled after the plans are created. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.enabled = enabled
        # The page number.
        # 
        # This parameter is required.
        self.page_number = page_number
        # The number of entries per page.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The name of the resource group.
        # 
        # > *   If you do not specify this parameter, the scaling plans of all resource groups are queried, covering the interactive resource group type and the elastic I/O unit (EIU) type.
        # >*   You can call the [DescribeDBResourceGroup](https://help.aliyun.com/document_detail/459446.html) operation to query the name of a resource group within a cluster.
        self.resource_group_name = resource_group_name
        # The type of the scaling plan. Valid values:
        # 
        # *   **EXECUTOR**: the interactive resource group type, which specifies the computing resource type.
        # *   **WORKER**: the EIU type.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.elastic_plan_name is not None:
            result['ElasticPlanName'] = self.elastic_plan_name

        if self.enabled is not None:
            result['Enabled'] = self.enabled

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.resource_group_name is not None:
            result['ResourceGroupName'] = self.resource_group_name

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('ElasticPlanName') is not None:
            self.elastic_plan_name = m.get('ElasticPlanName')

        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ResourceGroupName') is not None:
            self.resource_group_name = m.get('ResourceGroupName')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

