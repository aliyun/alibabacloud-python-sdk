# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ReleaseCallRequest(DaraModel):
    def __init__(
        self,
        channel_id: str = None,
        device_id: str = None,
        instance_id: str = None,
        job_id: str = None,
        user_id: str = None,
    ):
        # Channel ID of the call to hang up. This parameter is optional. If not specified, it defaults to the channel where the agent corresponding to the UserId is located.
        self.channel_id = channel_id
        # Device ID. This parameter is meaningless and can be filled with any value.
        self.device_id = device_id
        # Instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # Call ID.
        # 
        # This parameter is required.
        self.job_id = job_id
        # Agent ID. If not specified, the agent mapped to the current Resource Access Management (RAM) user is used by default.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id

        if self.device_id is not None:
            result['DeviceId'] = self.device_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')

        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

