# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateDBClusterRequest(DaraModel):
    def __init__(
        self,
        cache_size: str = None,
        charge_type: str = None,
        cluster_node_count: int = None,
        cluster_node_type: str = None,
        dbcluster_class: str = None,
        dbcluster_description: str = None,
        dbinstance_id: str = None,
        engine: str = None,
        engine_version: str = None,
        period: str = None,
        region_id: str = None,
        resource_owner_id: int = None,
        scale_max: float = None,
        scale_min: float = None,
        used_time: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
        zone_id: str = None,
    ):
        # The reserved cache size.
        # 
        # This parameter is required.
        self.cache_size = cache_size
        # The billing method of the cluster. Valid values:
        # 
        # - **Postpaid**: pay-as-you-go
        # 
        # - **Prepaid**: subscription
        # 
        # This parameter is required.
        self.charge_type = charge_type
        # The number of nodes in the cluster. This parameter takes effect only in Serverless mode.
        self.cluster_node_count = cluster_node_count
        # The node type of the cluster. This parameter takes effect only in Serverless mode.
        self.cluster_node_type = cluster_node_type
        # The cluster specifications. Valid values:
        # - **selectdb.xlarge**: 4 cores and 32 GB memory
        # - **selectdb.2xlarge**: 8 cores and 64 GB memory
        # - **selectdb.4xlarge**: 16 cores and 128 GB memory
        # - **selectdb.8xlarge**: 32 cores and 256 GB memory
        # - **selectdb.16xlarge**: 64 cores and 512 GB memory
        # - **selectdb.24xlarge**: 96 cores and 768 GB memory
        # - **selectdb.32xlarge**: 128 cores and 1024 GB memory
        # 
        # This parameter is required.
        self.dbcluster_class = dbcluster_class
        # The cluster description.
        # 
        # This parameter is required.
        self.dbcluster_description = dbcluster_description
        # The instance ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The database type.
        self.engine = engine
        # The database version.
        # 
        # This parameter is required.
        self.engine_version = engine_version
        # Specifies whether the subscription cluster is billed on a yearly or monthly basis. Valid values:
        # 
        # - **Year**: yearly
        # - **Month**: monthly
        # > This parameter takes effect and is required only when **ChargeType** is set to **Prepaid**.
        self.period = period
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_id = resource_owner_id
        # The maximum value of the auto-scaling range for the instance RCU (RDS Capacity Unit).
        self.scale_max = scale_max
        # The minimum value of the auto-scaling range for the instance RCU (RDS Capacity Unit).
        self.scale_min = scale_min
        # Specifies the purchase duration of the subscription cluster. The unit is specified by Period: Year indicates years, and Month indicates months. Valid values:
        # - If Period is set to Year, valid values for UsedTime are 1, 2, 3, and 5.
        # - If Period is set to Month, valid values for UsedTime are 1 to 9.
        # > This parameter takes effect and is required only when ChargeType is set to Prepaid.
        self.used_time = used_time
        # The vSwitch ID.
        # 
        # This parameter is required.
        self.v_switch_id = v_switch_id
        # The VPC ID.
        # 
        # This parameter is required.
        self.vpc_id = vpc_id
        # The zone ID.
        # 
        # This parameter is required.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cache_size is not None:
            result['CacheSize'] = self.cache_size

        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        if self.cluster_node_count is not None:
            result['ClusterNodeCount'] = self.cluster_node_count

        if self.cluster_node_type is not None:
            result['ClusterNodeType'] = self.cluster_node_type

        if self.dbcluster_class is not None:
            result['DBClusterClass'] = self.dbcluster_class

        if self.dbcluster_description is not None:
            result['DBClusterDescription'] = self.dbcluster_description

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.engine is not None:
            result['Engine'] = self.engine

        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version

        if self.period is not None:
            result['Period'] = self.period

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.scale_max is not None:
            result['ScaleMax'] = self.scale_max

        if self.scale_min is not None:
            result['ScaleMin'] = self.scale_min

        if self.used_time is not None:
            result['UsedTime'] = self.used_time

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CacheSize') is not None:
            self.cache_size = m.get('CacheSize')

        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        if m.get('ClusterNodeCount') is not None:
            self.cluster_node_count = m.get('ClusterNodeCount')

        if m.get('ClusterNodeType') is not None:
            self.cluster_node_type = m.get('ClusterNodeType')

        if m.get('DBClusterClass') is not None:
            self.dbcluster_class = m.get('DBClusterClass')

        if m.get('DBClusterDescription') is not None:
            self.dbcluster_description = m.get('DBClusterDescription')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('Engine') is not None:
            self.engine = m.get('Engine')

        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('ScaleMax') is not None:
            self.scale_max = m.get('ScaleMax')

        if m.get('ScaleMin') is not None:
            self.scale_min = m.get('ScaleMin')

        if m.get('UsedTime') is not None:
            self.used_time = m.get('UsedTime')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

