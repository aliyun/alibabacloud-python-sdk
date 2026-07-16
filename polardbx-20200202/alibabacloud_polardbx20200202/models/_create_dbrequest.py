# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateDBRequest(DaraModel):
    def __init__(
        self,
        account_name: str = None,
        account_privilege: str = None,
        charset: str = None,
        dbinstance_name: str = None,
        db_description: str = None,
        db_name: str = None,
        mode: str = None,
        region_id: str = None,
        security_account_name: str = None,
        security_account_password: str = None,
        storage_pool_name: str = None,
    ):
        # The name of the account that is authorized to access the created database.
        # 
        # This parameter is required.
        self.account_name = account_name
        # The permissions granted to the account on the database. Valid values:
        # 
        # - **ReadWrite**: read and write permissions.
        # - **ReadOnly**: read-only permissions.
        # - **DMLOnly**: DML-only permissions.
        # - **DDLOnly**: DDL-only permissions.
        self.account_privilege = account_privilege
        # The character set. Valid values:
        # 
        # - **utf8**
        # - **gbk**
        # - **latin1**
        # - **utf8mb4**.
        # 
        # This parameter is required.
        self.charset = charset
        # The name of the instance.
        # 
        # This parameter is required.
        self.dbinstance_name = dbinstance_name
        # The description of the database.
        self.db_description = db_description
        # The name of the database to create.
        # 
        # This parameter is required.
        self.db_name = db_name
        # The mode of the database. Valid values:
        # 
        # - **auto**: The database supports automatic partitioning. You do not need to specify a partition key when you create a table.
        # - **drds**: The database does not support automatic partitioning. You must use the dedicated sharding syntax to specify sharding keys when you create a table.
        self.mode = mode
        # The region where the instance resides.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The name of the security administrator account.
        # 
        # > If the three-role mode is enabled, this parameter is required. If the three-role mode is not enabled, this parameter is not required.
        self.security_account_name = security_account_name
        # The password of the security administrator account.
        # 
        # > If the three-role mode is enabled, this parameter is required. If the three-role mode is not enabled, this parameter is not required.
        self.security_account_password = security_account_password
        self.storage_pool_name = storage_pool_name

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

        if self.charset is not None:
            result['Charset'] = self.charset

        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name

        if self.db_description is not None:
            result['DbDescription'] = self.db_description

        if self.db_name is not None:
            result['DbName'] = self.db_name

        if self.mode is not None:
            result['Mode'] = self.mode

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.security_account_name is not None:
            result['SecurityAccountName'] = self.security_account_name

        if self.security_account_password is not None:
            result['SecurityAccountPassword'] = self.security_account_password

        if self.storage_pool_name is not None:
            result['StoragePoolName'] = self.storage_pool_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')

        if m.get('AccountPrivilege') is not None:
            self.account_privilege = m.get('AccountPrivilege')

        if m.get('Charset') is not None:
            self.charset = m.get('Charset')

        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')

        if m.get('DbDescription') is not None:
            self.db_description = m.get('DbDescription')

        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')

        if m.get('Mode') is not None:
            self.mode = m.get('Mode')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SecurityAccountName') is not None:
            self.security_account_name = m.get('SecurityAccountName')

        if m.get('SecurityAccountPassword') is not None:
            self.security_account_password = m.get('SecurityAccountPassword')

        if m.get('StoragePoolName') is not None:
            self.storage_pool_name = m.get('StoragePoolName')

        return self

