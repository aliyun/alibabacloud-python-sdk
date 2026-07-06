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
        allow_user_to_manage_service_credentials: bool = None,
        enable_save_mfaticket: bool = None,
        login_network_masks: str = None,
        login_session_duration: int = None,
        mfaoperation_for_login: str = None,
        max_idle_days_for_access_keys: int = None,
        max_idle_days_for_users: int = None,
        operation_for_risk_login: str = None,
        verification_types_shrink: str = None,
    ):
        # Specifies whether RAM users can change their own passwords. Valid values:
        # 
        # - true (default): Allowed.
        # 
        # - false: Not allowed.
        self.allow_user_to_change_password = allow_user_to_change_password
        # Specifies whether RAM users can use passkeys to log on to the console. Valid values:
        # 
        # - true (default): Allowed.
        # 
        # - false: Not allowed.
        self.allow_user_to_login_with_passkey = allow_user_to_login_with_passkey
        # Specifies whether RAM users can manage their own AccessKeys. Valid values:
        # 
        # - true: Allowed.
        # 
        # - false (default): Not allowed.
        self.allow_user_to_manage_access_keys = allow_user_to_manage_access_keys
        # Specifies whether RAM users can manage their own MFA devices. Valid values:
        # 
        # - true (default): Allowed.
        # 
        # - false: Not allowed.
        self.allow_user_to_manage_mfadevices = allow_user_to_manage_mfadevices
        # Specifies whether RAM users can link or unlink their personal DingTalk accounts. Valid values:
        # 
        # - true (default): Allowed.
        # 
        # - false: Not allowed.
        self.allow_user_to_manage_personal_ding_talk = allow_user_to_manage_personal_ding_talk
        # Specifies whether RAM users can manage their own API keys. Valid values:
        # 
        # - true: Allowed.
        # 
        # - false: Not allowed.
        self.allow_user_to_manage_service_credentials = allow_user_to_manage_service_credentials
        # Specifies whether a RAM user who logs on with multi-factor authentication (MFA) can skip MFA for the next seven days. Valid values:
        # 
        # - true: Allowed.
        # 
        # - false (default): Not allowed.
        self.enable_save_mfaticket = enable_save_mfaticket
        # The IP address mask that is used to log on to the console. This mask applies to password-based logons and single sign-on (SSO) logons, but does not affect API calls that are initiated by using an AccessKey pair.
        # 
        # - If you specify a mask, RAM users can log on to the console only from the specified IP addresses.
        # 
        # - If you do not specify a mask, RAM users can log on to the console from all IP addresses.
        # 
        # If you need to specify multiple masks, separate them with semicolons (`;`). Example: `192.168.0.0/16;10.0.0.0/8`.
        # 
        # You can specify up to 40 masks. The total length cannot exceed 512 characters.
        self.login_network_masks = login_network_masks
        # The session duration of a RAM user who logs on to the console. Unit: hours.
        # 
        # Valid values: 1 to 24.
        # 
        # Default value: 6.
        self.login_session_duration = login_session_duration
        # Specifies the MFA policy for user logon. This parameter replaces `EnforceMFAForLogin`. We recommend that you use this parameter. `EnforceMFAForLogin` is still valid. Valid values:
        # 
        # - `mandatory`: enforces MFA for all RAM users. This is equivalent to setting `EnforceMFAForLogin` to `true`.
        # 
        # - `independent` (default): The MFA settings for each RAM user are not affected. This is equivalent to setting `EnforceMFAForLogin` to `false`.
        # 
        # - `adaptive`: enforces MFA only for unusual logons.
        self.mfaoperation_for_login = mfaoperation_for_login
        # The maximum idle period of the AccessKey pairs of RAM users. An AccessKey pair that is not used for the specified period of time is automatically disabled on the next day. You can set the value to one of the following numbers:
        # 
        # - 90
        # 
        # - 180
        # 
        # - 365
        # 
        # - 730 (default)
        self.max_idle_days_for_access_keys = max_idle_days_for_access_keys
        # The maximum idle period of RAM users. If a RAM user who can log on to the console does not log on to the console for the specified period of time (SSO logons are not included), the console logon feature of the RAM user is disabled on the next day. You can set the value to one of the following numbers:
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

        if self.allow_user_to_manage_service_credentials is not None:
            result['AllowUserToManageServiceCredentials'] = self.allow_user_to_manage_service_credentials

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

        if m.get('AllowUserToManageServiceCredentials') is not None:
            self.allow_user_to_manage_service_credentials = m.get('AllowUserToManageServiceCredentials')

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

