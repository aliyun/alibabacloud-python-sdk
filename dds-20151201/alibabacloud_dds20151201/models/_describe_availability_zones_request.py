# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeAvailabilityZonesRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        dbinstance_class: str = None,
        db_type: str = None,
        engine_version: str = None,
        exclude_secondary_zone_id: str = None,
        exclude_zone_id: str = None,
        instance_charge_type: str = None,
        instance_type: str = None,
        mongo_type: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        replication_factor: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        storage_support: str = None,
        storage_type: str = None,
        zone_id: str = None,
    ):
        # The language of the returned **RegionName** and **ZoneName** parameter values. Valid values:
        # 
        # *   **zh** (default): Chinese
        # *   **en**: English
        self.accept_language = accept_language
        # The instance type of the instance.
        self.dbinstance_class = dbinstance_class
        # The architecture of the instance. Valid values:
        # 
        # *   **normal**: replica set instance
        # *   **sharding**: sharded cluster instance
        self.db_type = db_type
        # The database engine version of the instance.
        self.engine_version = engine_version
        # The secondary zone ID that is excluded from the query results. You can configure the ExcludeZoneId and ExcludeSecondaryZoneId parameters to specify the IDs of multiple zones that are excluded from the query results.
        self.exclude_secondary_zone_id = exclude_secondary_zone_id
        # The zone ID that is excluded from the query results.
        self.exclude_zone_id = exclude_zone_id
        # The billing method of the product. Valid values:
        # 
        # *   **PrePaid**: subscription
        # *   **PostPaid:** pay-as-you-go
        self.instance_charge_type = instance_charge_type
        # The architecture of the instance. Valid values:
        # 
        # *   **sharding**: sharded cluster instance
        # *   **replicate**: replica set or standalone instance
        self.instance_type = instance_type
        # The edition of the instance. High-Available Edition and Preview Edition (dbfs) are supported.
        self.mongo_type = mongo_type
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID of the instance. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/61933.html) operation to query the latest available regions.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The number of nodes in the instance.
        # 
        # >  This parameter is available only for replica set instances.
        # 
        # Valid values:
        # 
        # *   1
        # *   3
        # *   5
        # *   7
        self.replication_factor = replication_factor
        # The ID of the resource group. For more information, see [View basic information of a resource group](https://help.aliyun.com/document_detail/151181.html).
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The storage type. Valid values:
        # 
        # *   **cloud**: displays only zones available for instances that use cloud disks.
        # *   **local**: only displays zones available for instances that use local disks instances.
        # *   **default** or unspecified: displays zones available for instances that use cloud disks and those that use local disks.
        self.storage_support = storage_support
        # The storage type. Valid values:
        # 
        # *   **cloud_essd1**: PL1 Enterprise SSDs (ESSDs)
        # *   **cloud_essd2**: PL2 ESSDs
        # *   **cloud_essd3**: PL3 ESSDs
        # *   **local_ssd**: local SSDs
        # 
        # > *   Instances that run MongoDB 4.4 or later only use cloud disks to store data. If you do not specify this parameter, the value **cloud_essd1** is used by default.
        # > *   Instances that run MongoDB 4.2 and earlier only use local disks to store data. If you do not specify this parameter, the value **local_ssd** is used by default.
        self.storage_type = storage_type
        # The zone ID of the instance. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/61933.html) operation to query available zones.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language

        if self.dbinstance_class is not None:
            result['DBInstanceClass'] = self.dbinstance_class

        if self.db_type is not None:
            result['DbType'] = self.db_type

        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version

        if self.exclude_secondary_zone_id is not None:
            result['ExcludeSecondaryZoneId'] = self.exclude_secondary_zone_id

        if self.exclude_zone_id is not None:
            result['ExcludeZoneId'] = self.exclude_zone_id

        if self.instance_charge_type is not None:
            result['InstanceChargeType'] = self.instance_charge_type

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.mongo_type is not None:
            result['MongoType'] = self.mongo_type

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

        if self.storage_support is not None:
            result['StorageSupport'] = self.storage_support

        if self.storage_type is not None:
            result['StorageType'] = self.storage_type

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')

        if m.get('DBInstanceClass') is not None:
            self.dbinstance_class = m.get('DBInstanceClass')

        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')

        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')

        if m.get('ExcludeSecondaryZoneId') is not None:
            self.exclude_secondary_zone_id = m.get('ExcludeSecondaryZoneId')

        if m.get('ExcludeZoneId') is not None:
            self.exclude_zone_id = m.get('ExcludeZoneId')

        if m.get('InstanceChargeType') is not None:
            self.instance_charge_type = m.get('InstanceChargeType')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('MongoType') is not None:
            self.mongo_type = m.get('MongoType')

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

        if m.get('StorageSupport') is not None:
            self.storage_support = m.get('StorageSupport')

        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

