# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudsso20210515 import models as main_models
from darabonba.model import DaraModel

class GetMFAAuthenticationSettingInfoResponseBody(DaraModel):
    def __init__(
        self,
        mfaauthentication_setting_info: main_models.GetMFAAuthenticationSettingInfoResponseBodyMFAAuthenticationSettingInfo = None,
        request_id: str = None,
    ):
        # The global MFA verification configuration.
        self.mfaauthentication_setting_info = mfaauthentication_setting_info
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.mfaauthentication_setting_info:
            self.mfaauthentication_setting_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.mfaauthentication_setting_info is not None:
            result['MFAAuthenticationSettingInfo'] = self.mfaauthentication_setting_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MFAAuthenticationSettingInfo') is not None:
            temp_model = main_models.GetMFAAuthenticationSettingInfoResponseBodyMFAAuthenticationSettingInfo()
            self.mfaauthentication_setting_info = temp_model.from_map(m.get('MFAAuthenticationSettingInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetMFAAuthenticationSettingInfoResponseBodyMFAAuthenticationSettingInfo(DaraModel):
    def __init__(
        self,
        allowed_verification_types: List[str] = None,
        mfa_authentication_advance_settings: str = None,
        operation_for_risk_login: str = None,
    ):
        self.allowed_verification_types = allowed_verification_types
        # The global MFA verification policy. Valid values:
        # 
        # - Enabled: MFA verification is enabled for all users.
        # - Byuser: MFA verification depends on the independent MFA configuration of each user. For more information about user-specific MFA configuration, see [UpdateUserMFAAuthenticationSettings](https://help.aliyun.com/document_detail/450135.html).
        # - Disabled: MFA verification is disabled for all users.
        # - OnlyRiskyLogin: MFA verification is required only for unusual logon attempts.
        self.mfa_authentication_advance_settings = mfa_authentication_advance_settings
        # The MFA verification policy for unusual logon attempts. Valid values:
        # 
        # - Autonomous: Users can skip MFA binding during unusual logon, but users who have already bound MFA must complete verification.
        # - EnforceVerify: Users are required to bind or verify MFA during unusual logon.
        # 
        # > This parameter is displayed only when MfaAuthenticationAdvanceSettings is set to Byuser or OnlyRiskyLogin.
        self.operation_for_risk_login = operation_for_risk_login

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allowed_verification_types is not None:
            result['AllowedVerificationTypes'] = self.allowed_verification_types

        if self.mfa_authentication_advance_settings is not None:
            result['MfaAuthenticationAdvanceSettings'] = self.mfa_authentication_advance_settings

        if self.operation_for_risk_login is not None:
            result['OperationForRiskLogin'] = self.operation_for_risk_login

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowedVerificationTypes') is not None:
            self.allowed_verification_types = m.get('AllowedVerificationTypes')

        if m.get('MfaAuthenticationAdvanceSettings') is not None:
            self.mfa_authentication_advance_settings = m.get('MfaAuthenticationAdvanceSettings')

        if m.get('OperationForRiskLogin') is not None:
            self.operation_for_risk_login = m.get('OperationForRiskLogin')

        return self

