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
        # The ID of the backup set from which you want to restore data. You can call the DescribeBackups operation to query the IDs of data backup files.
        # 
        # >  This parameter is required when you set the **RestoreType** parameter to **BackupSetID**.
        self.backup_set_id = backup_set_id
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the generated token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # The instance ID. You can call the DescribeDBInstances operation to query the instance ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The name of the database to query. The system implements exact match based on the value of this parameter and returns the name of the matched database and the names of all tables contained in the database.
        # 
        # > If you leave this parameter empty, the system returns all databases that are created on the instance.
        self.get_db_name = get_db_name
        self.owner_id = owner_id
        # The number of the page to return. Valid values: any non-zero positive integer.**** Default value: **1**.
        # 
        # > This parameter only takes effect when you specify the **PageSize** parameter.
        self.page_index = page_index
        # The number of entries to return on each page. Default value: **1**.
        # 
        # > This parameter only takes effect when you specify the **PageIndex** parameter.
        self.page_size = page_size
        # The name of the database to query. The system implements fuzzy match based on the value of this parameter and returns only the name of the matched database.
        # 
        # > For example, if you set the value to `test`, the system returns `testdb1` and `testdb2`. Then, you can specify the **GetDbName** parameter to query tables in the required database.
        self.pattern = pattern
        # The resource group ID.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The point in time to which you want to restore data. The specified point in time must be earlier than the current time. Specify the time in the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time must be in UTC. You can call the DescribeBackups operation to query the restorable time range.
        # 
        # >  This parameter must be specified when the **RestoreType** parameter is set to **RestoreTime**.
        self.restore_time = restore_time
        # The restoration method that you want to use. Valid values:
        # 
        # *   **BackupSetID**: Data is restored from the backup set. If you use this value, you must also specify the **BackupSetID** parameter.
        # *   **RestoreTime**: Data is restored to a specific point in time. If you use this value, you must also specify the **RestoreTime** parameter.
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

