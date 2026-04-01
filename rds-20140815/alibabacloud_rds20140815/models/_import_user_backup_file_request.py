# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ImportUserBackupFileRequest(DaraModel):
    def __init__(
        self,
        backup_file: str = None,
        bucket_region: str = None,
        build_replication: bool = None,
        comment: str = None,
        dbinstance_id: str = None,
        engine_version: str = None,
        master_info: str = None,
        mode: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        restore_size: int = None,
        retention: int = None,
        source_info: str = None,
        zone_id: str = None,
    ):
        # A JSON array that consists of the information about the full backup file stored as an object in an OSS bucket. Example: `{"Bucket":"test", "Object":"test/test_db_employees.xb","Location":"ap-southeast-1"}`
        # 
        # The JSON array contains the following fields:
        # 
        # *   **Bucket**: The name of the OSS bucket in which the full backup file is stored as an object. You can call the [GetBucket](https://help.aliyun.com/document_detail/31965.html) operation to query the name of the bucket.
        # *   **Object**: The path of the full backup file that is stored as an object in the OSS bucket. You can call the [GetObject](https://help.aliyun.com/document_detail/31980.html) operation to query the path of the object.
        # *   **Location**: The ID of the region in which the OSS bucket is located. You can call the [GetBucketLocation](https://help.aliyun.com/document_detail/31967.html) operation to query the region of the bucket.
        self.backup_file = backup_file
        # The region ID of the OSS bucket where the full backup file of the self-managed MySQL database is located. You can call the DescribeRegions operation to query the most recent region list.
        self.bucket_region = bucket_region
        self.build_replication = build_replication
        # The description of the full backup file.
        self.comment = comment
        # The instance ID.
        self.dbinstance_id = dbinstance_id
        # The version of the database engine that is run on the self-managed MySQL database and ApsaraDB RDS for MySQL instance. Set the value to **5.7**.
        self.engine_version = engine_version
        self.master_info = master_info
        self.mode = mode
        self.owner_id = owner_id
        # The region ID of the instance. You can call the DescribeRegions operation to query the most recent region list.
        # 
        # > *   The value of this parameter is the ID of the region in which you want to create the instance.
        # > *   The value of this parameter must be consistent with the value of **BucketRegion**.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The resource group ID. You can call the DescribeDBInstanceAttribute operation to query the resource group ID.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The amount of storage that is required to restore the data of the full backup file. Unit: GB.
        # 
        # > *   The default value of this parameter is 5 times the size of the full backup file.
        # > *   The minimum value of this parameter is 20.
        self.restore_size = restore_size
        # The retention period of the full backup file. Unit: days. Valid values: any **non-zero** positive integer.
        self.retention = retention
        self.source_info = source_info
        # The zone ID. You can call the DescribeRegions operation to query the zone ID.
        # 
        # > *   If you specify this parameter, the system creates a snapshot in single-digit seconds, which greatly reduces the time that is required to import the full backup file.
        # > *   When you call the CreateDBInstance operation to create an instance by using the full backup file, the instance is created in the zone that you specify for this parameter.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backup_file is not None:
            result['BackupFile'] = self.backup_file

        if self.bucket_region is not None:
            result['BucketRegion'] = self.bucket_region

        if self.build_replication is not None:
            result['BuildReplication'] = self.build_replication

        if self.comment is not None:
            result['Comment'] = self.comment

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version

        if self.master_info is not None:
            result['MasterInfo'] = self.master_info

        if self.mode is not None:
            result['Mode'] = self.mode

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

        if self.restore_size is not None:
            result['RestoreSize'] = self.restore_size

        if self.retention is not None:
            result['Retention'] = self.retention

        if self.source_info is not None:
            result['SourceInfo'] = self.source_info

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupFile') is not None:
            self.backup_file = m.get('BackupFile')

        if m.get('BucketRegion') is not None:
            self.bucket_region = m.get('BucketRegion')

        if m.get('BuildReplication') is not None:
            self.build_replication = m.get('BuildReplication')

        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')

        if m.get('MasterInfo') is not None:
            self.master_info = m.get('MasterInfo')

        if m.get('Mode') is not None:
            self.mode = m.get('Mode')

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

        if m.get('RestoreSize') is not None:
            self.restore_size = m.get('RestoreSize')

        if m.get('Retention') is not None:
            self.retention = m.get('Retention')

        if m.get('SourceInfo') is not None:
            self.source_info = m.get('SourceInfo')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

