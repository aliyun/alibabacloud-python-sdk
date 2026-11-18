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
        instance_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        parameters: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        security_token: str = None,
        source_biz: str = None,
    ):
        # The description of the account.
        # * It must start with a letter or a Chinese character and cannot start with `http://` or `https://`.
        # * It can contain Chinese characters, letters, digits, underscores (_), and hyphens (-). 
        # * It must be 2 to 256 characters in length.
        self.account_description = account_description
        # The account name. The account name must meet the following requirements:
        # * It must start with a letter and consist of lowercase letters, digits, and underscores (_).
        # * It can be up to 100 characters in length.
        # * It cannot be a <props="china">[reserved word for Redis usernames](https://www.alibabacloud.com/help/en/redis/user-guide/create-and-manage-database-accounts#section-u3q-817-om3)<props="intl">[reserved word for Redis usernames](https://www.alibabacloud.com/help/zh/redis/user-guide/create-and-manage-database-accounts#section-u3q-817-om3).
        # 
        # This parameter is required.
        self.account_name = account_name
        # The password of the account. The password must be 8 to 32 characters in length and must contain at least three of the following character types: uppercase letters, lowercase letters, special characters, and digits. The allowed special characters include `!@#$%^&*()_+-=`.
        # 
        # This parameter is required.
        self.account_password = account_password
        # The permissions of the account. Valid values:
        # * **RoleReadOnly**: read-only permissions.
        # * **RoleReadWrite**: read and write permissions. This is the default value.
        self.account_privilege = account_privilege
        # The account type. Set the value to **Normal**, which indicates a standard account.
        self.account_type = account_type
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The account parameters to modify. The parameters must be in JSON format. The modified values overwrite the original values.
        # >Notice: This parameter is supported only by Tair Serverless KV instances.
        self.parameters = parameters
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.security_token = security_token
        # This parameter is used only for internal maintenance. You do not need to specify this parameter.
        self.source_biz = source_biz

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

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.parameters is not None:
            result['Parameters'] = self.parameters

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        if self.source_biz is not None:
            result['SourceBiz'] = self.source_biz

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

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        if m.get('SourceBiz') is not None:
            self.source_biz = m.get('SourceBiz')

        return self

