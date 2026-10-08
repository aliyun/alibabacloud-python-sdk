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
        # The account name. You can call [DescribeAccounts](https://help.aliyun.com/document_detail/610454.html) to query the account name.
        # 
        # This parameter is required.
        self.account_name = account_name
        # The type of account permission. If you specify multiple values for DBName, you must specify the same number of permission types in the same order, separated by commas (,).
        # 
        # The supported permission types vary by database engine. Valid values:
        # > For more information about account permissions, see [MySQL/MariaDB permission list](https://help.aliyun.com/document_detail/146395.html), [SQL Server permission list](https://help.aliyun.com/document_detail/95692.html), and [PostgreSQL permission list](https://help.aliyun.com/document_detail/257684.html).
        # <details>
        # <summary>ApsaraDB RDS for MySQL/ApsaraDB RDS for MariaDB</summary>
        # 
        # - **ReadWrite**: read and write.
        # - **ReadOnly**: read-only.
        # - **DDLOnly**: DDL only.
        # - **DMLOnly**: DML only.
        # 
        # </details>
        # 
        # <details>
        # <summary>ApsaraDB RDS for SQL Server</summary>
        # 
        # - **ReadWrite**: read and write. This permission corresponds to the `db_datawriter` and `db_datareader` database roles in SQL Server.
        # - **ReadOnly**: read-only. This permission corresponds to the `db_datareader` database role in SQL Server.
        # - **DBOwner**: database owner. This permission corresponds to the `db_owner` database role in SQL Server.
        # > For more information about database-level roles, see [Microsoft official documentation](https://learn.microsoft.com/en-us/sql/relational-databases/security/authentication-access/database-level-roles?view=sql-server-ver16).
        # </details>
        # 
        # <details>
        # <summary>ApsaraDB RDS for PostgreSQL</summary>
        # 
        # **DBOwner**: database owner.
        # > For fine-grained permission management, see [Best practices for PostgreSQL permission management](https://help.aliyun.com/document_detail/352149.html).
        # </details>
        # 
        # This parameter is required.
        self.account_privilege = account_privilege
        # The instance ID. You can call [DescribeDBInstances](https://help.aliyun.com/document_detail/610396.html) to query the instance ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The name of the database to which you want to grant access permissions. To grant permissions on multiple databases at a time, separate the database names with commas (,), such as `db1,db2,db3`.
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

