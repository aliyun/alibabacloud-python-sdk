# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ram20150501 import models as main_models
from darabonba.model import DaraModel

class GetSecurityPreferenceResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        security_preference: main_models.GetSecurityPreferenceResponseBodySecurityPreference = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The security preferences.
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
        public_key_preference: main_models.GetSecurityPreferenceResponseBodySecurityPreferencePublicKeyPreference = None,
    ):
        # The AccessKey pair preference.
        self.access_key_preference = access_key_preference
        # The logon preference.
        self.login_profile_preference = login_profile_preference
        # The multi-factor authentication (MFA) preference.
        self.mfapreference = mfapreference
        # The public key preference.
        # 
        # >  This parameter is valid only for the Japan site.
        self.public_key_preference = public_key_preference

    def validate(self):
        if self.access_key_preference:
            self.access_key_preference.validate()
        if self.login_profile_preference:
            self.login_profile_preference.validate()
        if self.mfapreference:
            self.mfapreference.validate()
        if self.public_key_preference:
            self.public_key_preference.validate()

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

        if self.public_key_preference is not None:
            result['PublicKeyPreference'] = self.public_key_preference.to_map()

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

        if m.get('PublicKeyPreference') is not None:
            temp_model = main_models.GetSecurityPreferenceResponseBodySecurityPreferencePublicKeyPreference()
            self.public_key_preference = temp_model.from_map(m.get('PublicKeyPreference'))

        return self

class GetSecurityPreferenceResponseBodySecurityPreferencePublicKeyPreference(DaraModel):
    def __init__(
        self,
        allow_user_to_manage_public_keys: bool = None,
    ):
        # Indicates whether RAM users can manage their public keys. Valid values:
        # 
        # *   true
        # *   false
        self.allow_user_to_manage_public_keys = allow_user_to_manage_public_keys

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allow_user_to_manage_public_keys is not None:
            result['AllowUserToManagePublicKeys'] = self.allow_user_to_manage_public_keys

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowUserToManagePublicKeys') is not None:
            self.allow_user_to_manage_public_keys = m.get('AllowUserToManagePublicKeys')

        return self

class GetSecurityPreferenceResponseBodySecurityPreferenceMFAPreference(DaraModel):
    def __init__(
        self,
        allow_user_to_manage_mfadevices: bool = None,
    ):
        # Indicates whether RAM users can manage their MFA devices. Valid values:
        # 
        # *   true
        # *   false
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
        enable_save_mfaticket: bool = None,
        login_network_masks: str = None,
        login_session_duration: int = None,
    ):
        # Indicates whether RAM users can change their passwords. Valid values:
        # 
        # *   true
        # *   false
        self.allow_user_to_change_password = allow_user_to_change_password
        # Indicates whether RAM users can save security codes for MFA during logon. Each security code is valid for seven days. Valid values:
        # 
        # *   true
        # *   false
        self.enable_save_mfaticket = enable_save_mfaticket
        # The subnet mask that indicates the IP addresses from which logon to the Alibaba Cloud Management Console is allowed. This parameter applies to password-based logon and single sign-on (SSO). However, this parameter does not apply to API calls that are authenticated based on AccessKey pairs.
        # 
        # *   If you specify a subnet mask, RAM users can use only the IP addresses in the subnet mask to log on to the Alibaba Cloud Management Console.
        # *   If you do not specify a subnet mask, RAM users can use all IP addresses to log on to the Alibaba Cloud Management Console.
        # 
        # If you want to specify more than one subnet mask, separate the masks with semicolons (;). Example: 192.168.0.0/16;10.0.0.0/8.
        self.login_network_masks = login_network_masks
        # The validity period of the logon session of RAM users. Unit: hours.
        self.login_session_duration = login_session_duration

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allow_user_to_change_password is not None:
            result['AllowUserToChangePassword'] = self.allow_user_to_change_password

        if self.enable_save_mfaticket is not None:
            result['EnableSaveMFATicket'] = self.enable_save_mfaticket

        if self.login_network_masks is not None:
            result['LoginNetworkMasks'] = self.login_network_masks

        if self.login_session_duration is not None:
            result['LoginSessionDuration'] = self.login_session_duration

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowUserToChangePassword') is not None:
            self.allow_user_to_change_password = m.get('AllowUserToChangePassword')

        if m.get('EnableSaveMFATicket') is not None:
            self.enable_save_mfaticket = m.get('EnableSaveMFATicket')

        if m.get('LoginNetworkMasks') is not None:
            self.login_network_masks = m.get('LoginNetworkMasks')

        if m.get('LoginSessionDuration') is not None:
            self.login_session_duration = m.get('LoginSessionDuration')

        return self

class GetSecurityPreferenceResponseBodySecurityPreferenceAccessKeyPreference(DaraModel):
    def __init__(
        self,
        allow_user_to_manage_access_keys: bool = None,
    ):
        # Indicates whether Resource Access Management (RAM) users can manage their AccessKey pairs. Valid values:
        # 
        # *   true
        # *   false
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

