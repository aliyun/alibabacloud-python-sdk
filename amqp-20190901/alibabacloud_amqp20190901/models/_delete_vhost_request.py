# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class DeleteVhostRequest(DaraModel):
    def __init__(
        self,
        console_session_id: str = None,
        instance_id: str = None,
        vhost_name: str = None,
        vhost_names: Dict[str, Any] = None,
    ):
        self.console_session_id = console_session_id
        self.instance_id = instance_id
        self.vhost_name = vhost_name
        self.vhost_names = vhost_names

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

        if self.vhost_name is not None:
            result['VhostName'] = self.vhost_name

        if self.vhost_names is not None:
            result['VhostNames'] = self.vhost_names

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsoleSessionId') is not None:
            self.console_session_id = m.get('ConsoleSessionId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('VhostName') is not None:
            self.vhost_name = m.get('VhostName')

        if m.get('VhostNames') is not None:
            self.vhost_names = m.get('VhostNames')

        return self

