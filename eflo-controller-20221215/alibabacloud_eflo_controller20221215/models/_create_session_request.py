# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateSessionRequest(DaraModel):
    def __init__(
        self,
        node_id: str = None,
        session_type: str = None,
        start_time: str = None,
    ):
        # The instance ID.
        self.node_id = node_id
        # The type of the session corresponding to the session package.
        self.session_type = session_type
        # The start time. The value is a 13-digit timestamp.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.session_type is not None:
            result['SessionType'] = self.session_type

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('SessionType') is not None:
            self.session_type = m.get('SessionType')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

