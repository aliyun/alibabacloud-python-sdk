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
        # The end of the time range to query. The end time must be later than the start time. Specify the time in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time must be in UTC.
        # 
        # >  You can query the monitoring data of the previous month. The maximum time range that you can specify for a query is seven days.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is deprecated. Set the value to `01m`.
        # 
        # The **interval at which a query is performed** is automatically determined based on the start time and end time of the query. For example, if the query time range is less than or equal to 10 minutes, data is aggregated at a frequency of every 5 seconds and the results are returned at 5-second intervals.
        # 
        # > *   The query result is aligned with the data aggregation frequency. If the specified StartTime value does not coincide with a point in time for data aggregation, the system returns the latest point in time for data aggregation as the first point in time. For example, if you set the StartTime parameter to 2022-01-20T12:01:48Z, the first point in time returned is 2022-01-20T12:01:45Z.
        # > *   If the number of data shards is greater than or equal to 32, the minimum data aggregation frequency is 1 minute.
        # 
        # This parameter is required.
        self.interval_for_history = interval_for_history
        # The monitoring metrics. Separate the metrics with commas (,). Take CpuUsage as an example:
        # 
        # *   Cluster or read/write splitting instances
        # 
        #     *   To query the overall CPU utilization of all data nodes, specify **CpuUsage$db**.
        #     *   To query the CPU utilization of a single data node, specify **CpuUsage** and NodeId.
        # 
        # *   Standard master-replica instances: Specify only **CpuUsage**.
        # 
        # For more information about monitoring metrics and their descriptions, see [Additional description of MonitorKeys](https://www.alibabacloud.com/help/zh/redis/developer-reference/api-r-kvstore-2015-01-01-describehistorymonitorvalues-redis#monitorKeys-note).
        # 
        # > *   This parameter is empty by default, which indicates that the UsedMemory and quotaMemory metrics are returned.
        # > *   To ensure query efficiency, we recommend that you specify no more than five metrics for a single node at a time, and specify only a single metric when you query aggregate metrics.
        self.monitor_keys = monitor_keys
        # The ID of the node in the instance. You can set this parameter to query the data of a specified node.
        # 
        # *   This parameter is available only for read/write splitting or cluster instances of Tair.
        # 
        # *   You can call the [DescribeLogicInstanceTopology](https://help.aliyun.com/document_detail/473786.html) operation to query node IDs.
        self.node_id = node_id
        # If you want to query the metrics of the read replicas in a cloud-native read/write splitting instance, you must set this parameter to **READONLY** and specify **NodeId**.
        # 
        # > In other cases, you do not need to specify this parameter or you can set this parameter to **MASTER**.
        self.node_role = node_role
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.security_token = security_token
        # The beginning of the time range to query. Specify the time in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time must be in UTC.
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

