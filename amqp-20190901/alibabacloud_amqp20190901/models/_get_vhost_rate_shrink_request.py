# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetVhostRateShrinkRequest(DaraModel):
    def __init__(
        self,
        console_session_id: str = None,
        instance_id: str = None,
        vhost_names_shrink: str = None,
    ):
        self.console_session_id = console_session_id
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.vhost_names_shrink = vhost_names_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.console_session_id is not None:
            result['ConsoleSessionId'] = self.console_session_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.vhost_names_shrink is not None:
            result['VhostNames'] = self.vhost_names_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsoleSessionId') is not None:
            self.console_session_id = m.get('ConsoleSessionId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('VhostNames') is not None:
            self.vhost_names_shrink = m.get('VhostNames')

        return self

