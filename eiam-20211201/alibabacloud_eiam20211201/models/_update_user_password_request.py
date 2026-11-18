# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class UpdateUserPasswordRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        password: str = None,
        password_forced_update_status: str = None,
        user_id: str = None,
        user_notification_channels: List[str] = None,
    ):
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The new password for the account. The password format must comply with the password policy.
        # 
        # This parameter is required.
        self.password = password
        # The forced password update status. This feature is disabled by default. Valid values:
        # - enabled: Enabled.
        # - disabled: Disabled.
        self.password_forced_update_status = password_forced_update_status
        # The account ID.
        # 
        # This parameter is required.
        self.user_id = user_id
        # The list of password notification channels. Valid values:
        # - email: Email.
        # - sms: SMS.
        self.user_notification_channels = user_notification_channels

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.password is not None:
            result['Password'] = self.password

        if self.password_forced_update_status is not None:
            result['PasswordForcedUpdateStatus'] = self.password_forced_update_status

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.user_notification_channels is not None:
            result['UserNotificationChannels'] = self.user_notification_channels

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Password') is not None:
            self.password = m.get('Password')

        if m.get('PasswordForcedUpdateStatus') is not None:
            self.password_forced_update_status = m.get('PasswordForcedUpdateStatus')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('UserNotificationChannels') is not None:
            self.user_notification_channels = m.get('UserNotificationChannels')

        return self

