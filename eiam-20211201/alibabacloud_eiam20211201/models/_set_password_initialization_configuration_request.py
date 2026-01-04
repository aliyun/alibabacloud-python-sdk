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
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # Specifies whether to enable forcible password change upon first logon. Valid values:
        # 
        # *   enabled
        # *   disabled
        self.password_forced_update_status = password_forced_update_status
        # The methods for receiving password initialization notifications.
        self.password_initialization_notification_channels = password_initialization_notification_channels
        # Specifies whether to enable password initialization. Valid values:
        # 
        # *   enabled
        # *   disabled
        # 
        # This parameter is required.
        self.password_initialization_status = password_initialization_status
        # The password initialization method. This parameter is required when PasswordInitializationStatus is set to enabled. Set the value to random.
        # 
        # *   random: A randomly generated password is used.
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

