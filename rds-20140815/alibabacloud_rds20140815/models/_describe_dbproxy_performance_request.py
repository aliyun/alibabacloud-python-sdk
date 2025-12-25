# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDBProxyPerformanceRequest(DaraModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        dbproxy_engine_type: str = None,
        dbproxy_instance_type: str = None,
        dimension: str = None,
        end_time: str = None,
        metrics_name: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        start_time: str = None,
    ):
        # The instance ID. You can call the DescribeDBInstances operation to query the instance ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # A reserved parameter. You do not need to specify this parameter.
        self.dbproxy_engine_type = dbproxy_engine_type
        # The type of the database proxy instance. Valid values:
        # 
        # *   common: the general-purpose database proxy
        # *   exclusive: the dedicated database proxy
        self.dbproxy_instance_type = dbproxy_instance_type
        # Dimension.
        self.dimension = dimension
        # The end of the time range to query. The end time must be later than the start time. Specify the time in the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time must be in UTC.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The performance metrics that you want to query.
        # 
        # If the instance runs MySQL, you can query only the **Maxscale_CpuUsage** performance metric, which indicates the CPU utilization of the instance.
        # 
        # If the instance runs PostgreSQL, you can query the following performance metrics:
        # 
        # *   **Maxscale_TotalConns**: the number of connections per second
        # *   **Maxscale_CurrentConns**: the number of connections that are established
        # *   **Maxscale_DownFlows**: outbound traffic
        # *   **Maxscale_UpFlows**: inbound traffic
        # *   **Maxscale_QPS**: QPS
        # *   **Maxscale_MemUsage**: memory usage
        # *   **Maxscale_CpuUsage**: CPU utilization
        # 
        # If you want to query more than one performance metric, separate the performance metrics with commas (,). You can specify up to six performance metrics in a single request.
        # 
        # This parameter is required.
        self.metrics_name = metrics_name
        self.owner_id = owner_id
        # The region ID. You can call the DescribeRegions operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The beginning of the time range to query. Specify the time in the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time must be in UTC.
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

        if self.dbproxy_engine_type is not None:
            result['DBProxyEngineType'] = self.dbproxy_engine_type

        if self.dbproxy_instance_type is not None:
            result['DBProxyInstanceType'] = self.dbproxy_instance_type

        if self.dimension is not None:
            result['Dimension'] = self.dimension

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.metrics_name is not None:
            result['MetricsName'] = self.metrics_name

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('DBProxyEngineType') is not None:
            self.dbproxy_engine_type = m.get('DBProxyEngineType')

        if m.get('DBProxyInstanceType') is not None:
            self.dbproxy_instance_type = m.get('DBProxyInstanceType')

        if m.get('Dimension') is not None:
            self.dimension = m.get('Dimension')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('MetricsName') is not None:
            self.metrics_name = m.get('MetricsName')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

