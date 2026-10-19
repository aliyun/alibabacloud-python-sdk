# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateMultiModelKnowledgeBaseRequest(DaraModel):
    def __init__(
        self,
        adb_instance_name: str = None,
        dbcluster_id: str = None,
        db_cluster_acu: int = None,
        description: str = None,
        lake_storage_bucket_name: str = None,
        region_id: str = None,
        resource_acu_max: int = None,
        resource_acu_min: int = None,
        v_switch_id: str = None,
        vpc_id: str = None,
        zone_id: str = None,
    ):
        # **[Deprecated]**
        self.adb_instance_name = adb_instance_name
        # The ID of the cluster.
        self.dbcluster_id = dbcluster_id
        # The number of ACUs for the AnalyticDB for MySQL instance resources.
        self.db_cluster_acu = db_cluster_acu
        # The description of the multimodal knowledge base instance.
        self.description = description
        # **[Deprecated]**
        self.lake_storage_bucket_name = lake_storage_bucket_name
        # The region ID.
        # 
        # > You can call the DescribeRegions operation to query the region ID of a specified Data Lakehouse Edition cluster.
        self.region_id = region_id
        # The maximum number of ACUs for the multimodal knowledge base resources.
        self.resource_acu_max = resource_acu_max
        # The minimum number of ACUs for the multimodal knowledge base resources.
        self.resource_acu_min = resource_acu_min
        # The ID of the vSwitch.
        self.v_switch_id = v_switch_id
        # The ID of the VPC.
        self.vpc_id = vpc_id
        # The ID of the zone to which the instance belongs.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.adb_instance_name is not None:
            result['AdbInstanceName'] = self.adb_instance_name

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.db_cluster_acu is not None:
            result['DbClusterAcu'] = self.db_cluster_acu

        if self.description is not None:
            result['Description'] = self.description

        if self.lake_storage_bucket_name is not None:
            result['LakeStorageBucketName'] = self.lake_storage_bucket_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_acu_max is not None:
            result['ResourceAcuMax'] = self.resource_acu_max

        if self.resource_acu_min is not None:
            result['ResourceAcuMin'] = self.resource_acu_min

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdbInstanceName') is not None:
            self.adb_instance_name = m.get('AdbInstanceName')

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('DbClusterAcu') is not None:
            self.db_cluster_acu = m.get('DbClusterAcu')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('LakeStorageBucketName') is not None:
            self.lake_storage_bucket_name = m.get('LakeStorageBucketName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceAcuMax') is not None:
            self.resource_acu_max = m.get('ResourceAcuMax')

        if m.get('ResourceAcuMin') is not None:
            self.resource_acu_min = m.get('ResourceAcuMin')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

