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
        # The password expiration configuration.
        self.password_expiration_configuration = password_expiration_configuration
        # The request ID.
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
        # The list of effective authentication source IDs. Default value: ["ia_all"].
        # 
        # - ia_all: All authentication sources. If this value is specified, no other values can be specified.
        # - ia_password: Account password logon.
        # - ia_otp_sms: SMS verification code logon.
        # - ia_webauthn: WebAuthn authenticator logon.
        # - idp_xxx: Authentication method of a specific identity provider.
        self.effective_authentication_source_ids = effective_authentication_source_ids
        # The action to take when a password expires. Valid values:
        # 
        # - forbid_login: Forbid logon.
        # - force_update_password: Force password change.
        # - remind_update_password: Remind password change.
        self.password_expiration_action = password_expiration_action
        # The list of password expiration notification channels.
        self.password_expiration_notification_channels = password_expiration_notification_channels
        # The advance notice period before password expiration. Unit: days.
        self.password_expiration_notification_duration = password_expiration_notification_duration
        # The status of password expiration notification. Valid values:
        # 
        # - enabled: Enabled.
        # - disabled: Disabled.
        self.password_expiration_notification_status = password_expiration_notification_status
        # The status of the password expiration configuration. Valid values:
        # 
        # - enabled: Enabled.
        # - disabled: Disabled.
        self.password_expiration_status = password_expiration_status
        # The grace period for forced password change after expiration. Unit: days.
        self.password_forced_update_duration = password_forced_update_duration
        # The maximum validity period of a password. Unit: days.
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

