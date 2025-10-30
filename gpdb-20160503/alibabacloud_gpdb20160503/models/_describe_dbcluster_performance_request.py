# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDBClusterPerformanceRequest(DaraModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        end_time: str = None,
        key: str = None,
        node_type: str = None,
        nodes: str = None,
        resource_group_name: str = None,
        start_time: str = None,
    ):
        # The instance ID.
        # 
        # > You can call the [DescribeDBInstances](https://help.aliyun.com/document_detail/86911.html) operation to query details about all AnalyticDB for PostgreSQL instances within a region, including instance IDs.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The end of the time range to query. Specify the time in the ISO 8601 standard in the `YYYY-MM-DDTHH:mmZ` format.
        # 
        # > The end time must be later than the start time. The maximum time range that can be specified is seven days.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The performance metric that you want to query. Separate multiple values with commas (,). For more information, see [Performance parameters](https://help.aliyun.com/document_detail/86943.html).
        # 
        # This parameter is required.
        self.key = key
        # The node type. Valid values:
        # 
        # *   **master**: coordinator node.
        # *   **segment**: compute node.
        # 
        # > If you do not specify this parameter, the performance metrics of all nodes are returned.
        self.node_type = node_type
        # The nodes for which you want to query performance metrics. Separate multiple values with commas (,). Example: `master-10******1,master-10******2`. You can call the [DescribeDBClusterNode](https://help.aliyun.com/document_detail/390136.html) operation to query the names of nodes.
        # 
        # You can also filter the nodes based on their metric values. Valid values:
        # 
        # *   **top10**: the 10 nodes that have the highest metric values.
        # *   **top20**: the 20 nodes that have the highest metric values.
        # *   **bottom10**: the 10 nodes that have the lowest metric values.
        # *   **bottom20**: the 20 nodes that have the lowest metric values.
        self.nodes = nodes
        # The name of the resource group.
        self.resource_group_name = resource_group_name
        # The beginning of the time range to query. Specify the time in the ISO 8601 standard in the `YYYY-MM-DDTHH:mmZ` format.
        # 
        # > You can query monitoring information only within the last 30 days.
        # 
        # This parameter is required.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.key is not None:
            result['Key'] = self.key

        if self.node_type is not None:
            result['NodeType'] = self.node_type

        if self.nodes is not None:
            result['Nodes'] = self.nodes

        if self.resource_group_name is not None:
            result['ResourceGroupName'] = self.resource_group_name

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')

        if m.get('Nodes') is not None:
            self.nodes = m.get('Nodes')

        if m.get('ResourceGroupName') is not None:
            self.resource_group_name = m.get('ResourceGroupName')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

