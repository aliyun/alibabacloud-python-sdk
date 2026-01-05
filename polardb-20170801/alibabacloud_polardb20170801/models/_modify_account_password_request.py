# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyAccountPasswordRequest(DaraModel):
    def __init__(
        self,
        account_name: str = None,
        dbcluster_id: str = None,
        new_account_password: str = None,
        owner_account: str = None,
        owner_id: int = None,
        password_type: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The username of the account.
        # 
        # This parameter is required.
        self.account_name = account_name
        # The cluster ID.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The new password of the account. The new password must meet the following requirements:
        # 
        # *   It must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters.
        # *   It must be 8 to 32 characters in length.
        # *   Special characters include `! @ # $ % ^ & * ( ) _ + - =`
        # 
        # This parameter is required.
        self.new_account_password = new_account_password
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The password type.
        self.password_type = password_type
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

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.new_account_password is not None:
            result['NewAccountPassword'] = self.new_account_password

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.password_type is not None:
            result['PasswordType'] = self.password_type

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('NewAccountPassword') is not None:
            self.new_account_password = m.get('NewAccountPassword')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PasswordType') is not None:
            self.password_type = m.get('PasswordType')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

