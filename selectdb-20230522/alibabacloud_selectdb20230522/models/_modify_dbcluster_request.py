# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyDBClusterRequest(DaraModel):
    def __init__(
        self,
        cache_size: str = None,
        cluster_node_count: int = None,
        cluster_node_type: str = None,
        dbcluster_class: str = None,
        dbcluster_id: str = None,
        dbinstance_id: str = None,
        engine: str = None,
        region_id: str = None,
        resource_owner_id: int = None,
        scale_max: float = None,
        scale_min: float = None,
    ):
        # The reserved cache size.
        self.cache_size = cache_size
        # The number of cluster nodes. This parameter takes effect only in Serverless mode.
        self.cluster_node_count = cluster_node_count
        # The cluster node type. This parameter takes effect only in Serverless mode.
        self.cluster_node_type = cluster_node_type
        # The cluster specifications. Valid values:
        # - **selectdb.xlarge**: 4 cores and 32 GB.
        # - **selectdb.2xlarge**: 8 cores and 64 GB.
        # - **selectdb.4xlarge**: 16 cores and 128 GB.
        # - **selectdb.8xlarge**: 32 cores and 256 GB.
        # - **selectdb.16xlarge**: 16 cores and 512 GB.
        # - **selectdb.24xlarge**: 24 cores and 768 GB.
        # - **selectdb.32xlarge**: 32 cores and 1024 GB.
        # 
        # This parameter is required.
        self.dbcluster_class = dbcluster_class
        # The cluster ID.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The instance ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The database engine type. Set the value to selectdb.
        self.engine = engine
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_id = resource_owner_id
        # The maximum value of the auto-scaling range for the instance RCU (RDS Capacity Unit).
        self.scale_max = scale_max
        # The minimum value of the auto-scaling range for the instance RCU (RDS Capacity Unit).
        self.scale_min = scale_min

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cache_size is not None:
            result['CacheSize'] = self.cache_size

        if self.cluster_node_count is not None:
            result['ClusterNodeCount'] = self.cluster_node_count

        if self.cluster_node_type is not None:
            result['ClusterNodeType'] = self.cluster_node_type

        if self.dbcluster_class is not None:
            result['DBClusterClass'] = self.dbcluster_class

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.engine is not None:
            result['Engine'] = self.engine

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.scale_max is not None:
            result['ScaleMax'] = self.scale_max

        if self.scale_min is not None:
            result['ScaleMin'] = self.scale_min

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CacheSize') is not None:
            self.cache_size = m.get('CacheSize')

        if m.get('ClusterNodeCount') is not None:
            self.cluster_node_count = m.get('ClusterNodeCount')

        if m.get('ClusterNodeType') is not None:
            self.cluster_node_type = m.get('ClusterNodeType')

        if m.get('DBClusterClass') is not None:
            self.dbcluster_class = m.get('DBClusterClass')

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('Engine') is not None:
            self.engine = m.get('Engine')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('ScaleMax') is not None:
            self.scale_max = m.get('ScaleMax')

        if m.get('ScaleMin') is not None:
            self.scale_min = m.get('ScaleMin')

        return self

