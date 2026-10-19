# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CheckRecoveryConditionRequest(DaraModel):
    def __init__(
        self,
        backup_id: str = None,
        database_names: str = None,
        dest_region: str = None,
        engine_version: str = None,
        instance_type: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        restore_time: str = None,
        restore_type: str = None,
        source_dbinstance: str = None,
        src_region: str = None,
    ):
        # The ID of the backup set.
        # 
        # > - You can call the [DescribeBackups](https://help.aliyun.com/document_detail/62172.html) operation to query the backup ID.
        # > - You must specify either this parameter or the **RestoreTime** parameter.
        # > - This parameter is not supported for sharded cluster instances.
        self.backup_id = backup_id
        # The names of the databases to be restored. The value is a JSON array.
        # > If you do not specify this parameter, all databases are restored by default.
        self.database_names = database_names
        # The area where the backup set resides during geo-redundancy recover.
        # 
        # > This parameter is required when the backup recover type is geo-redundancy cloning.
        self.dest_region = dest_region
        # The database version. Valid values:
        # - **8.0**
        # - **7.0**
        # - **6.0**
        # - **5.0**
        # - **4.4**
        # - **4.2**
        # - **4.0**
        self.engine_version = engine_version
        # The instance type. Valid values:
        # - replicate 
        # - sharding
        # 
        # >- This parameter is required when the backup recover type is rebuilding a deleted instance.
        # >- This parameter is required when the backup recover type is geo-redundancy cloning.
        self.instance_type = instance_type
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The point in time to which you want to restore the instance. Specify the time in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
        # 
        # > - The value can be any point in time within the last seven days. The value must be earlier than the current time and later than the creation time of the instance.
        # > - You must specify either this parameter or the **BackupId** parameter.
        self.restore_time = restore_time
        # The backup recover type. Valid values:
        # 
        # >- 0: local backup recover
        # >- 1: local point-in-time recover
        # >- 2: backup recover of a deleted instance using a backup set
        # >- 3: geo-redundancy backup recover using a backup set
        self.restore_type = restore_type
        # The instance ID of the source instance to recover.
        self.source_dbinstance = source_dbinstance
        # The area where the source instance resides.
        # 
        # >- This parameter is required when the backup recover type is rebuilding a deleted instance.
        # >- This parameter is required when the backup recover type is geo-redundancy cloning.
        self.src_region = src_region

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backup_id is not None:
            result['BackupId'] = self.backup_id

        if self.database_names is not None:
            result['DatabaseNames'] = self.database_names

        if self.dest_region is not None:
            result['DestRegion'] = self.dest_region

        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

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

        if self.source_dbinstance is not None:
            result['SourceDBInstance'] = self.source_dbinstance

        if self.src_region is not None:
            result['SrcRegion'] = self.src_region

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupId') is not None:
            self.backup_id = m.get('BackupId')

        if m.get('DatabaseNames') is not None:
            self.database_names = m.get('DatabaseNames')

        if m.get('DestRegion') is not None:
            self.dest_region = m.get('DestRegion')

        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

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

        if m.get('SourceDBInstance') is not None:
            self.source_dbinstance = m.get('SourceDBInstance')

        if m.get('SrcRegion') is not None:
            self.src_region = m.get('SrcRegion')

        return self

