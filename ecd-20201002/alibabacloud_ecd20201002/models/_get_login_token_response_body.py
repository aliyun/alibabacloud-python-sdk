# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, List

from alibabacloud_ecd20201002 import models as main_models
from darabonba.model import DaraModel

class GetLoginTokenResponseBody(DaraModel):
    def __init__(
        self,
        email: str = None,
        end_user_id: str = None,
        industry: str = None,
        keep_alive_token: str = None,
        label: str = None,
        login_token: str = None,
        next_stage: str = None,
        nick_name: str = None,
        office_site_id: str = None,
        office_site_name: str = None,
        password_strategy: main_models.GetLoginTokenResponseBodyPasswordStrategy = None,
        phone: str = None,
        props: Dict[str, str] = None,
        qr_code_png: str = None,
        reason: str = None,
        request_id: str = None,
        risk_verify_info: main_models.GetLoginTokenResponseBodyRiskVerifyInfo = None,
        secret: str = None,
        session_id: str = None,
        tenant_id: int = None,
        window_display_mode: str = None,
        wy_id: str = None,
    ):
        # The email address of the user. This value is returned with the LoginToken after logon.    
        # 
        # - For a convenience user, the email address specified when the convenience user was created is returned.
        # - For an AD user, the value is returned in the format of `username@AD domain name`.
        self.email = email
        # The convenience account username or AD username.
        self.end_user_id = end_user_id
        # > This is an internal field and is not available for public use.
        self.industry = industry
        # The token used to keep the logon session alive. After a successful logon with the keep-alive option enabled, the operation returns a `KeepAliveToken`. If the keep-alive option is not enabled, an empty value is returned.
        self.keep_alive_token = keep_alive_token
        # The property of the convenience user. If the user is an AD user, an empty value is returned.
        self.label = label
        # The logon credential.
        self.login_token = login_token
        # The expected next stage. For example, if the administrator has enabled MFA authentication in the Elastic Desktop Service console, after the username and password authentication is passed (the `ADPassword` stage), this parameter returns `MFAVerify`, indicating that MFA authentication is required.
        # 
        # > For more information about each authentication stage, see the parameter description of the `CurrentStage` request parameter of this operation.
        self.next_stage = next_stage
        self.nick_name = nick_name
        self.office_site_id = office_site_id
        self.office_site_name = office_site_name
        # > This is an internal field and is not available for public use.
        self.password_strategy = password_strategy
        # The phone number of the convenience user. If the user is an AD user, an empty value is returned.
        self.phone = phone
        # > This is an internal field and is not available for public use.
        self.props = props
        # The QR code of the secret key used when attaching a virtual MFA device. The value uses Base64 encoding. This value can be empty and is used in the `MFABind` stage.
        # 
        # > For more information about each authentication stage, see the parameter description of the `CurrentStage` request parameter of this operation.
        self.qr_code_png = qr_code_png
        # > This is an internal field and is not available for public use.
        self.reason = reason
        # The request ID.
        self.request_id = request_id
        # The logon risk identification information.
        self.risk_verify_info = risk_verify_info
        # The secret key used when attaching a virtual MFA device. This value is used in the `MFABind` stage.
        # 
        # > For more information about each authentication stage, see the parameter description of the `CurrentStage` request parameter of this operation.
        self.secret = secret
        # The session ID. This value is returned only when `GetLoginToken` is invoked for the first time within the same session. For subsequent stages that require multiple authentications, pass in this parameter.
        # 
        # > For more information about each authentication stage, see the parameter description of the `CurrentStage` request parameter of this operation.
        self.session_id = session_id
        # The Alibaba Cloud account ID. This value is used for hardware terminal identification.
        self.tenant_id = tenant_id
        # > This is an internal field and is not available for public use.
        self.window_display_mode = window_display_mode
        self.wy_id = wy_id

    def validate(self):
        if self.password_strategy:
            self.password_strategy.validate()
        if self.risk_verify_info:
            self.risk_verify_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.email is not None:
            result['Email'] = self.email

        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id

        if self.industry is not None:
            result['Industry'] = self.industry

        if self.keep_alive_token is not None:
            result['KeepAliveToken'] = self.keep_alive_token

        if self.label is not None:
            result['Label'] = self.label

        if self.login_token is not None:
            result['LoginToken'] = self.login_token

        if self.next_stage is not None:
            result['NextStage'] = self.next_stage

        if self.nick_name is not None:
            result['NickName'] = self.nick_name

        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id

        if self.office_site_name is not None:
            result['OfficeSiteName'] = self.office_site_name

        if self.password_strategy is not None:
            result['PasswordStrategy'] = self.password_strategy.to_map()

        if self.phone is not None:
            result['Phone'] = self.phone

        if self.props is not None:
            result['Props'] = self.props

        if self.qr_code_png is not None:
            result['QrCodePng'] = self.qr_code_png

        if self.reason is not None:
            result['Reason'] = self.reason

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.risk_verify_info is not None:
            result['RiskVerifyInfo'] = self.risk_verify_info.to_map()

        if self.secret is not None:
            result['Secret'] = self.secret

        if self.session_id is not None:
            result['SessionId'] = self.session_id

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        if self.window_display_mode is not None:
            result['WindowDisplayMode'] = self.window_display_mode

        if self.wy_id is not None:
            result['WyId'] = self.wy_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Email') is not None:
            self.email = m.get('Email')

        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')

        if m.get('Industry') is not None:
            self.industry = m.get('Industry')

        if m.get('KeepAliveToken') is not None:
            self.keep_alive_token = m.get('KeepAliveToken')

        if m.get('Label') is not None:
            self.label = m.get('Label')

        if m.get('LoginToken') is not None:
            self.login_token = m.get('LoginToken')

        if m.get('NextStage') is not None:
            self.next_stage = m.get('NextStage')

        if m.get('NickName') is not None:
            self.nick_name = m.get('NickName')

        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')

        if m.get('OfficeSiteName') is not None:
            self.office_site_name = m.get('OfficeSiteName')

        if m.get('PasswordStrategy') is not None:
            temp_model = main_models.GetLoginTokenResponseBodyPasswordStrategy()
            self.password_strategy = temp_model.from_map(m.get('PasswordStrategy'))

        if m.get('Phone') is not None:
            self.phone = m.get('Phone')

        if m.get('Props') is not None:
            self.props = m.get('Props')

        if m.get('QrCodePng') is not None:
            self.qr_code_png = m.get('QrCodePng')

        if m.get('Reason') is not None:
            self.reason = m.get('Reason')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RiskVerifyInfo') is not None:
            temp_model = main_models.GetLoginTokenResponseBodyRiskVerifyInfo()
            self.risk_verify_info = temp_model.from_map(m.get('RiskVerifyInfo'))

        if m.get('Secret') is not None:
            self.secret = m.get('Secret')

        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        if m.get('WindowDisplayMode') is not None:
            self.window_display_mode = m.get('WindowDisplayMode')

        if m.get('WyId') is not None:
            self.wy_id = m.get('WyId')

        return self

