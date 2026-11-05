# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetUserRequest(DaraModel):
    def __init__(
        self,
        user_access_key_id: str = None,
        user_id: str = None,
        user_principal_name: str = None,
    ):
        # The AccessKey ID of the Resource Access Management (RAM) user.
        # > You must specify exactly one of the following parameters: `UserPrincipalName`, `UserId`, and `UserAccessKeyId`.
        self.user_access_key_id = user_access_key_id
        # The ID of the Resource Access Management (RAM) user.
        # > You must specify exactly one of the following parameters: `UserPrincipalName`, `UserId`, and `UserAccessKeyId`.
        self.user_id = user_id
        # The logon Resource Access Management (RAM) user.
        # 
        # The format is `<username>@<AccountAlias>.onaliyun.com`, where `<username>` is the Resource Access Management (RAM) user and `<AccountAlias>.onaliyun.com` is the default domain name. 
        # 
        # The `UserPrincipalName` must be 1 to 128 characters in length and can contain letters, digits, periods (.), hyphens (-), and underscores (_). The `<username>` must be 1 to 64 characters in length.
        # 
        # > You must specify exactly one of the following parameters: `UserPrincipalName`, `UserId`, and `UserAccessKeyId`.
        self.user_principal_name = user_principal_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.user_access_key_id is not None:
            result['UserAccessKeyId'] = self.user_access_key_id

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserAccessKeyId') is not None:
            self.user_access_key_id = m.get('UserAccessKeyId')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('UserPrincipalName') is not None:
            self.user_principal_name = m.get('UserPrincipalName')

        return self

