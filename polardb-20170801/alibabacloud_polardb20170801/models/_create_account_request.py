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
        # - Cannot start with `http://` or `https://`.
        # - Is 2 to 256 characters in length.
        self.account_description = account_description
        # The account name. The name must meet the following requirements:
        # 
        # * Starts with a lowercase letter and ends with a letter or digit.
        # * Contains only lowercase letters, digits, or underscores (_).
        # * Is 2 to 16 characters in length.
        # * Cannot use certain reserved usernames such as root or admin.
        # 
        # This parameter is required.
        self.account_name = account_name
        # The account password. The password must meet the following requirements:
        # * Contains at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters.
        # * Is 8 to 32 characters in length.
        # * Special characters include `!@#$%^&*()_+-=`.
        # 
        # This parameter is required.
        self.account_password = account_password
        # The permissions of the account. Valid values: 
        # 
        # * **ReadWrite**: read and write
        # * **ReadOnly**: read-only
        # * **DMLOnly**: DML only
        # * **DDLOnly**: DDL only
        # * **ReadIndex**: read-only and index
        # 
        # >* The DBName parameter must be specified for AccountPrivilege to take effect.
        # >* If you specify multiple database names for the DBName parameter, you must grant the corresponding permissions to each database. Separate multiple permissions with commas (,) and make sure that the total length of the AccountPrivilege string does not exceed 900 characters. For example, to grant read and write permissions on database DB1 and read-only permissions on database DB2, set DBName to `DB1,DB2` and set AccountPrivilege to `ReadWrite,ReadOnly`.
        # > * This parameter is supported only for standard accounts of PolarDB for MySQL clusters.
        self.account_privilege = account_privilege
        # The account type. Valid values:
        # 
        # - **Normal**: standard account. 
        # - **Super**: privileged account. 
        # - **DynamoDB**: DynamoDB account. 
        # 
        # 
        #  
        # > * If this parameter is left empty, a **Super** account is created by default.
        # > * If the cluster is a PolarDB for PostgreSQL (Compatible with Oracle) or PolarDB for PostgreSQL cluster, you can create multiple privileged accounts for each cluster. Privileged accounts have more permissions than standard accounts. For more information, see [Create a database account](https://help.aliyun.com/document_detail/68508.html).
        # > * If the cluster is a PolarDB for MySQL cluster, you can create at most one privileged account for each cluster. Privileged accounts have more permissions than standard accounts. For more information, see [Create a database account](https://help.aliyun.com/document_detail/68508.html).
        # > * DynamoDB accounts are dedicated accounts created for the DynamoDB compatibility feature of PolarDB for PostgreSQL. For more information, see [DynamoDB usage instructions](https://help.aliyun.com/document_detail/2979941.html).
        self.account_type = account_type
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the value. Make sure that the value is unique among different requests. The token is case-sensitive and cannot exceed 64 ASCII characters in length.
        self.client_token = client_token
        # The cluster ID.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The name of the database that the account is authorized to access. You can specify multiple database names separated by commas (,).
        # 
        # > This parameter is supported only for standard accounts of PolarDB for MySQL clusters.
        self.dbname = dbname
        # The node type. Valid values:
        # 
        # - Search: required when creating an account for a PolarDB Search node
        self.node_type = node_type
        self.owner_account = owner_account
        self.owner_id = owner_id
        # Specifies whether to grant permissions on all existing databases and all new databases in the current cluster. Valid values:
        # 
        # - **0 or empty**: does not grant permissions.
        # 
        # - **1**: grants permissions.
        # >* The AccountPrivilege parameter must be specified for this parameter to take effect.
        # >* If this parameter is set to `1`, the permissions specified by AccountPrivilege are granted on all databases.
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

