# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListVhostRequest(DaraModel):
    def __init__(
        self,
        console_session_id: str = None,
        instance_id: str = None,
        vhost_name_prefix: str = None,
    ):
        self.console_session_id = console_session_id
        self.instance_id = instance_id
        self.vhost_name_prefix = vhost_name_prefix

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

        if self.vhost_name_prefix is not None:
            result['VhostNamePrefix'] = self.vhost_name_prefix

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsoleSessionId') is not None:
            self.console_session_id = m.get('ConsoleSessionId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('VhostNamePrefix') is not None:
            self.vhost_name_prefix = m.get('VhostNamePrefix')

        return self

