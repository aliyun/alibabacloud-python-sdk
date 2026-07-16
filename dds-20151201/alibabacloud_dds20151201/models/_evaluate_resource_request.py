# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class EvaluateResourceRequest(DaraModel):
    def __init__(
        self,
        dbinstance_class: str = None,
        dbinstance_id: str = None,
        engine: str = None,
        engine_version: str = None,
        owner_account: str = None,
        owner_id: int = None,
        readonly_replicas: str = None,
        region_id: str = None,
        replication_factor: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        shards_info: str = None,
        storage: str = None,
        zone_id: str = None,
    ):
        # The instance type.
        # 
        # > This parameter is required when you evaluate resources for a replica set instance. For details about instance types, see [Instance types](https://help.aliyun.com/document_detail/57141.html).
        self.dbinstance_class = dbinstance_class
        # The instance ID. This parameter is required when you evaluate resources for an instance upgrade or downgrade.
        self.dbinstance_id = dbinstance_id
        # The database engine. Set the value to **MongoDB**.
        self.engine = engine
        # The database engine version.
        # 
        # This parameter is required.
        self.engine_version = engine_version
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The number of read-only nodes in the instance. Valid values: **1** to **5**.
        # 
        # > This parameter is not required for standalone instances<props="china"> and Serverless instances.
        self.readonly_replicas = readonly_replicas
        # The ID of the region. For more information, see [DescribeRegions](https://help.aliyun.com/document_detail/61933.html).
        # 
        # This parameter is required.
        self.region_id = region_id
        # The number of nodes in the instance.
        # 
        # - Set the value to **1** for a standalone instance.
        # 
        # - Set the value to **2** for an instance that uses shared storage.
        # 
        # - For a replica set instance, valid values are **3**, **5**, and **7**.
        # 
        # <props="china">
        # 
        # > This parameter is not required for Serverless instances.
        self.replication_factor = replication_factor
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The shard information of the sharded cluster. This parameter is required when you evaluate resources for a sharded cluster instance.
        # 
        # To evaluate resources for a new sharded cluster instance, specify the instance type for each shard in a JSON string. Example:
        # 
        # ```
        # {
        #      "ConfigSvrs":
        #          [{"Storage":20,"DBInstanceClass":"dds.cs.mid"}],
        #      "Mongos":
        #          [{"DBInstanceClass":"dds.mongos.standard"},{"DBInstanceClass":"dds.mongos.standard"}],
        #      "Shards":
        #          [{"Storage":50,"DBInstanceClass":"dds.shard.standard"},{"Storage":50,"DBInstanceClass":"dds.shard.standard"},   {"Storage":50,"DBInstanceClass":"dds.shard.standard"}]
        #  }
        # ```
        # 
        # The parameters in the example are described as follows:
        # 
        # - ConfigSvrs: The ConfigServer nodes.
        # 
        # - Mongos: The Mongos nodes.
        # 
        # - Shards: The shard nodes.
        # 
        # - Storage: The storage space of the target shard.
        # 
        # - DBInstanceClass: The instance type of the target shard. For details about instance types, see [Sharded cluster instance types](https://help.aliyun.com/document_detail/311414.html).
        # 
        # To evaluate resources for upgrading or downgrading a sharded cluster instance, specify only the node information in a JSON string. Example:
        # 
        # ```
        # {
        #      "NodeId": "d-bp147c4d9ca7****", "NodeClass": "dds.shard.standard"
        # } 
        # ```
        # 
        # The parameters in the example are described as follows:
        # 
        # - NodeId: The ID of the target node.
        # 
        # - NodeClass: The instance type of the target node. For details about instance types, see [Sharded cluster instance types](https://help.aliyun.com/document_detail/311414.html).
        self.shards_info = shards_info
        # The storage space of the replica set. Unit: GB.
        # 
        # > This parameter is required if the instance uses cloud disks.
        self.storage = storage
        # The ID of the zone. For more information, see [DescribeRegions](https://help.aliyun.com/document_detail/61933.html).
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
        if self.dbinstance_class is not None:
            result['DBInstanceClass'] = self.dbinstance_class

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.engine is not None:
            result['Engine'] = self.engine

        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.readonly_replicas is not None:
            result['ReadonlyReplicas'] = self.readonly_replicas

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.replication_factor is not None:
            result['ReplicationFactor'] = self.replication_factor

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.shards_info is not None:
            result['ShardsInfo'] = self.shards_info

        if self.storage is not None:
            result['Storage'] = self.storage

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceClass') is not None:
            self.dbinstance_class = m.get('DBInstanceClass')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('Engine') is not None:
            self.engine = m.get('Engine')

        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ReadonlyReplicas') is not None:
            self.readonly_replicas = m.get('ReadonlyReplicas')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ReplicationFactor') is not None:
            self.replication_factor = m.get('ReplicationFactor')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('ShardsInfo') is not None:
            self.shards_info = m.get('ShardsInfo')

        if m.get('Storage') is not None:
            self.storage = m.get('Storage')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

