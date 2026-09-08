# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class MonitorCallRequest(DaraModel):
    def __init__(
        self,
        device_id: str = None,
        instance_id: str = None,
        monitored_user_id: str = None,
        timeout_seconds: int = None,
        user_id: str = None,
    ):
        # Device ID. This parameter is meaningless and can be filled with any value.
        self.device_id = device_id
        # Instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The ID of the agent being monitored.
        # 
        # This parameter is required.
        self.monitored_user_id = monitored_user_id
        # The timeout period for the listening operation, in seconds. If the listening operation does not succeed within the specified time, it is canceled. Normally, the listening operation succeeds immediately. The timeout setting is provided to handle abnormal scenarios. This field is optional and defaults to 30 seconds.
        self.timeout_seconds = timeout_seconds
        # Agent ID.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.device_id is not None:
            result['DeviceId'] = self.device_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.monitored_user_id is not None:
            result['MonitoredUserId'] = self.monitored_user_id

        if self.timeout_seconds is not None:
            result['TimeoutSeconds'] = self.timeout_seconds

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('MonitoredUserId') is not None:
            self.monitored_user_id = m.get('MonitoredUserId')

        if m.get('TimeoutSeconds') is not None:
            self.timeout_seconds = m.get('TimeoutSeconds')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

