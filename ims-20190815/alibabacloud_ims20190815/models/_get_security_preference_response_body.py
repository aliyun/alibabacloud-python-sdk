# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ims20190815 import models as main_models
from darabonba.model import DaraModel

class GetSecurityPreferenceResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        security_preference: main_models.GetSecurityPreferenceResponseBodySecurityPreference = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The information about security preferences.
        self.security_preference = security_preference

    def validate(self):
        if self.security_preference:
            self.security_preference.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.security_preference is not None:
            result['SecurityPreference'] = self.security_preference.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SecurityPreference') is not None:
            temp_model = main_models.GetSecurityPreferenceResponseBodySecurityPreference()
            self.security_preference = temp_model.from_map(m.get('SecurityPreference'))

        return self

class GetSecurityPreferenceResponseBodySecurityPreference(DaraModel):
    def __init__(
        self,
        access_key_preference: main_models.GetSecurityPreferenceResponseBodySecurityPreferenceAccessKeyPreference = None,
        login_profile_preference: main_models.GetSecurityPreferenceResponseBodySecurityPreferenceLoginProfilePreference = None,
        mfapreference: main_models.GetSecurityPreferenceResponseBodySecurityPreferenceMFAPreference = None,
        max_idle_days: main_models.GetSecurityPreferenceResponseBodySecurityPreferenceMaxIdleDays = None,
        personal_info_preference: main_models.GetSecurityPreferenceResponseBodySecurityPreferencePersonalInfoPreference = None,
        verification_preference: main_models.GetSecurityPreferenceResponseBodySecurityPreferenceVerificationPreference = None,
    ):
        # The AccessKey preference.
        self.access_key_preference = access_key_preference
        # The logon preferences.
        self.login_profile_preference = login_profile_preference
        # The MFA preferences.
        self.mfapreference = mfapreference
        # The configuration of the maximum idle period.
        self.max_idle_days = max_idle_days
        # The personal information preferences.
        self.personal_info_preference = personal_info_preference
        # The preferences for MFA methods.
        self.verification_preference = verification_preference

    def validate(self):
        if self.access_key_preference:
            self.access_key_preference.validate()
        if self.login_profile_preference:
            self.login_profile_preference.validate()
        if self.mfapreference:
            self.mfapreference.validate()
        if self.max_idle_days:
            self.max_idle_days.validate()
        if self.personal_info_preference:
            self.personal_info_preference.validate()
        if self.verification_preference:
            self.verification_preference.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_key_preference is not None:
            result['AccessKeyPreference'] = self.access_key_preference.to_map()

        if self.login_profile_preference is not None:
            result['LoginProfilePreference'] = self.login_profile_preference.to_map()

        if self.mfapreference is not None:
            result['MFAPreference'] = self.mfapreference.to_map()

        if self.max_idle_days is not None:
            result['MaxIdleDays'] = self.max_idle_days.to_map()

        if self.personal_info_preference is not None:
            result['PersonalInfoPreference'] = self.personal_info_preference.to_map()

        if self.verification_preference is not None:
            result['VerificationPreference'] = self.verification_preference.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessKeyPreference') is not None:
            temp_model = main_models.GetSecurityPreferenceResponseBodySecurityPreferenceAccessKeyPreference()
            self.access_key_preference = temp_model.from_map(m.get('AccessKeyPreference'))

        if m.get('LoginProfilePreference') is not None:
            temp_model = main_models.GetSecurityPreferenceResponseBodySecurityPreferenceLoginProfilePreference()
            self.login_profile_preference = temp_model.from_map(m.get('LoginProfilePreference'))

        if m.get('MFAPreference') is not None:
            temp_model = main_models.GetSecurityPreferenceResponseBodySecurityPreferenceMFAPreference()
            self.mfapreference = temp_model.from_map(m.get('MFAPreference'))

        if m.get('MaxIdleDays') is not None:
            temp_model = main_models.GetSecurityPreferenceResponseBodySecurityPreferenceMaxIdleDays()
            self.max_idle_days = temp_model.from_map(m.get('MaxIdleDays'))

        if m.get('PersonalInfoPreference') is not None:
            temp_model = main_models.GetSecurityPreferenceResponseBodySecurityPreferencePersonalInfoPreference()
            self.personal_info_preference = temp_model.from_map(m.get('PersonalInfoPreference'))

        if m.get('VerificationPreference') is not None:
            temp_model = main_models.GetSecurityPreferenceResponseBodySecurityPreferenceVerificationPreference()
            self.verification_preference = temp_model.from_map(m.get('VerificationPreference'))

        return self

