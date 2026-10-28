# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeElasticPlanSpecificationsRequest(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        resource_group_name: str = None,
        type: str = None,
    ):
        # The ID of the cluster.
        # > You can call the [DescribeDBClusters](https://help.aliyun.com/document_detail/454250.html) operation to query the cluster ID.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The name of the resource group.
        # 
        # >- To query the specifications supported by the elastic plan of an Interactive resource group (compute resource type), you must specify the resource group name. To query the specifications supported by the elastic plan of the storage acceleration service (EIU), you do not need to specify the resource group name.
        # - You can call the [DescribeDBResourceGroup](https://help.aliyun.com/document_detail/459446.html) operation to query the resource group name of a specific cluster.
        self.resource_group_name = resource_group_name
        # The type of the elastic plan. Valid values:
        # 
        # - EXECUTOR: Interactive resource group, which is the compute resource type.
        # - WORKER: storage acceleration service (EIU).
        # 
        # This parameter is required.
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

        if self.resource_group_name is not None:
            result['ResourceGroupName'] = self.resource_group_name

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('ResourceGroupName') is not None:
            self.resource_group_name = m.get('ResourceGroupName')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

