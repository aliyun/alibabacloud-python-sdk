# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetSecurityPreferenceShrinkRequest(DaraModel):
    def __init__(
        self,
        allow_user_to_change_password: bool = None,
        allow_user_to_login_with_passkey: bool = None,
        allow_user_to_manage_access_keys: bool = None,
        allow_user_to_manage_mfadevices: bool = None,
        allow_user_to_manage_personal_ding_talk: bool = None,
        enable_save_mfaticket: bool = None,
        login_network_masks: str = None,
        login_session_duration: int = None,
        mfaoperation_for_login: str = None,
        max_idle_days_for_access_keys: int = None,
        max_idle_days_for_users: int = None,
        operation_for_risk_login: str = None,
        verification_types_shrink: str = None,
    ):
        # Specifies whether RAM users can manage their own passwords. Valid values:
        # 
        # - true (default)
        # 
        # - false
        self.allow_user_to_change_password = allow_user_to_change_password
        # Specifies whether RAM users can log on using passkeys. Valid values:
        # 
        # - true (default)
        # 
        # - false
        self.allow_user_to_login_with_passkey = allow_user_to_login_with_passkey
        # Specifies whether RAM users can manage their own AccessKey pairs. Valid values:
        # 
        # - true:
        # 
        # - false (default)
        self.allow_user_to_manage_access_keys = allow_user_to_manage_access_keys
        # Specifies whether RAM users can manage their own MFA devices. Valid values:
        # 
        # - true (default)
        # 
        # - false
        self.allow_user_to_manage_mfadevices = allow_user_to_manage_mfadevices
        # Specifies whether RAM users can attach or detach their personal DingTalk accounts. Valid values:
        # 
        # - true (default)
        # 
        # - false
        self.allow_user_to_manage_personal_ding_talk = allow_user_to_manage_personal_ding_talk
        # Specifies whether to save the multi-factor authentication (MFA) status for seven days after a RAM user logs on using MFA. Valid values:
        # 
        # - true
        # 
        # - false (default)
        self.enable_save_mfaticket = enable_save_mfaticket
        # Specifies the IP addresses or CIDR blocks from which RAM users are allowed to sign in to the Alibaba Cloud console.
        # 
        # - This restriction applies to both password-based and single sign-on (SSO) logons.
        # 
        # - It does not affect API calls made with an AccessKey pair.
        # 
        # - If a mask is not configured, logons are allowed from any IP address.
        # 
        # Separate multiple entries with a semicolon (`;`). For example: 192.168.0.0/16;10.0.0.0/8.
        # 
        # The mask is limited to a maximum of 40 entries and a total length of 512 characters.
        self.login_network_masks = login_network_masks
        # The duration of a logon session for a RAM user.
        # 
        # Valid values: 1 to 24. Unit: hours.
        # 
        # Default value: 6.
        self.login_session_duration = login_session_duration
        # Specifies whether MFA is required for logon. This parameter replaces `EnforceMFAForLogin`. The `EnforceMFAForLogin` parameter is still valid, but using this new parameter is recommended. Valid values:
        # 
        # - mandatory: Enforces MFA for all RAM users. This value corresponds to `true` for the `EnforceMFAForLogin` parameter.
        # 
        # - independent (default): The MFA requirement depends on the configuration of each RAM user. This value corresponds to `false` for the `EnforceMFAForLogin` parameter.
        # 
        # - adaptive: Enforces MFA only for abnormal logons.
        self.mfaoperation_for_login = mfaoperation_for_login
        # The maximum number of days that a RAM user\\"s AccessKey pair can be idle. If an AccessKey pair is not used within the specified period, it is automatically disabled the next day. Valid values:
        # 
        # - 90
        # 
        # - 180
        # 
        # - 365
        # 
        # - 730 (default)
        self.max_idle_days_for_access_keys = max_idle_days_for_access_keys
        # The maximum number of days that a RAM user can be idle. If a RAM user with console logon enabled does not log on within this period, their console logon is automatically disabled the next day. This setting does not apply to single sign-on (SSO) logons. Valid values:
        # 
        # - 90
        # 
        # - 180
        # 
        # - 365
        # 
        # - 730 (default)
        self.max_idle_days_for_users = max_idle_days_for_users
        # This parameter is deprecated.
        self.operation_for_risk_login = operation_for_risk_login
        # The MFA methods.
        self.verification_types_shrink = verification_types_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allow_user_to_change_password is not None:
            result['AllowUserToChangePassword'] = self.allow_user_to_change_password

        if self.allow_user_to_login_with_passkey is not None:
            result['AllowUserToLoginWithPasskey'] = self.allow_user_to_login_with_passkey

        if self.allow_user_to_manage_access_keys is not None:
            result['AllowUserToManageAccessKeys'] = self.allow_user_to_manage_access_keys

        if self.allow_user_to_manage_mfadevices is not None:
            result['AllowUserToManageMFADevices'] = self.allow_user_to_manage_mfadevices

        if self.allow_user_to_manage_personal_ding_talk is not None:
            result['AllowUserToManagePersonalDingTalk'] = self.allow_user_to_manage_personal_ding_talk

        if self.enable_save_mfaticket is not None:
            result['EnableSaveMFATicket'] = self.enable_save_mfaticket

        if self.login_network_masks is not None:
            result['LoginNetworkMasks'] = self.login_network_masks

        if self.login_session_duration is not None:
            result['LoginSessionDuration'] = self.login_session_duration

        if self.mfaoperation_for_login is not None:
            result['MFAOperationForLogin'] = self.mfaoperation_for_login

        if self.max_idle_days_for_access_keys is not None:
            result['MaxIdleDaysForAccessKeys'] = self.max_idle_days_for_access_keys

        if self.max_idle_days_for_users is not None:
            result['MaxIdleDaysForUsers'] = self.max_idle_days_for_users

        if self.operation_for_risk_login is not None:
            result['OperationForRiskLogin'] = self.operation_for_risk_login

        if self.verification_types_shrink is not None:
            result['VerificationTypes'] = self.verification_types_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowUserToChangePassword') is not None:
            self.allow_user_to_change_password = m.get('AllowUserToChangePassword')

        if m.get('AllowUserToLoginWithPasskey') is not None:
            self.allow_user_to_login_with_passkey = m.get('AllowUserToLoginWithPasskey')

        if m.get('AllowUserToManageAccessKeys') is not None:
            self.allow_user_to_manage_access_keys = m.get('AllowUserToManageAccessKeys')

        if m.get('AllowUserToManageMFADevices') is not None:
            self.allow_user_to_manage_mfadevices = m.get('AllowUserToManageMFADevices')

        if m.get('AllowUserToManagePersonalDingTalk') is not None:
            self.allow_user_to_manage_personal_ding_talk = m.get('AllowUserToManagePersonalDingTalk')

        if m.get('EnableSaveMFATicket') is not None:
            self.enable_save_mfaticket = m.get('EnableSaveMFATicket')

        if m.get('LoginNetworkMasks') is not None:
            self.login_network_masks = m.get('LoginNetworkMasks')

        if m.get('LoginSessionDuration') is not None:
            self.login_session_duration = m.get('LoginSessionDuration')

        if m.get('MFAOperationForLogin') is not None:
            self.mfaoperation_for_login = m.get('MFAOperationForLogin')

        if m.get('MaxIdleDaysForAccessKeys') is not None:
            self.max_idle_days_for_access_keys = m.get('MaxIdleDaysForAccessKeys')

        if m.get('MaxIdleDaysForUsers') is not None:
            self.max_idle_days_for_users = m.get('MaxIdleDaysForUsers')

        if m.get('OperationForRiskLogin') is not None:
            self.operation_for_risk_login = m.get('OperationForRiskLogin')

        if m.get('VerificationTypes') is not None:
            self.verification_types_shrink = m.get('VerificationTypes')

        return self