class GetSecurityPreferenceResponseBodySecurityPreferenceVerificationPreference(DaraModel):
    def __init__(
        self,
        verification_types: List[str] = None,
    ):
        # The MFA methods.
        self.verification_types = verification_types

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.verification_types is not None:
            result['VerificationTypes'] = self.verification_types

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VerificationTypes') is not None:
            self.verification_types = m.get('VerificationTypes')

        return self

class GetSecurityPreferenceResponseBodySecurityPreferencePersonalInfoPreference(DaraModel):
    def __init__(
        self,
        allow_user_to_manage_personal_ding_talk: bool = None,
    ):
        # Indicates whether RAM users can attach or detach their personal DingTalk accounts. Valid values:
        # 
        # - true
        # 
        # - false
        self.allow_user_to_manage_personal_ding_talk = allow_user_to_manage_personal_ding_talk

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allow_user_to_manage_personal_ding_talk is not None:
            result['AllowUserToManagePersonalDingTalk'] = self.allow_user_to_manage_personal_ding_talk

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowUserToManagePersonalDingTalk') is not None:
            self.allow_user_to_manage_personal_ding_talk = m.get('AllowUserToManagePersonalDingTalk')

        return self

class GetSecurityPreferenceResponseBodySecurityPreferenceMaxIdleDays(DaraModel):
    def __init__(
        self,
        max_idle_days_for_access_keys: int = None,
        max_idle_days_for_users: int = None,
    ):
        # The maximum idle period for the AccessKey pair of a RAM user. If an AccessKey pair remains unused for this period, it is automatically disabled the next day.
        # 
        # Default value: 730.
        # 
        # Unit: days.
        self.max_idle_days_for_access_keys = max_idle_days_for_access_keys
        # The maximum idle period for RAM users. If a RAM user with console logon enabled remains inactive for this period, their console logon is automatically disabled the next day. This does not apply to single sign-on (SSO) logons.
        # 
        # Default value: 730.
        # 
        # Unit: days.
        self.max_idle_days_for_users = max_idle_days_for_users

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_idle_days_for_access_keys is not None:
            result['MaxIdleDaysForAccessKeys'] = self.max_idle_days_for_access_keys

        if self.max_idle_days_for_users is not None:
            result['MaxIdleDaysForUsers'] = self.max_idle_days_for_users

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxIdleDaysForAccessKeys') is not None:
            self.max_idle_days_for_access_keys = m.get('MaxIdleDaysForAccessKeys')

        if m.get('MaxIdleDaysForUsers') is not None:
            self.max_idle_days_for_users = m.get('MaxIdleDaysForUsers')

        return self

class GetSecurityPreferenceResponseBodySecurityPreferenceMFAPreference(DaraModel):
    def __init__(
        self,
        allow_user_to_manage_mfadevices: bool = None,
    ):
        # Indicates whether RAM users can manage their own MFA devices. Valid values:
        # 
        # - true
        # 
        # - false
        self.allow_user_to_manage_mfadevices = allow_user_to_manage_mfadevices

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allow_user_to_manage_mfadevices is not None:
            result['AllowUserToManageMFADevices'] = self.allow_user_to_manage_mfadevices

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowUserToManageMFADevices') is not None:
            self.allow_user_to_manage_mfadevices = m.get('AllowUserToManageMFADevices')

        return self

