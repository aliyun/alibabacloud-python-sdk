# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeAvailableResourceRequest(DaraModel):
    def __init__(
        self,
        dbinstance_class: str = None,
        db_type: str = None,
        engine_version: str = None,
        instance_charge_type: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        replication_factor: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        storage_type: str = None,
        zone_id: str = None,
    ):
        # The instance type of the instance.
        self.dbinstance_class = dbinstance_class
        # The architecture of the instance. Valid values:
        # 
        # *   **normal**: replica set instance
        # *   **sharding**: sharded cluster instance
        self.db_type = db_type
        # The major engine version of the instance.
        self.engine_version = engine_version
        # The billing method of the instance. Valid values:
        # 
        # *   **PrePaid** (default): subscription
        # *   **PostPaid**: pay-as-you-go
        self.instance_charge_type = instance_charge_type
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The ID of the region. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/61933.html) operation to query the latest available regions.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The number of nodes, only applicable to replica sets.
        self.replication_factor = replication_factor
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The storage type of the instance. Valid values:
        # 
        # *   local_ssd: local SSD
        # *   cloud_essd1: PL1 enhanced SSD (ESSD)
        # *   cloud_essd2: PL2 ESSD
        # *   cloud_essd3: PL3 ESSD
        # *   cloud_auto: ESSD AutoPL disk
        # 
        # This parameter is empty by default, which indicates all types of storage resources are queried.
        self.storage_type = storage_type
        # The ID of the zone. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/61933.html) operation to query the available zones.
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

        if self.db_type is not None:
            result['DbType'] = self.db_type

        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version

        if self.instance_charge_type is not None:
            result['InstanceChargeType'] = self.instance_charge_type

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.replication_factor is not None:
            result['ReplicationFactor'] = self.replication_factor

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.storage_type is not None:
            result['StorageType'] = self.storage_type

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceClass') is not None:
            self.dbinstance_class = m.get('DBInstanceClass')

        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')

        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')

        if m.get('InstanceChargeType') is not None:
            self.instance_charge_type = m.get('InstanceChargeType')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ReplicationFactor') is not None:
            self.replication_factor = m.get('ReplicationFactor')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

