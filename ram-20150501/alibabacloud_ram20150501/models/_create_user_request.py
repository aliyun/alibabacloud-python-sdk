# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateUserRequest(DaraModel):
    def __init__(
        self,
        comments: str = None,
        display_name: str = None,
        email: str = None,
        mobile_phone: str = None,
        user_name: str = None,
    ):
        # The description of the RAM user.
        # 
        # The description must be 1 to 128 characters in length.
        self.comments = comments
        # The display name of the RAM user.
        # 
        # The name must be 1 to 128 characters in length.
        self.display_name = display_name
        # The email address of the RAM user.
        # 
        # >  This parameter applies only to the China site (aliyun.com).
        self.email = email
        # The mobile phone number of the RAM user.
        # 
        # Format: \\<Country code>-\\<Mobile phone number>.
        # 
        # >  This parameter applies only to the China site (aliyun.com).
        self.mobile_phone = mobile_phone
        # The name of the RAM user.
        # 
        # The name must be 1 to 64 characters in length, and can contain letters, digits, periods (.), hyphens (-), and underscores (_).
        self.user_name = user_name

    def validate(self):
        pass

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

        if self.user_name is not None:
            result['UserName'] = self.user_name

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

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        return self

