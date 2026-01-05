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
        # *   It cannot start with `http://` or `https://`.
        # *   It must be 2 to 256 characters in length.
        self.account_description = account_description
        # The name of the account. The name must meet the following requirements:
        # 
        # *   It must start with a lowercase letter and end with a letter or a digit.
        # *   It can contain lowercase letters, digits, and underscores (_).
        # *   It must be 2 to 16 characters in length.
        # *   It cannot be root, admin, or another username that is reserved by the system.
        # 
        # This parameter is required.
        self.account_name = account_name
        # The password of the account. The password must meet the following requirements:
        # 
        # *   The password must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters.
        # *   The password must be 8 to 32 characters in length.
        # *   Special characters include `! @ # $ % ^ & * ( ) _ + - =`
        # 
        # This parameter is required.
        self.account_password = account_password
        # The permissions that are granted to the account. Valid values:
        # 
        # *   **ReadWrite**: read and write permissions.
        # *   **ReadOnly**: read-only permissions.
        # *   **DMLOnly**: the permissions to execute only DML statements.
        # *   **DDLOnly**: the permissions to execute only DDL statements.
        # *   **ReadIndex**: the read-only and index permissions.
        # 
        # > 
        # 
        # *   `AccountPrivilege` is valid only after you specify `DBName`.
        # 
        # *   If multiple database names are specified by the `DBName` parameter, you must grant permissions on the databases. Separate multiple permissions with commas (,), and make sure that the length of the value of `AccountPrivilege` does not exceed 900. For example, if you want to grant the account the read and write permissions on DB1 and the read-only permissions on DB2, set `DBName` to `DB1,DB2` and set `AccountPrivilege` to `ReadWrite,ReadOnly`.
        # 
        # *   This parameter is valid only for standard accounts of PolarDB for MySQL clusters.
        self.account_privilege = account_privilege
        # The type of the account. Valid values:
        # 
        # *   **Normal**: standard account
        # *   **Super**: privileged account.
        # 
        # > 
        # 
        # *   If you leave this parameter empty, the default value **Super** is used.
        # 
        # *   You can create multiple privileged accounts for a PolarDB for PostgreSQL (Compatible with Oracle) cluster or a PolarDB for PostgreSQL cluster. A privileged account has more permissions than a standard account. For more information, see [Create a database account](https://help.aliyun.com/document_detail/68508.html).
        # 
        # *   You can create only one privileged account for a PolarDB for MySQL cluster. A privileged account has more permissions than a standard account. For more information, see [Create a database account](https://help.aliyun.com/document_detail/68508.html).
        self.account_type = account_type
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. The token is case-sensitive.
        self.client_token = client_token
        # The ID of cluster.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The name of the database that can be accessed by the account. To enter multiple database names, separate the names with commas (,).
        # 
        # >  This parameter is valid only for standard accounts of PolarDB for MySQL clusters.
        self.dbname = dbname
        self.node_type = node_type
        self.owner_account = owner_account
        self.owner_id = owner_id
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

