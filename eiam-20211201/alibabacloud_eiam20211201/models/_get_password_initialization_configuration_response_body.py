# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eiam20211201 import models as main_models
from darabonba.model import DaraModel

class GetPasswordInitializationConfigurationResponseBody(DaraModel):
    def __init__(
        self,
        password_initialization_configuration: main_models.GetPasswordInitializationConfigurationResponseBodyPasswordInitializationConfiguration = None,
        request_id: str = None,
    ):
        # The password initialization configurations.
        self.password_initialization_configuration = password_initialization_configuration
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.password_initialization_configuration:
            self.password_initialization_configuration.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.password_initialization_configuration is not None:
            result['PasswordInitializationConfiguration'] = self.password_initialization_configuration.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PasswordInitializationConfiguration') is not None:
            temp_model = main_models.GetPasswordInitializationConfigurationResponseBodyPasswordInitializationConfiguration()
            self.password_initialization_configuration = temp_model.from_map(m.get('PasswordInitializationConfiguration'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetPasswordInitializationConfigurationResponseBodyPasswordInitializationConfiguration(DaraModel):
    def __init__(
        self,
        password_forced_update_status: str = None,
        password_initialization_notification_channels: List[str] = None,
        password_initialization_status: str = None,
        password_initialization_type: str = None,
    ):
        # Indicates whether forcible password change upon first logon is enabled. Valid values:
        # 
        # *   enabled
        # *   disabled
        self.password_forced_update_status = password_forced_update_status
        # The methods for receiving password initialization notifications.
        self.password_initialization_notification_channels = password_initialization_notification_channels
        # Indicates whether the password initialization feature is enabled. Valid values:
        # 
        # *   enabled
        # *   disabled
        self.password_initialization_status = password_initialization_status
        # The password initialization method. Set the value to random.
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
        if m.get('PasswordForcedUpdateStatus') is not None:
            self.password_forced_update_status = m.get('PasswordForcedUpdateStatus')

        if m.get('PasswordInitializationNotificationChannels') is not None:
            self.password_initialization_notification_channels = m.get('PasswordInitializationNotificationChannels')

        if m.get('PasswordInitializationStatus') is not None:
            self.password_initialization_status = m.get('PasswordInitializationStatus')

        if m.get('PasswordInitializationType') is not None:
            self.password_initialization_type = m.get('PasswordInitializationType')

        return self

