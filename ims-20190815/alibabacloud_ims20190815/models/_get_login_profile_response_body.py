# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ims20190815 import models as main_models
from darabonba.model import DaraModel

class GetLoginProfileResponseBody(DaraModel):
    def __init__(
        self,
        login_profile: main_models.GetLoginProfileResponseBodyLoginProfile = None,
        request_id: str = None,
    ):
        # The console logon profile.
        self.login_profile = login_profile
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.login_profile:
            self.login_profile.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.login_profile is not None:
            result['LoginProfile'] = self.login_profile.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LoginProfile') is not None:
            temp_model = main_models.GetLoginProfileResponseBodyLoginProfile()
            self.login_profile = temp_model.from_map(m.get('LoginProfile'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetLoginProfileResponseBodyLoginProfile(DaraModel):
    def __init__(
        self,
        auto_disable_login_status: str = None,
        last_login_time: str = None,
        mfabind_required: bool = None,
        password_reset_required: bool = None,
        password_status: str = None,
        status: str = None,
        update_date: str = None,
        user_principal_name: str = None,
    ):
        # Specifies whether console logon is automatically disabled when the idle disablement conditions are met. This feature is enabled by default and cannot be disabled.
        self.auto_disable_login_status = auto_disable_login_status
        # The last console logon time in UTC.
        self.last_login_time = last_login_time
        # Specifies whether the user is required to enable multi-factor authentication (MFA). Valid values:
        # 
        # - false: MFA is not required.
        # - true: MFA is required.
        self.mfabind_required = mfabind_required
        # Specifies whether the Resource Access Management (RAM) user must reset the password upon the next logon. Valid values:
        # 
        # - false: The user is not required to reset the password.
        # - true: The user must reset the password.
        self.password_reset_required = password_reset_required
        # The status of the initial password. An initial password is the password set when console logon is newly created or re-enabled. Valid values:
        # 
        # - "NotInitial": The password is not an initial password.
        # - "InitialValid": The initial password is valid.
        # - "InitialExpired": The initial password has expired.
        self.password_status = password_status
        # Indicates whether console logon is enabled or disabled. Valid values:
        # 
        # - Active: Console logon is enabled.
        # - Inactive: Console logon is disabled.
        self.status = status
        # The update time in UTC.
        self.update_date = update_date
        # The logon name of the Resource Access Management (RAM) user.
        self.user_principal_name = user_principal_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_disable_login_status is not None:
            result['AutoDisableLoginStatus'] = self.auto_disable_login_status

        if self.last_login_time is not None:
            result['LastLoginTime'] = self.last_login_time

        if self.mfabind_required is not None:
            result['MFABindRequired'] = self.mfabind_required

        if self.password_reset_required is not None:
            result['PasswordResetRequired'] = self.password_reset_required

        if self.password_status is not None:
            result['PasswordStatus'] = self.password_status

        if self.status is not None:
            result['Status'] = self.status

        if self.update_date is not None:
            result['UpdateDate'] = self.update_date

        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoDisableLoginStatus') is not None:
            self.auto_disable_login_status = m.get('AutoDisableLoginStatus')

        if m.get('LastLoginTime') is not None:
            self.last_login_time = m.get('LastLoginTime')

        if m.get('MFABindRequired') is not None:
            self.mfabind_required = m.get('MFABindRequired')

        if m.get('PasswordResetRequired') is not None:
            self.password_reset_required = m.get('PasswordResetRequired')

        if m.get('PasswordStatus') is not None:
            self.password_status = m.get('PasswordStatus')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')

        if m.get('UserPrincipalName') is not None:
            self.user_principal_name = m.get('UserPrincipalName')

        return self

