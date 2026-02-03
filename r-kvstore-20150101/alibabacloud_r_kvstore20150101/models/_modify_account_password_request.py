# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyAccountPasswordRequest(DaraModel):
    def __init__(
        self,
        account_name: str = None,
        instance_id: str = None,
        new_account_password: str = None,
        old_account_password: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        security_token: str = None,
        source_biz: str = None,
    ):
        # The username of the account for which you want to change the password. You can call the [DescribeAccounts](https://help.aliyun.com/document_detail/473816.html) operation to query the username of the account.
        # 
        # This parameter is required.
        self.account_name = account_name
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The new password to be set for the account. The password must be 8 to 32 characters in length and contain at least three of the following character types: uppercase letters, lowercase letters, digits, and specific special characters. These special characters include `! @ # $ % ^ & * ( ) _ + - =`
        # 
        # This parameter is required.
        self.new_account_password = new_account_password
        # The current password of the account.
        #  
        # > If you forget your password, you can call the [ResetAccountPassword](https://help.aliyun.com/document_detail/473815.html) operation to reset your password.
        # 
        # This parameter is required.
        self.old_account_password = old_account_password
        self.owner_account = owner_account
        self.owner_id = owner_id
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
        if self.account_name is not None:
            result['AccountName'] = self.account_name

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.new_account_password is not None:
            result['NewAccountPassword'] = self.new_account_password

        if self.old_account_password is not None:
            result['OldAccountPassword'] = self.old_account_password

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

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
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('NewAccountPassword') is not None:
            self.new_account_password = m.get('NewAccountPassword')

        if m.get('OldAccountPassword') is not None:
            self.old_account_password = m.get('OldAccountPassword')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        if m.get('SourceBiz') is not None:
            self.source_biz = m.get('SourceBiz')

        return self

