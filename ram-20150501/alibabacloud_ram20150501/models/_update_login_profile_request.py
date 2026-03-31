# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateLoginProfileRequest(DaraModel):
    def __init__(
        self,
        mfabind_required: bool = None,
        password: str = None,
        password_reset_required: bool = None,
        user_name: str = None,
    ):
        # Specifies whether a multi-factor authentication (MFA) device must be bound to the RAM user upon logon.
        self.mfabind_required = mfabind_required
        # The logon password of the RAM user. The password must meet the password strength requirements.
        self.password = password
        # Specifies whether the RAM user has to change the password upon logon.
        self.password_reset_required = password_reset_required
        # The name of the RAM user.
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.mfabind_required is not None:
            result['MFABindRequired'] = self.mfabind_required

        if self.password is not None:
            result['Password'] = self.password

        if self.password_reset_required is not None:
            result['PasswordResetRequired'] = self.password_reset_required

        if self.user_name is not None:
            result['UserName'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MFABindRequired') is not None:
            self.mfabind_required = m.get('MFABindRequired')

        if m.get('Password') is not None:
            self.password = m.get('Password')

        if m.get('PasswordResetRequired') is not None:
            self.password_reset_required = m.get('PasswordResetRequired')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        return self

