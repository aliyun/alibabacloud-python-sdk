# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RestoreTableRequest(DaraModel):
    def __init__(
        self,
        backup_id: str = None,
        dbcluster_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        restore_time: str = None,
        security_token: str = None,
        table_meta: str = None,
    ):
        # The backup set ID.
        # 
        # > This parameter is required if you want to restore databases and tables from a backup set. Call the [DescribeBackups](https://help.aliyun.com/document_detail/98102.html) operation to query backup set IDs.
        self.backup_id = backup_id
        # The cluster ID.
        # 
        # > Call the [DescribeDBClusters](https://help.aliyun.com/document_detail/98094.html) operation to query the details of all clusters in your account.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The point in time to which you want to restore data. Specify the time in the YYYY-MM-DDThh:mmZ format. The time must be in Coordinated Universal Time (UTC).
        # 
        # > - This parameter is required if you want to restore data to a specific point in time.
        # >
        # > - Data can be restored to any point in time within the last seven days.
        self.restore_time = restore_time
        self.security_token = security_token
        # A JSON string that specifies the destination databases and tables to restore. All values in the JSON string must be strings.
        # For example: `[ { "tables":[ { "name":"testtb", "type":"table", "newname":"testtb_restore" } ], "name":"testdb", "type":"db", "newname":"testdb_restore" } ]`.
        # 
        # > Call the [DescribeMetaList](https://help.aliyun.com/document_detail/194770.html) operation to query the names of the databases and tables that can be restored. Then, enter the information into the example format.
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

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.restore_time is not None:
            result['RestoreTime'] = self.restore_time

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        if self.table_meta is not None:
            result['TableMeta'] = self.table_meta

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupId') is not None:
            self.backup_id = m.get('BackupId')

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('RestoreTime') is not None:
            self.restore_time = m.get('RestoreTime')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        if m.get('TableMeta') is not None:
            self.table_meta = m.get('TableMeta')

        return self

