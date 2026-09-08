# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SendDtmfSignalingRequest(DaraModel):
    def __init__(
        self,
        channel_id: str = None,
        device_id: str = None,
        dtmf: str = None,
        instance_id: str = None,
        job_id: str = None,
        user_id: str = None,
    ):
        # The channel ID of the call to which DTMF tones are to be sent.
        # 
        # This parameter is required.
        self.channel_id = channel_id
        # Device ID. This parameter is meaningless and can be filled with any value.
        self.device_id = device_id
        # DTMF key information, which refers to the keys on a dial pad, including 0–9, \\*, and #.
        # 
        # This parameter is required.
        self.dtmf = dtmf
        # Instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The call ID.
        # 
        # This parameter is required.
        self.job_id = job_id
        # The agent ID that sends DTMF.
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

        if self.dtmf is not None:
            result['Dtmf'] = self.dtmf

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

        if m.get('Dtmf') is not None:
            self.dtmf = m.get('Dtmf')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

