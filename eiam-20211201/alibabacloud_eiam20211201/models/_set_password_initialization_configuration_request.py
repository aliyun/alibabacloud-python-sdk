# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class SetPasswordInitializationConfigurationRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        password_forced_update_status: str = None,
        password_initialization_notification_channels: List[str] = None,
        password_initialization_status: str = None,
        password_initialization_type: str = None,
    ):
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The password forced update status. Valid values:
        # - enabled: Enabled.
        # - disabled: Disabled.
        self.password_forced_update_status = password_forced_update_status
        # The list of password initialization notification channels.
        self.password_initialization_notification_channels = password_initialization_notification_channels
        # The password initialization configuration status. Valid values:
        # - enabled: Enabled.
        # - disabled: Disabled.
        # 
        # This parameter is required.
        self.password_initialization_status = password_initialization_status
        # The password initialization method. This parameter is required when PasswordInitializationStatus is set to enabled. Valid values:
        # - random: Random.
        self.password_initialization_type = password_initialization_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.password_forced_update_status is not None:
            result['PasswordForcedUpdateStatus'] = self.password_forced_update_status

        if self.password_initialization_notification_channels is not None:
            result['PasswordInitializationNotificationChannels'] = self.password_initialization_notification_channels

        if self.password_initialization_status is not None:
            result['PasswordInitializationStatus'] = self.password_initialization_status

        if self.password_initialization_type is not None:
            result['PasswordInitializationType'] = self.password_initialization_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('PasswordForcedUpdateStatus') is not None:
            self.password_forced_update_status = m.get('PasswordForcedUpdateStatus')

        if m.get('PasswordInitializationNotificationChannels') is not None:
            self.password_initialization_notification_channels = m.get('PasswordInitializationNotificationChannels')

        if m.get('PasswordInitializationStatus') is not None:
            self.password_initialization_status = m.get('PasswordInitializationStatus')

        if m.get('PasswordInitializationType') is not None:
            self.password_initialization_type = m.get('PasswordInitializationType')

        return self

