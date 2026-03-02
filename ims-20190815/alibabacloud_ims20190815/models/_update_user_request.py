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
        new_user_principal_name: str = None,
        user_id: str = None,
        user_principal_name: str = None,
    ):
        self.new_comments = new_comments
        self.new_display_name = new_display_name
        self.new_email = new_email
        self.new_mobile_phone = new_mobile_phone
        self.new_user_principal_name = new_user_principal_name
        self.user_id = user_id
        self.user_principal_name = user_principal_name

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

        if self.new_user_principal_name is not None:
            result['NewUserPrincipalName'] = self.new_user_principal_name

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name

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

        if m.get('NewUserPrincipalName') is not None:
            self.new_user_principal_name = m.get('NewUserPrincipalName')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('UserPrincipalName') is not None:
            self.user_principal_name = m.get('UserPrincipalName')

        return self

