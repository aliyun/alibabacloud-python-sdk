# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class SetPasswordExpirationConfigurationRequest(DaraModel):
    def __init__(
        self,
        effective_authentication_source_ids: List[str] = None,
        instance_id: str = None,
        password_expiration_action: str = None,
        password_expiration_notification_channels: List[str] = None,
        password_expiration_notification_duration: int = None,
        password_expiration_notification_status: str = None,
        password_expiration_status: str = None,
        password_forced_update_duration: int = None,
        password_valid_max_day: int = None,
    ):
        # The list of effective authentication source IDs.
        self.effective_authentication_source_ids = effective_authentication_source_ids
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The action to take when a password expires. This parameter is required when PasswordExpirationStatus is set to enabled. Valid values:
        # - forbid_login: Prohibit logon.
        # - force_update_password: Force password change.
        # - remind_update_password: Remind to change password.
        self.password_expiration_action = password_expiration_action
        # The list of password expiration notification channels. This parameter is required when PasswordExpirationNotificationStatus is set to enabled.
        self.password_expiration_notification_channels = password_expiration_notification_channels
        # The password expiration notification time, in days. This parameter is required when PasswordExpirationNotificationStatus is set to enabled.
        self.password_expiration_notification_duration = password_expiration_notification_duration
        # The password expiration notification status. Valid values:
        # - enabled: Enabled.
        # - disabled: Disabled.
        self.password_expiration_notification_status = password_expiration_notification_status
        # The password expiration configuration status. Valid values:
        # - enabled: Enabled.
        # - disabled: Disabled.
        # 
        # This parameter is required.
        self.password_expiration_status = password_expiration_status
        # The forced password change time, in days. The value of this parameter must be greater than the value of PasswordExpirationNotificationDuration.
        self.password_forced_update_duration = password_forced_update_duration
        # The validity period of a password, in days. This parameter is required when PasswordExpirationStatus is set to enabled.
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

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

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

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

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

