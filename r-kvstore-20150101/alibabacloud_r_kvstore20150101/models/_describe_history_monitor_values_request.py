# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeHistoryMonitorValuesRequest(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        instance_id: str = None,
        interval_for_history: str = None,
        monitor_keys: str = None,
        node_id: str = None,
        node_role: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        security_token: str = None,
        start_time: str = None,
        type: str = None,
    ):
        # The end time of the query for historical monitoring data. The end time must be later than the start time. Specify the time in the <i>yyyy-MM-dd</i>T<i>HH:mm:ss</i>Z format (UTC).
        # 
        # > You can query monitoring data of the last month. The maximum query range cannot exceed 7 days.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # **[Deprecated]** This parameter is deprecated. The value is fixed to `01m`.
        # 
        # The system automatically determines the **query interval** based on the start time and end time. For example, if the query time range is less than or equal to 10 minutes, the data aggregation frequency is 5s, and the query results are returned at a frequency of 5s.
        # > * The query results are aligned with the data aggregation frequency of the instance. If the StartTime you specify does not fall on a data aggregation point, the first time point returned by the system is the nearest data aggregation point. For example, if the StartTime you specify is 2022-01-20T12:01:48Z, the first time point returned by the system is 2022-01-20T12:01:45Z.
        # > * If the number of data shards of the instance is greater than or equal to 32, the minimum data aggregation frequency is 1 minute.
        # 
        # This parameter is required.
        self.interval_for_history = interval_for_history
        # The monitoring metrics. To specify multiple monitoring metrics, separate them with commas (,). Take CpuUsage as an example:
        # * Cluster or read/write splitting architecture:
        #     - To query the overall CPU usage of all data nodes (DB), specify **CpuUsage$db**.
        #    - To query the CPU usage of a single data node, specify **CpuUsage** and set the NodeId parameter to the DB node.
        # 
        # * Standard architecture (primary/secondary): Specify **CpuUsage**.
        # 
        # For more information about monitoring metrics and their descriptions, see <props="china">[MonitorKeys parameter description](https://www.alibabacloud.com/help/en/redis/developer-reference/api-r-kvstore-2015-01-01-describehistorymonitorvalues-redis#monitorKeys-note)<props="intl">[MonitorKeys parameter description](https://www.alibabacloud.com/help/zh/redis/developer-reference/api-r-kvstore-2015-01-01-describehistorymonitorvalues-redis#monitorKeys-note).
        # > * This parameter is empty by default. If this parameter is not specified, the UsedMemory and quotaMemory metrics are returned.
        # > * To ensure query efficiency, specify no more than 5 monitoring metrics in a single request when querying metrics for a single node. Specify no more than 1 monitoring metric in a single request when querying aggregated monitoring metrics.
        self.monitor_keys = monitor_keys
        # The node ID of the instance. Specify this parameter to query the monitoring information of a specific node.
        # 
        # > * This parameter is available only when the instance uses a read/write splitting or cluster architecture.
        # > * You can call the [DescribeLogicInstanceTopology](https://help.aliyun.com/document_detail/473786.html) operation to query node IDs.
        self.node_id = node_id
        # To query the metrics of a read-only node in a cloud-native read/write splitting instance, specify the **NodeId** parameter and set this parameter to **READONLY**.
        # >  In other cases, you do not need to specify this parameter (or set it to **MASTER**).
        self.node_role = node_role
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.security_token = security_token
        # The start time of the query for historical monitoring data. Specify the time in the <i>yyyy-MM-dd</i>T<i>HH:mm:ss</i>Z format (UTC).
        # 
        # This parameter is required.
        self.start_time = start_time
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.interval_for_history is not None:
            result['IntervalForHistory'] = self.interval_for_history

        if self.monitor_keys is not None:
            result['MonitorKeys'] = self.monitor_keys

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.node_role is not None:
            result['NodeRole'] = self.node_role

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('IntervalForHistory') is not None:
            self.interval_for_history = m.get('IntervalForHistory')

        if m.get('MonitorKeys') is not None:
            self.monitor_keys = m.get('MonitorKeys')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('NodeRole') is not None:
            self.node_role = m.get('NodeRole')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

