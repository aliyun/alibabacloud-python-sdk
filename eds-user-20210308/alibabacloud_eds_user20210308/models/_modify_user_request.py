# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyUserRequest(DaraModel):
    def __init__(
        self,
        business_channel: str = None,
        email: str = None,
        end_user_id: str = None,
        phone: str = None,
    ):
        self.business_channel = business_channel
        # The email address of the convenience user. For a user-activated convenience user, the email address or mobile number must be verified. You can choose to verify the email address or the mobile number. For an administrator-activated convenience user, the email address and mobile number can be left empty.
        self.email = email
        # The name of the user.
        # 
        # This parameter is required.
        self.end_user_id = end_user_id
        # The mobile number of the convenience user. For a user-activated convenience user, the email address or mobile number must be verified. You can choose to verify the email address or the mobile number. For an administrator-activated convenience user, the email address and mobile number can be left empty.
        # 
        # >  Accounts created on the International site (alibabacloud.com) do not support mobile number-based authentication.
        self.phone = phone

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.business_channel is not None:
            result['BusinessChannel'] = self.business_channel

        if self.email is not None:
            result['Email'] = self.email

        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id

        if self.phone is not None:
            result['Phone'] = self.phone

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessChannel') is not None:
            self.business_channel = m.get('BusinessChannel')

        if m.get('Email') is not None:
            self.email = m.get('Email')

        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')

        if m.get('Phone') is not None:
            self.phone = m.get('Phone')

        return self

