# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateAccountRequest(DaraModel):
    def __init__(
        self,
        account_name: str = None,
        account_password: str = None,
        character_type: str = None,
        dbinstance_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The name of the database account. The name must be 4 to 16 characters in length. It can contain lowercase letters, digits, and underscores (_). It must start with a lowercase letter. The account is granted read-only permissions.
        # 
        # This parameter is required.
        self.account_name = account_name
        # The password of the database account. The password must be 8 to 32 characters in length. It can contain at least three types of the following characters: uppercase letters, lowercase letters, digits, and special characters. Special characters include ! # $ % ^ & \\* ( ) _ + - =
        # 
        # This parameter is required.
        self.account_password = account_password
        # The type of the account that you want to create. Valid values:
        # 
        # *   **db** (default): shard account (available)
        # *   **cs**: ConfigServer account
        # *   **normal**: replica set account
        # 
        # >  You can set this parameter only to **db**.
        self.character_type = character_type
        # The cluster ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
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

        if self.account_password is not None:
            result['AccountPassword'] = self.account_password

        if self.character_type is not None:
            result['CharacterType'] = self.character_type

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

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

        if m.get('AccountPassword') is not None:
            self.account_password = m.get('AccountPassword')

        if m.get('CharacterType') is not None:
            self.character_type = m.get('CharacterType')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

