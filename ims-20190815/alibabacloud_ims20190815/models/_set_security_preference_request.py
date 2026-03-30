# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class SetSecurityPreferenceRequest(DaraModel):
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
        verification_types: List[str] = None,
    ):
        # Specifies whether RAM users can change their passwords. Valid values:
        # 
        # *   true (default)
        # *   false
        self.allow_user_to_change_password = allow_user_to_change_password
        # Specifies whether a RAM user can use a passkey for logon. Valid values:
        # 
        # *   true: A RAM user can use a passkey for logon. This is the default value.
        # *   false: A RAM user cannot use a passkey for logon.
        self.allow_user_to_login_with_passkey = allow_user_to_login_with_passkey
        # Specifies whether RAM users can manage their AccessKey pairs. Valid values:
        # 
        # *   true
        # *   false (default)
        self.allow_user_to_manage_access_keys = allow_user_to_manage_access_keys
        # Specifies whether RAM users can manage their MFA devices. Valid values:
        # 
        # *   true (default)
        # *   false
        self.allow_user_to_manage_mfadevices = allow_user_to_manage_mfadevices
        # Specifies whether RAM users can manage their personal DingTalk accounts, such as binding and unbinding of the accounts. Valid values:
        # 
        # *   true (default)
        # *   false
        self.allow_user_to_manage_personal_ding_talk = allow_user_to_manage_personal_ding_talk
        # Specifies whether RAM users can remember the MFA devices for seven days. Valid values:
        # 
        # *   true
        # *   false (default)
        self.enable_save_mfaticket = enable_save_mfaticket
        # The subnet mask that specifies the IP addresses from which you can log on to the Alibaba Cloud Management Console. This parameter takes effect on password-based logon and single sign-on (SSO). This parameter does not take effect on API calls that are authenticated by using AccessKey pairs.
        # 
        # *   If you specify a subnet mask, RAM users can use only the IP addresses in the subnet mask to log on to the Alibaba Cloud Management Console.
        # *   If you do not specify a subnet mask, RAM users can use all IP addresses to log on to the Alibaba Cloud Management Console.
        # 
        # If you need to specify multiple subnet masks, separate the subnet masks with semicolons (;). Example: 192.168.0.0/16;10.0.0.0/8.
        # 
        # You can specify up to 40 subnet masks. The total length of the subnet masks can be a maximum of 512 characters.
        self.login_network_masks = login_network_masks
        # The validity period of the logon session of RAM users.
        # 
        # Valid values: 1 to 24. Unit: hours.
        # 
        # Default value: 6.
        self.login_session_duration = login_session_duration
        # Specifies whether MFA is required for all RAM users when they log on to the Alibaba Cloud Management Console. This parameter is used to replace EnforceMFAForLogin. EnforceMFAForLogin is still valid. However, we recommend that you use MFAOperationForLogin. Valid values:
        # 
        # *   mandatory: MFA is required for all RAM users. If you use EnforceMFAForLogin, set the value to true.
        # *   independent (default): User-specific settings are applied. If you use EnforceMFAForLogin, set the value to false.
        # *   adaptive: MFA is required only for RAM users who initiated unusual logons.
        self.mfaoperation_for_login = mfaoperation_for_login
        self.max_idle_days_for_access_keys = max_idle_days_for_access_keys
        self.max_idle_days_for_users = max_idle_days_for_users
        # Specifies whether to enable MFA for RAM users who initiated unusual logons. Valid values:
        # 
        # *   autonomous (default): yes. MFA is prompted for RAM users who initiated unusual logons. However, the RAM users are allowed to skip MFA.
        # *   enforceVerify: MFA is prompted for RAM users who initiated unusual logons and the RAM users cannot skip MFA.
        self.operation_for_risk_login = operation_for_risk_login
        # The MFA methods.
        self.verification_types = verification_types

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

        if self.verification_types is not None:
            result['VerificationTypes'] = self.verification_types

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
            self.verification_types = m.get('VerificationTypes')

        return self

