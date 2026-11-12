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
        # > You can call the [DescribeDBInstances](https://help.aliyun.com/document_detail/86911.html) operation to query the details of all AnalyticDB for PostgreSQL instances in a specified region, including the instance IDs.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The end time of the query. Specify the time in the `YYYY-MM-DDTHH:mmZ` format.
        # 
        # > The end time must be later than the start time, and the time interval between the start time and the end time cannot exceed 7 days.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The names of the performance metrics. Separate multiple metrics with commas (,). For more information, see [Performance metric table](https://help.aliyun.com/document_detail/86943.html).
        # 
        # This parameter is required.
        self.key = key
        # The node type. Valid values:
        # 
        # - **master**: Master node.
        # - **segment**: Segment node.
        # 
        # > If you do not specify this parameter, the monitoring metrics of all nodes are returned.
        self.node_type = node_type
        # The names of the nodes for which you want to query monitoring metrics. Separate multiple node names with commas (,), such as `master-10******1,master-10******2`. You can call the [DescribeDBClusterNode](https://help.aliyun.com/document_detail/390136.html) operation to obtain the node names.
        # 
        # You can also filter nodes based on the values of monitoring metrics. Valid values:
        # - **top10**: The top 10 nodes with the highest monitoring metric values.
        # - **top20**: The top 20 nodes with the highest monitoring metric values.
        # - **bottom10**: The bottom 10 nodes with the lowest monitoring metric values.
        # - **bottom20**: The bottom 20 nodes with the lowest monitoring metric values.
        self.nodes = nodes
        # The name of the resource group.
        self.resource_group_name = resource_group_name
        # The start time of the query. Specify the time in the `YYYY-MM-DDTHH:mmZ` format.
        # 
        # > You can query monitoring information only for the last 30 days.
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

