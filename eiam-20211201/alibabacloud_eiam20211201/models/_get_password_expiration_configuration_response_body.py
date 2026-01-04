# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eiam20211201 import models as main_models
from darabonba.model import DaraModel

class GetPasswordExpirationConfigurationResponseBody(DaraModel):
    def __init__(
        self,
        password_expiration_configuration: main_models.GetPasswordExpirationConfigurationResponseBodyPasswordExpirationConfiguration = None,
        request_id: str = None,
    ):
        # The password expiration configurations.
        self.password_expiration_configuration = password_expiration_configuration
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.password_expiration_configuration:
            self.password_expiration_configuration.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.password_expiration_configuration is not None:
            result['PasswordExpirationConfiguration'] = self.password_expiration_configuration.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PasswordExpirationConfiguration') is not None:
            temp_model = main_models.GetPasswordExpirationConfigurationResponseBodyPasswordExpirationConfiguration()
            self.password_expiration_configuration = temp_model.from_map(m.get('PasswordExpirationConfiguration'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetPasswordExpirationConfigurationResponseBodyPasswordExpirationConfiguration(DaraModel):
    def __init__(
        self,
        effective_authentication_source_ids: List[str] = None,
        password_expiration_action: str = None,
        password_expiration_notification_channels: List[str] = None,
        password_expiration_notification_duration: int = None,
        password_expiration_notification_status: str = None,
        password_expiration_status: str = None,
        password_forced_update_duration: int = None,
        password_valid_max_day: int = None,
    ):
        # The list of valid authentication IDs. The default is all ["ia_all"]
        # 
        # ia_all: All. If you fill in this value, you cannot fill in other values
        # 
        # ia_password: Account password login
        # 
        # ia_otp_sms: SMS verification code login method
        # 
        # ia_webauthn: WebAuthn authenticator login method
        # 
        # idp_xxx: Specific identity provider authentication method
        self.effective_authentication_source_ids = effective_authentication_source_ids
        # The action to take when a password expires. Valid values:
        # 
        # *   forbid_login: Prohibit the user from using the password to log on to IDaaS.
        # *   force_update_password: Force the user to change the password.
        # *   remind_update_password: Remind the user to change the password.
        self.password_expiration_action = password_expiration_action
        # The methods for receiving password expiration notifications.
        self.password_expiration_notification_channels = password_expiration_notification_channels
        # The number of days before the expiration date during which password expiration notifications are sent. Unit: day.
        self.password_expiration_notification_duration = password_expiration_notification_duration
        # Indicates whether the password expiration notification feature is enabled. Valid values:
        # 
        # *   enabled
        # *   disabled
        self.password_expiration_notification_status = password_expiration_notification_status
        # Indicates whether the password expiration feature is enabled. Valid values:
        # 
        # *   enabled
        # *   disabled
        self.password_expiration_status = password_expiration_status
        # The number of days before which users must change the password to prevent password expiration. Unit: day.
        self.password_forced_update_duration = password_forced_update_duration
        # The validity period of a password. Unit: day.
        self.password_valid_max_day = password_valid_max_day

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.effective_authentication_source_ids is not None:
            result['EffectiveAuthenticationSourceIds'] = self.effective_authentication_source_ids

        if self.password_expiration_action is not None:
            result['PasswordExpirationAction'] = self.password_expiration_action

        if self.password_expiration_notification_channels is not None:
            result['PasswordExpirationNotificationChannels'] = self.password_expiration_notification_channels

        if self.password_expiration_notification_duration is not None:
            result['PasswordExpirationNotificationDuration'] = self.password_expiration_notification_duration

        if self.password_expiration_notification_status is not None:
            result['PasswordExpirationNotificationStatus'] = self.password_expiration_notification_status

        if self.password_expiration_status is not None:
            result['PasswordExpirationStatus'] = self.password_expiration_status

        if self.password_forced_update_duration is not None:
            result['PasswordForcedUpdateDuration'] = self.password_forced_update_duration

        if self.password_valid_max_day is not None:
            result['PasswordValidMaxDay'] = self.password_valid_max_day

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EffectiveAuthenticationSourceIds') is not None:
            self.effective_authentication_source_ids = m.get('EffectiveAuthenticationSourceIds')

        if m.get('PasswordExpirationAction') is not None:
            self.password_expiration_action = m.get('PasswordExpirationAction')

        if m.get('PasswordExpirationNotificationChannels') is not None:
            self.password_expiration_notification_channels = m.get('PasswordExpirationNotificationChannels')

        if m.get('PasswordExpirationNotificationDuration') is not None:
            self.password_expiration_notification_duration = m.get('PasswordExpirationNotificationDuration')

        if m.get('PasswordExpirationNotificationStatus') is not None:
            self.password_expiration_notification_status = m.get('PasswordExpirationNotificationStatus')

        if m.get('PasswordExpirationStatus') is not None:
            self.password_expiration_status = m.get('PasswordExpirationStatus')

        if m.get('PasswordForcedUpdateDuration') is not None:
            self.password_forced_update_duration = m.get('PasswordForcedUpdateDuration')

        if m.get('PasswordValidMaxDay') is not None:
            self.password_valid_max_day = m.get('PasswordValidMaxDay')

        return self

