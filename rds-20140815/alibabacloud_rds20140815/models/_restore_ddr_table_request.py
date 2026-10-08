# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RestoreDdrTableRequest(DaraModel):
    def __init__(
        self,
        backup_id: str = None,
        client_token: str = None,
        dbinstance_id: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        restore_time: str = None,
        restore_type: str = None,
        source_dbinstance_name: str = None,
        source_region: str = None,
        table_meta: str = None,
    ):
        # The cross-region backup set ID. You can call the DescribeCrossRegionBackups operation to query the backup set ID.
        # >This parameter is required when **RestoreType** is set to **0**.
        self.backup_id = backup_id
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # The instance ID of the existing instance to which you want to recover data.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        self.owner_id = owner_id
        # The ID of the destination region. You can call the DescribeRegions operation to query region IDs.
        self.region_id = region_id
        # The resource group ID.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The point in time to which you want to restore data. The point in time must be earlier than the current time. Format: <i>yyyy-MM-dd</i>T<i>HH:mm:ss</i>Z (UTC).
        # 
        # >This parameter is required when **RestoreType** is set to **1**.
        self.restore_time = restore_time
        # The restoration method. Valid values:
        # * **0**: restores data from a backup set. You must also specify the **BackupId** parameter.
        # * **1**: restores data to a point in time. You must also specify the **RestoreTime**, **SourceRegion**, and **SourceDBInstanceName** parameters.
        # 
        # Default value: **0**.
        # 
        # This parameter is required.
        self.restore_type = restore_type
        # The instance ID of the source instance from which you want to recover data to a point in time.
        # >This parameter is required when **RestoreType** is set to **1**.
        self.source_dbinstance_name = source_dbinstance_name
        # The region ID of the source instance for point-in-time restoration.
        # >This parameter is required when **RestoreType** is set to **1**.
        self.source_region = source_region
        # The databases and tables that you want to restore. Format:
        # ```[{"type":"db","name":"<Database 1 name>","newname":"<New database 1 name>","tables":[{"type":"table","name":"<Table 1 name in database 1>","newname":"<New table 1 name>"},{"type":"table","name":"<Table 2 name in database 1>","newname":"<New table 2 name>"}]},{"type":"db","name":"<Database 2 name>","newname":"<New database 2 name>","tables":[{"type":"table","name":"<Table 3 name in database 2>","newname":"<New table 3 name>"},{"type":"table","name":"<Table 4 name in database 2>","newname":"<New table 4 name>"}]}]```
        # 
        # This parameter is required.
        self.table_meta = table_meta

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backup_id is not None:
            result['BackupId'] = self.backup_id

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

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

        if self.table_meta is not None:
            result['TableMeta'] = self.table_meta

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupId') is not None:
            self.backup_id = m.get('BackupId')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

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

        if m.get('TableMeta') is not None:
            self.table_meta = m.get('TableMeta')

        return self

