# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateLoginProfileRequest(DaraModel):
    def __init__(
        self,
        mfabind_required: bool = None,
        password: str = None,
        password_reset_required: bool = None,
        status: str = None,
        user_principal_name: str = None,
    ):
        # Specifies whether the RAM user must enable multi-factor authentication (MFA). Valid values:
        # 
        # - true: MFA is required. The RAM user must bind an MFA device at the next logon.
        # 
        # - false (default): MFA is not required.
        self.mfabind_required = mfabind_required
        # The logon password for the RAM user.
        # 
        # The password must meet the password strength requirements.
        self.password = password
        # Specifies whether the RAM user must reset the password at the next logon. Valid values:
        # 
        # - true
        # 
        # - false (default)
        self.password_reset_required = password_reset_required
        # Specifies whether to enable password-based logon for the console. Valid values:
        # 
        # - Active (default): Enables logon.
        # 
        # - Inactive: Disables logon.
        self.status = status
        # The logon name of the RAM user.
        # 
        # This parameter is required.
        self.user_principal_name = user_principal_name

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

        if self.status is not None:
            result['Status'] = self.status

        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MFABindRequired') is not None:
            self.mfabind_required = m.get('MFABindRequired')

        if m.get('Password') is not None:
            self.password = m.get('Password')

        if m.get('PasswordResetRequired') is not None:
            self.password_reset_required = m.get('PasswordResetRequired')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UserPrincipalName') is not None:
            self.user_principal_name = m.get('UserPrincipalName')

        return self

