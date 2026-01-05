# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateDatabaseRequest(DaraModel):
    def __init__(
        self,
        account_name: str = None,
        account_privilege: str = None,
        character_set_name: str = None,
        collate: str = None,
        ctype: str = None,
        dbcluster_id: str = None,
        dbdescription: str = None,
        dbname: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The name of the account that is authorized to access the database. You can call the [DescribeAccounts](https://help.aliyun.com/document_detail/98107.html) operation to query account information.
        # >- You can specify only a standard account. By default, privileged accounts have all permissions on all databases. You do not need to grant privileged accounts the permissions to access the database.
        # >- This parameter is required for PolarDB for PostgreSQL (Compatible with Oracle) clusters or PolarDB for PostgreSQL clusters. This parameter is optional for PolarDB for MySQL clusters.
        self.account_name = account_name
        # The permissions that are granted to the account. Valid values:
        # 
        # *   **ReadWrite**: read and write permissions.
        # *   **ReadOnly**: read-only permissions.
        # *   **DMLOnly**: permissions only to execute DML statements on the database.
        # *   **DDLOnly**: permissions only to execute DDL statements on the database.
        # *   **ReadIndex**: read-only and index permissions.
        # 
        # The default value is **ReadWrite**.
        # 
        # > 
        # 
        # *   This parameter is valid only when the **AccountName** parameter is specified.
        # 
        # *   For a PolarDB for PostgreSQL (Compatible with Oracle) or PolarDB for PostgreSQL cluster, this parameter is optional. If **AccountName** is specified, it is the account of the database owner.
        # 
        # *   For a PolarDB for MySQL cluster, this parameter is optional.
        self.account_privilege = account_privilege
        # The character set that is used by the cluster. For more information, see [Character set tables](https://help.aliyun.com/document_detail/99716.html).
        # 
        # This parameter is required.
        self.character_set_name = character_set_name
        # The language that defines the collation rules in the database.
        # 
        # > 
        # 
        # *   The language must be compatible with the character set that is specified by **CharacterSetName**.
        # 
        # *   This parameter is required for a PolarDB for PostgreSQL (Compatible with Oracle) or PolarDB for PostgreSQL cluster. This parameter is optional for a PolarDB for MySQL cluster. To view the valid values of this parameter, perform the following steps: Log on to the PolarDB console and click the ID of the cluster. In the left-side navigation pane, choose **Settings and Management** > **Databases**. Then, click **Create Database**.
        self.collate = collate
        # The language that indicates the character type of the database.
        # 
        # >- The language must be compatible with the character set that is specified by **CharacterSetName**.
        # >- The value that you specify must be the same as the value of **Collate**.
        # >- This parameter is required for PolarDB for PostgreSQL (Compatible with Oracle) clusters or PolarDB for PostgreSQL clusters. This parameter is optional for PolarDB for MySQL clusters.
        # 
        # To view the valid values for this parameter, perform the following steps: Log on to the PolarDB console and click the ID of a cluster. In the left-side navigation pane, choose **Settings and Management** > **Databases**. Then, click **Create Database**.
        self.ctype = ctype
        # The ID of cluster.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The description of the database. The description must meet the following requirements:
        # 
        # *   It cannot start with `http://` or `https://`.
        # *   It must be 2 to 256 characters in length.
        # 
        # > This parameter is required for a PolarDB for Oracle or PolarDB for PostgreSQL cluster. This parameter is optional for a PolarDB for MySQL cluster.
        self.dbdescription = dbdescription
        # The name of the database. The name must meet the following requirements:
        # 
        # *   The name can contain lowercase letters, digits, hyphens (-), and underscores (_).
        # *   The name must start with a lowercase letter and end with a lowercase letter or a digit. The name must be 1 to 64 characters in length.
        # 
        # > Do not use reserved words as database names, such as `test` or `mysql`.
        # 
        # This parameter is required.
        self.dbname = dbname
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
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

        if self.character_set_name is not None:
            result['CharacterSetName'] = self.character_set_name

        if self.collate is not None:
            result['Collate'] = self.collate

        if self.ctype is not None:
            result['Ctype'] = self.ctype

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.dbdescription is not None:
            result['DBDescription'] = self.dbdescription

        if self.dbname is not None:
            result['DBName'] = self.dbname

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')

        if m.get('AccountPrivilege') is not None:
            self.account_privilege = m.get('AccountPrivilege')

        if m.get('CharacterSetName') is not None:
            self.character_set_name = m.get('CharacterSetName')

        if m.get('Collate') is not None:
            self.collate = m.get('Collate')

        if m.get('Ctype') is not None:
            self.ctype = m.get('Ctype')

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('DBDescription') is not None:
            self.dbdescription = m.get('DBDescription')

        if m.get('DBName') is not None:
            self.dbname = m.get('DBName')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

