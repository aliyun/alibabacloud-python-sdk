# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CoachCallRequest(DaraModel):
    def __init__(
        self,
        coached_user_id: str = None,
        device_id: str = None,
        instance_id: str = None,
        job_id: str = None,
        timeout_seconds: int = None,
        user_id: str = None,
    ):
        # Agent ID being coached.
        # 
        # This parameter is required.
        self.coached_user_id = coached_user_id
        # Device ID. This field is meaningless and can be filled with any value.
        self.device_id = device_id
        # Instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # Call ID.
        # 
        # This parameter is required.
        self.job_id = job_id
        # Coaching timeout. If the coaching session is not established within the specified time, the coaching operation is canceled. This field is optional and defaults to 30 seconds.
        self.timeout_seconds = timeout_seconds
        # Agent ID initiating the coaching.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.coached_user_id is not None:
            result['CoachedUserId'] = self.coached_user_id

        if self.device_id is not None:
            result['DeviceId'] = self.device_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.timeout_seconds is not None:
            result['TimeoutSeconds'] = self.timeout_seconds

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CoachedUserId') is not None:
            self.coached_user_id = m.get('CoachedUserId')

        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('TimeoutSeconds') is not None:
            self.timeout_seconds = m.get('TimeoutSeconds')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