class GetLoginTokenResponseBodyRiskVerifyInfo(DaraModel):
    def __init__(
        self,
        email: str = None,
        last_lock_duration: int = None,
        locked: str = None,
        phone: str = None,
    ):
        # The email address used for identity verification when risk verification is triggered.
        self.email = email
        # The account lockout duration.
        self.last_lock_duration = last_lock_duration
        # Indicates whether the account is locked.
        self.locked = locked
        # The phone number used for identity verification when risk verification is triggered.
        self.phone = phone

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.email is not None:
            result['Email'] = self.email

        if self.last_lock_duration is not None:
            result['LastLockDuration'] = self.last_lock_duration

        if self.locked is not None:
            result['Locked'] = self.locked

        if self.phone is not None:
            result['Phone'] = self.phone

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Email') is not None:
            self.email = m.get('Email')

        if m.get('LastLockDuration') is not None:
            self.last_lock_duration = m.get('LastLockDuration')

        if m.get('Locked') is not None:
            self.locked = m.get('Locked')

        if m.get('Phone') is not None:
            self.phone = m.get('Phone')

        return self

class GetLoginTokenResponseBodyPasswordStrategy(DaraModel):
    def __init__(
        self,
        tenant_alternative_chars: List[str] = None,
        tenant_password_length: str = None,
    ):
        # > This is an internal field and is not available for public use.
        self.tenant_alternative_chars = tenant_alternative_chars
        # > This is an internal field and is not available for public use.
        self.tenant_password_length = tenant_password_length

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tenant_alternative_chars is not None:
            result['TenantAlternativeChars'] = self.tenant_alternative_chars

        if self.tenant_password_length is not None:
            result['TenantPasswordLength'] = self.tenant_password_length

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TenantAlternativeChars') is not None:
            self.tenant_alternative_chars = m.get('TenantAlternativeChars')

        if m.get('TenantPasswordLength') is not None:
            self.tenant_password_length = m.get('TenantPasswordLength')

        return self

