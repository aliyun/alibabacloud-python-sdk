# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class BatchForbidVsStreamRequest(DaraModel):
    def __init__(
        self,
        channel: str = None,
        control_stream_action: str = None,
        domain_name: str = None,
        live_stream_type: str = None,
        oneshot: str = None,
        owner_id: int = None,
        resume_time: str = None,
    ):
        # This parameter is required.
        self.channel = channel
        self.control_stream_action = control_stream_action
        # This parameter is required.
        self.domain_name = domain_name
        # This parameter is required.
        self.live_stream_type = live_stream_type
        self.oneshot = oneshot
        self.owner_id = owner_id
        self.resume_time = resume_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.channel is not None:
            result['Channel'] = self.channel

        if self.control_stream_action is not None:
            result['ControlStreamAction'] = self.control_stream_action

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.live_stream_type is not None:
            result['LiveStreamType'] = self.live_stream_type

        if self.oneshot is not None:
            result['Oneshot'] = self.oneshot

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.resume_time is not None:
            result['ResumeTime'] = self.resume_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Channel') is not None:
            self.channel = m.get('Channel')

        if m.get('ControlStreamAction') is not None:
            self.control_stream_action = m.get('ControlStreamAction')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('LiveStreamType') is not None:
            self.live_stream_type = m.get('LiveStreamType')

        if m.get('Oneshot') is not None:
            self.oneshot = m.get('Oneshot')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResumeTime') is not None:
            self.resume_time = m.get('ResumeTime')

        return self

