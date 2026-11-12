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
        # > This parameter is required if you want to restore the destination databases and tables from a backup set. You can call the [DescribeBackups](https://help.aliyun.com/document_detail/98102.html) operation to query the backup set ID.
        # 
        # > To obtain the backup set ID, call the DescribeBackups operation and specify the StartTime and EndTime parameters. Then, call the DescribeMetaList operation to obtain the metadata of the restorable databases and tables. Operation description: Dependency chain description: To obtain the BackupId, you must call the DescribeBackups operation (the StartTime and EndTime parameters are required). To obtain the database and table names required for TableMeta, you must call the DescribeMetaList operation.
        self.backup_id = backup_id
        # The cluster ID.
        # > You can call the [DescribeDBClusters](https://help.aliyun.com/document_detail/98094.html) operation to query the details of all clusters within your account.
        # 
        # > The destination cluster must be in the Running state. You can call the DescribeDBClusterAttribute operation to query the current state. Operation description: Status prerequisite: The cluster must be in the Running state. You can call the DescribeDBClusterAttribute operation to query the current state.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The point in time to which you want to restore the data. Specify the time in the YYYY-MM-DDThh:mmZ format. The time must be in UTC.
        # >* This parameter is required if you want to restore data to a specific point in time.
        # >* You can restore data to any point in time within the last seven days.
        self.restore_time = restore_time
        self.security_token = security_token
        # The JSON string that contains the information about the destination databases and tables to be restored. All values in the database and table information are of the string type.
        # Example: `[
        #    {
        #        "tables":[
        #            {
        #                "name":"testtb",
        #                "type":"table",
        #                "newname":"testtb_restore"
        #            }
        #        ],
        #        "name":"testdb",
        #        "type":"db",
        #        "newname":"testdb_restore"
        #    }
        # ]`.
        # > You can call the [DescribeMetaList](https://help.aliyun.com/document_detail/194770.html) operation to view the details of the databases and tables that can be restored, and fill in the restorable database and table information in the corresponding positions in the preceding example.
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