class GetSecurityPreferenceResponseBodySecurityPreferenceLoginProfilePreference(DaraModel):
    def __init__(
        self,
        allow_user_to_change_password: bool = None,
        allow_user_to_login_with_passkey: bool = None,
        enable_save_mfaticket: bool = None,
        login_network_masks: str = None,
        login_session_duration: int = None,
        mfaoperation_for_login: str = None,
        operation_for_risk_login: str = None,
    ):
        # Indicates whether RAM users can manage their own passwords. Valid values:
        # 
        # - true
        # 
        # - false
        self.allow_user_to_change_password = allow_user_to_change_password
        # Indicates whether RAM users can log on using passkeys. Valid values:
        # 
        # - true
        # 
        # - false
        self.allow_user_to_login_with_passkey = allow_user_to_login_with_passkey
        # Indicates whether to save the multi-factor authentication (MFA) status for seven days after a RAM user logs on using MFA. Valid values:
        # 
        # - true
        # 
        # - false
        self.enable_save_mfaticket = enable_save_mfaticket
        # The the IP addresses or CIDR blocks from which RAM users are allowed to sign in to the Alibaba Cloud console.
        self.login_network_masks = login_network_masks
        # The duration of a logon session for a RAM user. Unit: hours.
        self.login_session_duration = login_session_duration
        # Indicates whether MFA is required for logon. This parameter replaces `EnforceMFAForLogin`. The `EnforceMFAForLogin` parameter is still valid, but using this new parameter is recommended. Valid values:
        # 
        # - mandatory: MFA is required for all RAM users. This value corresponds to `true` for the `EnforceMFAForLogin` parameter.
        # 
        # - independent (default): The MFA configuration of each RAM user is used. This value corresponds to `false` for the `EnforceMFAForLogin` parameter.
        # 
        # - adaptive: MFA is required only for abnormal logons.
        self.mfaoperation_for_login = mfaoperation_for_login
        # Indicates whether to use MFA for secondary authentication during an abnormal logon. Valid values:
        # 
        # - autonomous (default): The secondary authentication can be skipped. The attachment of an MFA device is not required.
        # 
        # - enforceVerify: The secondary authentication is required.
        self.operation_for_risk_login = operation_for_risk_login

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

        if self.enable_save_mfaticket is not None:
            result['EnableSaveMFATicket'] = self.enable_save_mfaticket

        if self.login_network_masks is not None:
            result['LoginNetworkMasks'] = self.login_network_masks

        if self.login_session_duration is not None:
            result['LoginSessionDuration'] = self.login_session_duration

        if self.mfaoperation_for_login is not None:
            result['MFAOperationForLogin'] = self.mfaoperation_for_login

        if self.operation_for_risk_login is not None:
            result['OperationForRiskLogin'] = self.operation_for_risk_login

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowUserToChangePassword') is not None:
            self.allow_user_to_change_password = m.get('AllowUserToChangePassword')

        if m.get('AllowUserToLoginWithPasskey') is not None:
            self.allow_user_to_login_with_passkey = m.get('AllowUserToLoginWithPasskey')

        if m.get('EnableSaveMFATicket') is not None:
            self.enable_save_mfaticket = m.get('EnableSaveMFATicket')

        if m.get('LoginNetworkMasks') is not None:
            self.login_network_masks = m.get('LoginNetworkMasks')

        if m.get('LoginSessionDuration') is not None:
            self.login_session_duration = m.get('LoginSessionDuration')

        if m.get('MFAOperationForLogin') is not None:
            self.mfaoperation_for_login = m.get('MFAOperationForLogin')

        if m.get('OperationForRiskLogin') is not None:
            self.operation_for_risk_login = m.get('OperationForRiskLogin')

        return self

class GetSecurityPreferenceResponseBodySecurityPreferenceAccessKeyPreference(DaraModel):
    def __init__(
        self,
        allow_user_to_manage_access_keys: bool = None,
    ):
        # Indicates whether RAM users can manage their own AccessKey pairs. Valid values:
        # 
        # - true
        # 
        # - false
        self.allow_user_to_manage_access_keys = allow_user_to_manage_access_keys

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allow_user_to_manage_access_keys is not None:
            result['AllowUserToManageAccessKeys'] = self.allow_user_to_manage_access_keys

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowUserToManageAccessKeys') is not None:
            self.allow_user_to_manage_access_keys = m.get('AllowUserToManageAccessKeys')

        return self

