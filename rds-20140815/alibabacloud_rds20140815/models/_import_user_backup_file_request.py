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
        # A JSON array that describes the backup file information in the OSS bucket. Example:
        # `{"Bucket":"test", "Object":"test/test_db_employees.xb","Location":"ap-southeast-1"}`
        # 
        # The following list describes the parameters in the array:
        # * **Bucket**: the name of the OSS bucket that stores the backup file. You can call [GetBucket](https://help.aliyun.com/document_detail/31965.html) to query the bucket name.
        # * **Object**: the full path of the backup file in the directory. You can call [GetObject](https://help.aliyun.com/document_detail/31980.html) to query the path.
        # * **Location**: the region ID of the OSS bucket. You can call [GetBucketLocation](https://help.aliyun.com/document_detail/31967.html) to query the region ID.
        self.backup_file = backup_file
        # The region ID of the OSS bucket that stores the backup file of the self-managed MySQL 5.7 database. You can call DescribeRegions to query the region ID.
        self.bucket_region = bucket_region
        # Specifies whether to automatically set up replication. Valid values:
        # - true: automatically sets up replication. The `MasterInfo` parameter is required.
        # - false: does not set up replication.
        # 
        # > This parameter takes effect only for native replication instances. You must specify the `DBInstanceId` parameter when you call this operation.
        self.build_replication = build_replication
        # The description of the user backup to be imported.
        self.comment = comment
        # The instance ID.
        self.dbinstance_id = dbinstance_id
        # The version of the MySQL database engine. Valid values: **5.7** and **8.0**.
        self.engine_version = engine_version
        # A JSON array that contains the master information for setting up MySQL replication (case-sensitive). Example:
        # 
        # ```
        # {"masterIp":"172.20.xx.xx","masterPort":"3306","masterUser":"replica","masterPassword":"W33uopkehBQ="}
        # 
        # ```
        # 
        # The following list describes the parameters in the array:
        # - `masterIp`: the IP address of the primary database.
        # - `masterPort`: the port of the primary database.
        # - `masterUser`: the replication account of the primary database.
        # - `masterPassword`: the password of the replication account for the primary database. The password must be Base64-encoded.
        # 
        # > This parameter takes effect only for native replication instances. You must specify the `DBInstanceId` parameter when you call this operation.
        self.master_info = master_info
        # The import mode. Valid values:
        # 
        # - oss: imports the backup from OSS.
        # - stream: imports the backup over the network.
        self.mode = mode
        self.owner_id = owner_id
        # The region ID of the ApsaraDB RDS instance. You can call DescribeRegions to query the region ID.
        # 
        # > * The value of this parameter specifies the region ID in which you want to create the ApsaraDB RDS instance.
        # > * The value must be the same as the value of the **BucketRegion** parameter.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The resource group ID. You can call DescribeDBInstanceAttribute to query the resource group ID.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The storage space required to restore the user backup. Unit: GB.
        # 
        # > * The default value is five times the size of the backup file.
        # > * The minimum value is 20.
        self.restore_size = restore_size
        # The retention period of the user backup file. Unit: days. The value must be an integer greater than **0**.
        self.retention = retention
        # A JSON array that provides the source information for the full backup (case-sensitive). Example:
        # 
        # ```
        # {"sourceIp":"172.20.xx
        # .xx","sourcePort":"9999"}
        # 
        # ```
        # 
        # The following list describes the parameters in the array:
        # 
        # - `sourceIp`: the source IP address.
        # 
        # - `sourcePort`: the Netcat listening port on the source.
        # 
        # > This parameter takes effect only for native replication instances. You must specify the `DBInstanceId` parameter when you call this operation.
        self.source_info = source_info
        # The zone ID. You can call DescribeRegions to query the zone ID.
        # 
        # > * After you specify a zone, the system creates a second-level snapshot in the zone, which significantly reduces the time required for backup import.
        # > * When you call CreateDBInstance to create an instance from the user backup, this zone is the zone in which the new instance resides.
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

