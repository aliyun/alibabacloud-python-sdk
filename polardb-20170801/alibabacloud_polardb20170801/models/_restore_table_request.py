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
        # The ID of the backup set.
        # 
        # >  You must specify this parameter if you need to restore a database or a table by using a backup set. You can call the [DescribeBackups](https://help.aliyun.com/document_detail/98102.html) operation to query the ID of the backup set.
        self.backup_id = backup_id
        # The cluster ID.
        # 
        # >  You can call the [DescribeDBClusters](https://help.aliyun.com/document_detail/98094.html) operation to query the details of all clusters within your account.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The point in time for the restoration. Specify the time in the ISO 8601 standard in the YYYY-MM-DDThh:mmZ format. The time must be in UTC.
        # 
        # > 
        # 
        # *   You must specify this parameter if you need to restore the database or the table to a point in time.
        # 
        # *   You can restore your cluster to a particular time only over the past seven days.
        self.restore_time = restore_time
        self.security_token = security_token
        # The JSON string that contains the information of the database and the table that you want to restore. All values of the database and table information are of the string type. Example: `[ { "tables":[ { "name":"testtb", "type":"table", "newname":"testtb_restore" } ], "name":"testdb", "type":"db", "newname":"testdb_restore" } ]`.
        # 
        # >  You can call the [DescribeMetaList](https://help.aliyun.com/document_detail/194770.html) operation to query the names and details of databases and tables that can be restored and enter their information into the corresponding locations in the preceding example.
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

