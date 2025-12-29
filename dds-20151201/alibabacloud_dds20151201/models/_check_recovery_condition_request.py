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
        # The backup ID.
        # 
        # > *   You can call the [DescribeBackups](https://help.aliyun.com/document_detail/62172.html) operation to query the backup ID.
        # > *   You must specify one of the **RestoreTime** and BackupId parameters.
        # > *   This parameter is not applicable to sharded cluster instances.
        self.backup_id = backup_id
        # The name of the source database. The value is a JSON array.
        # 
        # >  If you do not specify this parameter, all databases are restored by default.
        self.database_names = database_names
        # The region of the backup set used for the cross-region backup and restoration.
        # 
        # >  This parameter is required when you set the RestoreType parameter to 3.
        self.dest_region = dest_region
        # The database engine version of the instance.
        # 
        # *   **6.0**
        # *   **5.0**
        # *   **4.4**
        # *   **4.2**
        # *   **4.0**
        # *   **3.4**
        self.engine_version = engine_version
        # The instance architecture. Valid values:
        # 
        # *   replicate
        # *   sharding
        # 
        # > * This parameter is required when you set the RestoreType parameter to 2.
        # > * This parameter is required when you set the RestoreType parameter to 3.
        self.instance_type = instance_type
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The ID of the resource group to which the instance belongs.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The point in time to which the instance is restored. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
        # 
        # > *   The time can be a point in time within the past seven days. The time must be earlier than the current time, but later than the time when the instance was created.
        # > *   You must specify one of the RestoreTime and **BackupId** parameters.
        self.restore_time = restore_time
        # The restoration type.
        # 
        # > * 0: The data of the source instance is restored to a new instance in the same region.
        # > * 1: The data of the source instance is restored to an earlier point in time.
        # > * 2: The data of a deleted instance is restored to a new instance from the backup set.
        # > * 3: The data of a deleted instance is restored to a new instance in another region from the backup set.
        self.restore_type = restore_type
        # The ID of the source instance.
        self.source_dbinstance = source_dbinstance
        # The region where the source instance resides.
        # 
        # > * This parameter is required when you set the RestoreType parameter to 2.
        # > * This parameter is required when you set the RestoreType parameter to 3.
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

