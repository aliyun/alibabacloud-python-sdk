# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetPasswordHistoryConfigurationRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        password_history_max_retention: int = None,
        password_history_status: str = None,
    ):
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The number of recent password records to retain. This parameter is required when PasswordHistoryStatus is set to enabled.
        self.password_history_max_retention = password_history_max_retention
        # The status of the password history configuration. Valid values:
        # - enabled: Enabled.
        # - disabled: Disabled.
        # 
        # This parameter is required.
        self.password_history_status = password_history_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.password_history_max_retention is not None:
            result['PasswordHistoryMaxRetention'] = self.password_history_max_retention

        if self.password_history_status is not None:
            result['PasswordHistoryStatus'] = self.password_history_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('PasswordHistoryMaxRetention') is not None:
            self.password_history_max_retention = m.get('PasswordHistoryMaxRetention')

        if m.get('PasswordHistoryStatus') is not None:
            self.password_history_status = m.get('PasswordHistoryStatus')

        return self

