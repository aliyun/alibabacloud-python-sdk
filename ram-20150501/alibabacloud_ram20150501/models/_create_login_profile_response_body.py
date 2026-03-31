# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ram20150501 import models as main_models
from darabonba.model import DaraModel

class CreateLoginProfileResponseBody(DaraModel):
    def __init__(
        self,
        login_profile: main_models.CreateLoginProfileResponseBodyLoginProfile = None,
        request_id: str = None,
    ):
        # The logon configurations of the RAM user.
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
            temp_model = main_models.CreateLoginProfileResponseBodyLoginProfile()
            self.login_profile = temp_model.from_map(m.get('LoginProfile'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class CreateLoginProfileResponseBodyLoginProfile(DaraModel):
    def __init__(
        self,
        create_date: str = None,
        mfabind_required: bool = None,
        password_reset_required: bool = None,
        user_name: str = None,
    ):
        # The creation time.
        self.create_date = create_date
        # Indicates whether an MFA device must be bound to the RAM user.
        self.mfabind_required = mfabind_required
        # Indicates whether the RAM user must change the password upon logon.
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
        if self.create_date is not None:
            result['CreateDate'] = self.create_date

        if self.mfabind_required is not None:
            result['MFABindRequired'] = self.mfabind_required

        if self.password_reset_required is not None:
            result['PasswordResetRequired'] = self.password_reset_required

        if self.user_name is not None:
            result['UserName'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')

        if m.get('MFABindRequired') is not None:
            self.mfabind_required = m.get('MFABindRequired')

        if m.get('PasswordResetRequired') is not None:
            self.password_reset_required = m.get('PasswordResetRequired')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        return self

