# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CheckCreateDdrDBInstanceRequest(DaraModel):
    def __init__(
        self,
        backup_set_id: str = None,
        dbinstance_class: str = None,
        dbinstance_storage: int = None,
        engine: str = None,
        engine_version: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        restore_time: str = None,
        restore_type: str = None,
        source_dbinstance_name: str = None,
        source_region: str = None,
    ):
        # The ID of the backup set that is used for the restoration. You can call the DescribeCrossRegionBackups operation to query the backup set ID.
        # 
        # >  This parameter must be specified when the **RestoreType** parameter is set to **0**.
        self.backup_set_id = backup_set_id
        # The instance type of the destination instance. For more information, see [Primary ApsaraDB RDS instance types](https://help.aliyun.com/document_detail/26312.html).
        # 
        # This parameter is required.
        self.dbinstance_class = dbinstance_class
        # The storage capacity of the destination instance. Valid values: **5 to 2000**. Unit: GB. You can increase the storage capacity in increments of 5 GB. For more information, see [Primary instance types](https://help.aliyun.com/document_detail/26312.html).
        # 
        # This parameter is required.
        self.dbinstance_storage = dbinstance_storage
        # The database engine of the destination instance. Valid values:
        # 
        # *   **MySQL**
        # *   **SQLServer**
        # *   **PostgreSQL**
        # 
        # This parameter is required.
        self.engine = engine
        # The major engine version of the destination instance. The value of this parameter varies based on the value of **Engine**.
        # 
        # *   Valid values when Engine is set to MySQL: **5.5, 5.6, 5.7, and 8.0**
        # *   Valid values when Engine is set to SQLServer: **2008r2, 08r2_ent_ha, 2012, 2012_ent_ha, 2012_std_ha, 2012_web, 2014_std_ha, 2016_ent_ha, 2016_std_ha, 2016_web, 2017_std_ha, 2017_ent, 2019_std_ha, and 2019_ent**
        # *   PostgreSQL: **10.0, 11.0, 12.0, 13.0, 14.0, and 15.0**
        # 
        # This parameter is required.
        self.engine_version = engine_version
        self.owner_id = owner_id
        # The region ID of the destination instance. You can call the DescribeRegions operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The resource group ID. You can call the DescribeDBInstanceAttribute to query the resource group ID.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The point in time to which you want to restore data. The point in time that you specify must be earlier than the current time. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        # 
        # > If you set **RestoreType** to **1**, you must also specify this parameter.
        self.restore_time = restore_time
        # The method that is used to restore data. Valid values:
        # 
        # *   **0**: restores data from a backup set. If you set this parameter to 0, you must also specify the **BackupSetId** parameter.
        # *   **1**: restores data to a point in time. If you set this parameter to 1, you must also specify the **RestoreTime**, **SourceRegion**, and **SourceDBInstanceName** parameters.
        # 
        # Default value: **0**.
        # 
        # This parameter is required.
        self.restore_type = restore_type
        # The ID of the source instance if you want to restore data to a point in time.
        # 
        # >  This parameter must be specified when the **RestoreType** parameter is set to **1**.
        self.source_dbinstance_name = source_dbinstance_name
        # The region ID of the source instance if you want to restore data to a point in time.
        # 
        # > If you set **RestoreType** to **1**, you must also specify this parameter.
        self.source_region = source_region

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backup_set_id is not None:
            result['BackupSetId'] = self.backup_set_id

        if self.dbinstance_class is not None:
            result['DBInstanceClass'] = self.dbinstance_class

        if self.dbinstance_storage is not None:
            result['DBInstanceStorage'] = self.dbinstance_storage

        if self.engine is not None:
            result['Engine'] = self.engine

        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.restore_time is not None:
            result['RestoreTime'] = self.restore_time

        if self.restore_type is not None:
            result['RestoreType'] = self.restore_type

        if self.source_dbinstance_name is not None:
            result['SourceDBInstanceName'] = self.source_dbinstance_name

        if self.source_region is not None:
            result['SourceRegion'] = self.source_region

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupSetId') is not None:
            self.backup_set_id = m.get('BackupSetId')

        if m.get('DBInstanceClass') is not None:
            self.dbinstance_class = m.get('DBInstanceClass')

        if m.get('DBInstanceStorage') is not None:
            self.dbinstance_storage = m.get('DBInstanceStorage')

        if m.get('Engine') is not None:
            self.engine = m.get('Engine')

        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('RestoreTime') is not None:
            self.restore_time = m.get('RestoreTime')

        if m.get('RestoreType') is not None:
            self.restore_type = m.get('RestoreType')

        if m.get('SourceDBInstanceName') is not None:
            self.source_dbinstance_name = m.get('SourceDBInstanceName')

        if m.get('SourceRegion') is not None:
            self.source_region = m.get('SourceRegion')

        return self

