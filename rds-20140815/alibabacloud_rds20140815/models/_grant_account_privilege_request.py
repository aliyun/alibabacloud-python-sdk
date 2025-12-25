# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GrantAccountPrivilegeRequest(DaraModel):
    def __init__(
        self,
        account_name: str = None,
        account_privilege: str = None,
        dbinstance_id: str = None,
        dbname: str = None,
        resource_owner_id: int = None,
    ):
        # The username of the account.
        # 
        # This parameter is required.
        self.account_name = account_name
        # The permissions that you want to grant to the account. The number of permissions must be the same as the number of databases that you specify for the DBName parameter. You can specify this parameter based on your business requirements. Valid values:
        # 
        # *   **ReadWrite**: read and write permissions
        # *   **ReadOnly**: read-only permissions
        # *   **DDLOnly**: DDL-only permissions
        # *   **DMLOnly**: DML-only permissions
        # *   **DBOwner**: database owner permissions
        # 
        # > 
        # 
        # *   If the instance runs MySQL or MariaDB, you can set this parameter to **ReadWrite**, **ReadOnly**, **DDLOnly**, or **DMLOnly**.
        # 
        # *   If the instance runs SQL Server, you can set this parameter to **ReadWrite**, **ReadOnly**, or **DBOwner**.
        # *   If the instance runs PostgreSQL and uses cloud disks, you can set this parameter to **DBOwner**.
        # 
        # This parameter is required.
        self.account_privilege = account_privilege
        # The ID of the instance.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The name of the database on which you want to grant permissions. Separate multiple database names with commas (,).
        # 
        # This parameter is required.
        self.dbname = dbname
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_name is not None:
            result['AccountName'] = self.account_name

        if self.account_privilege is not None:
            result['AccountPrivilege'] = self.account_privilege

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.dbname is not None:
            result['DBName'] = self.dbname

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')

        if m.get('AccountPrivilege') is not None:
            self.account_privilege = m.get('AccountPrivilege')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('DBName') is not None:
            self.dbname = m.get('DBName')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

