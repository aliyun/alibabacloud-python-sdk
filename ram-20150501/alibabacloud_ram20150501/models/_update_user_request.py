# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateUserRequest(DaraModel):
    def __init__(
        self,
        new_comments: str = None,
        new_display_name: str = None,
        new_email: str = None,
        new_mobile_phone: str = None,
        new_user_name: str = None,
        user_name: str = None,
    ):
        # The new description of the RAM user.
        # 
        # The description must be 1 to 128 characters in length.
        self.new_comments = new_comments
        # The new display name of the RAM user.
        # 
        # The name must be 1 to 128 characters in length.
        self.new_display_name = new_display_name
        # The new email address of the RAM user.
        # 
        # >  This parameter applies only to the China site (aliyun.com).
        self.new_email = new_email
        # The new mobile phone number of the RAM user.
        # 
        # Format: \\<Country code>-\\<Mobile phone number>.
        # 
        # >  This parameter applies only to the China site (aliyun.com).
        self.new_mobile_phone = new_mobile_phone
        # The new username of the RAM user.
        # 
        # The username must be 1 to 64 characters in length, and can contain letters, digits, periods (.), hyphens (-), and underscores (_).
        self.new_user_name = new_user_name
        # The username of the RAM user.
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.new_comments is not None:
            result['NewComments'] = self.new_comments

        if self.new_display_name is not None:
            result['NewDisplayName'] = self.new_display_name

        if self.new_email is not None:
            result['NewEmail'] = self.new_email

        if self.new_mobile_phone is not None:
            result['NewMobilePhone'] = self.new_mobile_phone

        if self.new_user_name is not None:
            result['NewUserName'] = self.new_user_name

        if self.user_name is not None:
            result['UserName'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NewComments') is not None:
            self.new_comments = m.get('NewComments')

        if m.get('NewDisplayName') is not None:
            self.new_display_name = m.get('NewDisplayName')

        if m.get('NewEmail') is not None:
            self.new_email = m.get('NewEmail')

        if m.get('NewMobilePhone') is not None:
            self.new_mobile_phone = m.get('NewMobilePhone')

        if m.get('NewUserName') is not None:
            self.new_user_name = m.get('NewUserName')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        return self

