# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ViewInstanceRecordsRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        region_id: str = None,
        terminal_session_token: str = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id
        self.region_id = region_id
        # This parameter is required.
        self.terminal_session_token = terminal_session_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.terminal_session_token is not None:
            result['TerminalSessionToken'] = self.terminal_session_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('TerminalSessionToken') is not None:
            self.terminal_session_token = m.get('TerminalSessionToken')

        return self

