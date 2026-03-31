# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetSecurityPreferenceRequest(DaraModel):
    def __init__(
        self,
        allow_user_to_change_password: bool = None,
        allow_user_to_manage_access_keys: bool = None,
        allow_user_to_manage_mfadevices: bool = None,
        allow_user_to_manage_public_keys: bool = None,
        enable_save_mfaticket: bool = None,
        login_network_masks: str = None,
        login_session_duration: int = None,
    ):
        # Specifies whether RAM users can change their passwords. Valid values:
        # 
        # *   true (default)
        # *   false
        self.allow_user_to_change_password = allow_user_to_change_password
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
        # Specifies whether RAM users can manage their public keys. Valid values:
        # 
        # *   true
        # *   false (default)
        # 
        # >  This parameter is valid only for the Japan site.
        self.allow_user_to_manage_public_keys = allow_user_to_manage_public_keys
        # Specifies whether to remember the multi-factor authentication (MFA) devices of Resource Access Management (RAM) users for seven days. Valid values:
        # 
        # *   true
        # *   false (default)
        self.enable_save_mfaticket = enable_save_mfaticket
        # The subnet mask that specifies the IP addresses from which you can log on to the Alibaba Cloud Management Console. This parameter takes effect on password-based logon and single sign-on (SSO). However, this parameter does not take effect on API calls that are authenticated by using AccessKey pairs.
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
        # Valid values: 1 to 24. Default value: 6. Unit: hours.
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

        if self.allow_user_to_manage_access_keys is not None:
            result['AllowUserToManageAccessKeys'] = self.allow_user_to_manage_access_keys

        if self.allow_user_to_manage_mfadevices is not None:
            result['AllowUserToManageMFADevices'] = self.allow_user_to_manage_mfadevices

        if self.allow_user_to_manage_public_keys is not None:
            result['AllowUserToManagePublicKeys'] = self.allow_user_to_manage_public_keys

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

        if m.get('AllowUserToManageAccessKeys') is not None:
            self.allow_user_to_manage_access_keys = m.get('AllowUserToManageAccessKeys')

        if m.get('AllowUserToManageMFADevices') is not None:
            self.allow_user_to_manage_mfadevices = m.get('AllowUserToManageMFADevices')

        if m.get('AllowUserToManagePublicKeys') is not None:
            self.allow_user_to_manage_public_keys = m.get('AllowUserToManagePublicKeys')

        if m.get('EnableSaveMFATicket') is not None:
            self.enable_save_mfaticket = m.get('EnableSaveMFATicket')

        if m.get('LoginNetworkMasks') is not None:
            self.login_network_masks = m.get('LoginNetworkMasks')

        if m.get('LoginSessionDuration') is not None:
            self.login_session_duration = m.get('LoginSessionDuration')

        return self

