# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateDatabaseZonalRequest(DaraModel):
    def __init__(
        self,
        account_name: str = None,
        account_privilege: str = None,
        character_set_name: str = None,
        client_token: str = None,
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
        # The name of the account that is authorized to access the database.
        self.account_name = account_name
        # The permissions of the account. Valid values:
        # 
        # - ReadWrite: read and write permissions.
        # 
        # - ReadOnly: read-only permissions.
        # 
        # - DMLOnly: DML permissions only.
        # 
        # - DDLOnly: DDL permissions only.
        # 
        # - ReadIndex: read-only and index permissions.
        # 
        # If you do not specify this parameter, the default value is ReadWrite.
        self.account_privilege = account_privilege
        # The character set.
        # 
        # This parameter is required.
        self.character_set_name = character_set_name
        # A client token to ensure request idempotence. The client generates this token. The token must be unique across requests. It is case-sensitive and can be up to 64 ASCII characters long.
        self.client_token = client_token
        # The locale setting. This specifies the collation for the new database.
        self.collate = collate
        # The locale setting. This specifies the character classification for the database.
        self.ctype = ctype
        # The cluster ID.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The description of the database. The description must meet the following requirements:
        # 
        # - It cannot start with `http://` or `https://`.
        # 
        # - It must be 2 to 256 characters in length.
        self.dbdescription = dbdescription
        # The name of the database. The name must meet the following requirements:
        # 
        # - It must consist of lowercase letters, digits, hyphens (-), and underscores (_).
        # 
        # - It must start with a letter and end with a letter or a digit. The name can be up to 64 characters long.
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

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

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

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

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

