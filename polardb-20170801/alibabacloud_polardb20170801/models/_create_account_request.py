# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateAccountRequest(DaraModel):
    def __init__(
        self,
        account_description: str = None,
        account_name: str = None,
        account_password: str = None,
        account_privilege: str = None,
        account_type: str = None,
        client_token: str = None,
        dbcluster_id: str = None,
        dbname: str = None,
        node_type: str = None,
        owner_account: str = None,
        owner_id: int = None,
        priv_for_all_db: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The description of the account. The description must meet the following requirements:
        # 
        # - It cannot start with `http://` or `https://`.
        # 
        # - It must be 2 to 256 characters in length.
        self.account_description = account_description
        # The name of the database account. The name must meet the following requirements:
        # 
        # - It must start with a lowercase letter and end with a letter or a digit.
        # 
        # - It can contain lowercase letters, digits, and underscores (_).
        # 
        # - It must be 2 to 16 characters in length.
        # 
        # - It cannot be a reserved keyword, such as root or admin.
        # 
        # This parameter is required.
        self.account_name = account_name
        # The password of the database account. The password must meet the following requirements:
        # 
        # - It must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters.
        # 
        # - It must be 8 to 32 characters in length.
        # 
        # - The special characters are `!@#$%^&*()_+-=`.
        # 
        # This parameter is required.
        self.account_password = account_password
        # The privilege level to grant on the specified databases. Valid values:
        # 
        # - **ReadWrite**: read and write permissions
        # 
        # - **ReadOnly**: read-only permissions
        # 
        # - **DMLOnly**: DML permissions only
        # 
        # - **DDLOnly**: DDL permissions only
        # 
        # - **ReadIndex**: read-only and index permissions
        # 
        # > * This parameter takes effect only when you specify the `DBName` parameter.
        # >
        # > * If you specify multiple databases in `DBName`, you must specify a corresponding permission for each in `AccountPrivilege`, separated by commas. The `AccountPrivilege` string cannot exceed 900 characters. For example, to grant read and write permissions to database DB1 and read-only permissions to database DB2, set `DBName` to `DB1,DB2` and set `AccountPrivilege` to `ReadWrite,ReadOnly`.
        # >
        # > * This parameter applies only to standard accounts on PolarDB for MySQL clusters.
        self.account_privilege = account_privilege
        # The type of the account. Valid values:
        # 
        # - **Normal**: a standard account.
        # 
        # - **Super**: a privileged account.
        # 
        # > * If you do not specify this parameter, the system creates a **Super** account by default.
        # >
        # > * You can create multiple privileged accounts on PolarDB for PostgreSQL (Oracle-Compatible) and PolarDB for PostgreSQL clusters. A privileged account has more permissions than a standard account. For more information, see [Create database accounts](https://help.aliyun.com/document_detail/68508.html).
        # >
        # > * For a PolarDB for MySQL cluster, you can create only one privileged account. For more information, see [Create database accounts](https://help.aliyun.com/document_detail/68508.html).
        self.account_type = account_type
        # A client-generated token to ensure request idempotency. The token must be unique across requests. It is case-sensitive and can be up to 64 ASCII characters long.
        self.client_token = client_token
        # The cluster ID.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The name of the database that the account can access. To specify multiple databases, separate the database names with a comma (,).
        # 
        # > This parameter applies only to standard accounts on PolarDB for MySQL clusters.
        self.dbname = dbname
        # The type of the node. Valid values:
        # 
        # - **Search**: For creating an account on a PolarDB Search node.
        self.node_type = node_type
        self.owner_account = owner_account
        self.owner_id = owner_id
        # Specifies whether to grant the account permissions on all current and future databases in the cluster. Valid values:
        # 
        # - **0 or do not specify**: The specified permissions are not granted to all databases.
        # 
        # - **1**: Grants the specified permissions to all current and future databases.
        # 
        # > * This parameter takes effect only when you specify the `AccountPrivilege` parameter.
        # >
        # > * If you set this parameter to `1`, the permissions specified in `AccountPrivilege` are granted to all databases.
        self.priv_for_all_db = priv_for_all_db
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_description is not None:
            result['AccountDescription'] = self.account_description

        if self.account_name is not None:
            result['AccountName'] = self.account_name

        if self.account_password is not None:
            result['AccountPassword'] = self.account_password

        if self.account_privilege is not None:
            result['AccountPrivilege'] = self.account_privilege

        if self.account_type is not None:
            result['AccountType'] = self.account_type

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.dbname is not None:
            result['DBName'] = self.dbname

        if self.node_type is not None:
            result['NodeType'] = self.node_type

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.priv_for_all_db is not None:
            result['PrivForAllDB'] = self.priv_for_all_db

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountDescription') is not None:
            self.account_description = m.get('AccountDescription')

        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')

        if m.get('AccountPassword') is not None:
            self.account_password = m.get('AccountPassword')

        if m.get('AccountPrivilege') is not None:
            self.account_privilege = m.get('AccountPrivilege')

        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('DBName') is not None:
            self.dbname = m.get('DBName')

        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PrivForAllDB') is not None:
            self.priv_for_all_db = m.get('PrivForAllDB')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

