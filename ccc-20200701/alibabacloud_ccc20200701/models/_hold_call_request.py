# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class HoldCallRequest(DaraModel):
    def __init__(
        self,
        channel_id: str = None,
        device_id: str = None,
        instance_id: str = None,
        job_id: str = None,
        music: str = None,
        user_id: str = None,
    ):
        # This parameter is required.
        self.channel_id = channel_id
        self.device_id = device_id
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.job_id = job_id
        self.music = music
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

        if self.music is not None:
            result['Music'] = self.music

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

        if m.get('Music') is not None:
            self.music = m.get('Music')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

