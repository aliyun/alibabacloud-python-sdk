# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ResumeVsStreamRequest(DaraModel):
    def __init__(
        self,
        app_name: str = None,
        control_stream_action: str = None,
        domain_name: str = None,
        live_stream_type: str = None,
        owner_id: int = None,
        stream_name: str = None,
    ):
        # This parameter is required.
        self.app_name = app_name
        self.control_stream_action = control_stream_action
        # This parameter is required.
        self.domain_name = domain_name
        # This parameter is required.
        self.live_stream_type = live_stream_type
        self.owner_id = owner_id
        # This parameter is required.
        self.stream_name = stream_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.control_stream_action is not None:
            result['ControlStreamAction'] = self.control_stream_action

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.live_stream_type is not None:
            result['LiveStreamType'] = self.live_stream_type

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.stream_name is not None:
            result['StreamName'] = self.stream_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('ControlStreamAction') is not None:
            self.control_stream_action = m.get('ControlStreamAction')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('LiveStreamType') is not None:
            self.live_stream_type = m.get('LiveStreamType')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('StreamName') is not None:
            self.stream_name = m.get('StreamName')

        return self

