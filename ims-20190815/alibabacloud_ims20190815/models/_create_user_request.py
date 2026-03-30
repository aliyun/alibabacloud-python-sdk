# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ims20190815 import models as main_models
from darabonba.model import DaraModel

class CreateUserRequest(DaraModel):
    def __init__(
        self,
        comments: str = None,
        display_name: str = None,
        email: str = None,
        mobile_phone: str = None,
        tag: List[main_models.CreateUserRequestTag] = None,
        user_principal_name: str = None,
    ):
        # The description.
        # 
        # The description must be 1 to 128 characters in length.
        self.comments = comments
        # The display name of the RAM user.
        # 
        # The name must be 1 to 24 characters in length.
        # 
        # This parameter is required.
        self.display_name = display_name
        # The email address of the RAM user.
        # 
        # > This parameter is valid only on the China site (aliyun.com).
        self.email = email
        # The mobile number of the RAM user.
        # 
        # Format: Country code-Mobile phone number.
        # 
        # > This parameter is valid only on the China site (aliyun.com).
        self.mobile_phone = mobile_phone
        # The tags. You can specify up to 20 tags.
        self.tag = tag
        # The logon name of the Resource Access Management (RAM) user.
        # 
        # The name is in the format of `<username>@<AccountAlias>.onaliyun.com`. `<username>` indicates the name of the RAM user. `<AccountAlias>.onaliyun.com` indicates the default domain name. For more information about how to query the default domain name, see [GetDefaultDomain](https://help.aliyun.com/document_detail/186720.html).
        # 
        # The value of `UserPrincipalName` must be `1 to 128` characters in length and can contain letters, digits, periods (.), hyphens (-), and underscores (_). The value of `<username>` must be `1 to 64` characters in length.
        # 
        # This parameter is required.
        self.user_principal_name = user_principal_name

    def validate(self):
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.comments is not None:
            result['Comments'] = self.comments

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.email is not None:
            result['Email'] = self.email

        if self.mobile_phone is not None:
            result['MobilePhone'] = self.mobile_phone

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comments') is not None:
            self.comments = m.get('Comments')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('Email') is not None:
            self.email = m.get('Email')

        if m.get('MobilePhone') is not None:
            self.mobile_phone = m.get('MobilePhone')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.CreateUserRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('UserPrincipalName') is not None:
            self.user_principal_name = m.get('UserPrincipalName')

        return self

class CreateUserRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the tag.
        # 
        # The tag key cannot be an empty string. The tag key can be up to 128 characters in length and cannot start with `acs:` or `aliyun`. The tag key cannot contain `http://` or `https://`.
        self.key = key
        # The value of the tag.
        # 
        # The tag value can be an empty string. The tag value can be up to 128 characters in length. The tag value cannot start with `acs:` or contain `http://` or `https://`.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

