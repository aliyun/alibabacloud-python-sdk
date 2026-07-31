# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeApsResourceGroupsRequest(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        region_id: str = None,
        workload_id: str = None,
    ):
        # The ID of the Data Lakehouse Edition cluster.
        # 
        # > Call the [DescribeDBClusters](https://help.aliyun.com/document_detail/612397.html) operation to view the cluster ID.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The region ID.
        # 
        # > Call the [DescribeRegions](https://help.aliyun.com/document_detail/454314.html) operation to view the region ID of a cluster.
        self.region_id = region_id
        # The ID of the data synchronization task.
        self.workload_id = workload_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.workload_id is not None:
            result['WorkloadId'] = self.workload_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('WorkloadId') is not None:
            self.workload_id = m.get('WorkloadId')

        return self

