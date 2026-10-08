# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeMetaListRequest(DaraModel):
    def __init__(
        self,
        backup_set_id: int = None,
        client_token: str = None,
        dbinstance_id: str = None,
        get_db_name: str = None,
        owner_id: int = None,
        page_index: int = None,
        page_size: int = None,
        pattern: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        restore_time: str = None,
        restore_type: str = None,
    ):
        # The ID of the backup set used for the query. You can call DescribeBackups to query the backup set ID.
        # > This parameter is required when **RestoreType** is set to **BackupSetID**.
        self.backup_set_id = backup_set_id
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # The instance ID. You can call DescribeDBInstances to query the instance ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The name of the database to query. This parameter supports exact match and returns the specified database name and all tables in the database.
        # > If you leave this parameter empty, a list of all databases is returned.
        self.get_db_name = get_db_name
        self.owner_id = owner_id
        # The page number. Valid values: greater than **0** and up to the maximum value of Integer. Default value: **1**.
        # > This parameter takes effect only when it is specified together with **PageSize**.
        self.page_index = page_index
        # The number of entries per page. Default value: **1**.
        # > This parameter takes effect only when it is specified together with **PageIndex**.
        self.page_size = page_size
        # The name of the database to query. This parameter supports fuzzy match and returns only the matched database names without table names.
        # > For example, if you specify `test`, the databases `testdb1` and `testdb2` are matched. After you identify the target database, specify the exact database name by using the **GetDbName** parameter to query all tables in the database.
        self.pattern = pattern
        # The resource group ID.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The point in time used for the query. The value must be earlier than the current time. Format: <i>yyyy-MM-dd</i>T<i>HH:mm:ss</i>Z (UTC). You can call DescribeBackups to query available time points.
        # > This parameter is required when **RestoreType** is set to **RestoreTime**.
        self.restore_time = restore_time
        # The restoration method. Valid values:
        # 
        # * **BackupSetID**: Restores data from a backup set. You must also specify the **BackupSetID** parameter.
        # * **RestoreTime**: Restores data to a point in time. You must also specify the **RestoreTime** parameter.
        # 
        # Default value: **BackupSetID**.
        self.restore_type = restore_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backup_set_id is not None:
            result['BackupSetID'] = self.backup_set_id

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.get_db_name is not None:
            result['GetDbName'] = self.get_db_name

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.page_index is not None:
            result['PageIndex'] = self.page_index

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.pattern is not None:
            result['Pattern'] = self.pattern

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupSetID') is not None:
            self.backup_set_id = m.get('BackupSetID')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('GetDbName') is not None:
            self.get_db_name = m.get('GetDbName')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Pattern') is not None:
            self.pattern = m.get('Pattern')

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

        return self

