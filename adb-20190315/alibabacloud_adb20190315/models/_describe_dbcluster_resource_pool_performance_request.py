# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDBClusterResourcePoolPerformanceRequest(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        end_time: str = None,
        key: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        resource_pools: str = None,
        start_time: str = None,
    ):
        # The cluster ID.
        # 
        # > You can call the [DescribeDBClusters](https://help.aliyun.com/document_detail/129857.html) operation to query the information about all AnalyticDB for MySQL clusters within a region, including cluster IDs.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The end of the time range to monitor the resource group. The end time must be later than the start time. Specify the time in the ISO 8601 standard in the *yyyy-MM-ddTHH:mmZ* format. The time must be in UTC.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The metrics of the resource group. You can enter multiple metrics at the same time to query the monitoring information. Separate multiple metrics with commas (,). Valid values:
        # 
        # *   **AnalyticDB_RP_CPU**: the average CPU utilization. Unit: %.
        # *   **AnalyticDB_RP_RT**: the query response time (RT). Unit: milliseconds.
        # *   **AnalyticDB_RP_QPS**: the queries per second (QPS). The value of this parameter must be a numeric value.
        # *   **AnalyticDB_RP_WaitTime**: the query waiting time. Unit: milliseconds.
        # *   **AnalyticDB_RP_OriginalNode**: the number of basic nodes in the resource group.
        # *   **AnalyticDB_RP_ActualNode**: the number of scheduled nodes that are scaled out in the resource group.
        # *   **AnalyticDB_RP_PlanNode**: the number of scheduled nodes to be scaled out in the resource group.
        # *   **AnalyticDB_RP_TotalNode**: the total number of nodes in the resource group. Total number of nodes = Number of basic nodes + Number of scheduled nodes that are scaled out.
        # 
        # > 
        # 
        # *   If you leave this parameter empty, the monitoring information about all metrics is returned.
        # 
        # *   For more information about scaling plans, see [Create a resource scaling plan](https://help.aliyun.com/document_detail/189507.html).
        self.key = key
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The names of the resource groups that you want to query. You can enter multiple names of resource groups. Separate multiple names with commas (,).
        # 
        # > 
        # 
        # *   The value of this parameter is case-insensitive. For example, `USER_DEFAULT` and `user_default` specify the same resource group.
        # 
        # *   If you leave this parameter empty, the monitoring information about the `USER_DEFAULT` resource group is returned.
        self.resource_pools = resource_pools
        # The beginning of the time range to monitor the resource group. Specify the time in the ISO 8601 standard in the *yyyy-MM-ddTHH:mmZ* format. The time must be in UTC.
        # 
        # > You can view only the monitoring information about the resource groups within the last two days.
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
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.key is not None:
            result['Key'] = self.key

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.resource_pools is not None:
            result['ResourcePools'] = self.resource_pools

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('ResourcePools') is not None:
            self.resource_pools = m.get('ResourcePools')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

