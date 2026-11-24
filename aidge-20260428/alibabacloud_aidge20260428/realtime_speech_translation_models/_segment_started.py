# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SegmentStarted(DaraModel):
    def __init__(
        self,
        type: str = None,
        event_id: str = None,
        session_id: str = None,
        segment_id: str = None,
        start_ms: int = None,
    ):
        self.type = type
        self.event_id = event_id
        self.session_id = session_id
        self.segment_id = segment_id
        self.start_ms = start_ms

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.type is not None:
            result['type'] = self.type

        if self.event_id is not None:
            result['event_id'] = self.event_id

        if self.session_id is not None:
            result['session_id'] = self.session_id

        if self.segment_id is not None:
            result['segment_id'] = self.segment_id

        if self.start_ms is not None:
            result['start_ms'] = self.start_ms

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('event_id') is not None:
            self.event_id = m.get('event_id')

        if m.get('session_id') is not None:
            self.session_id = m.get('session_id')

        if m.get('segment_id') is not None:
            self.segment_id = m.get('segment_id')

        if m.get('start_ms') is not None:
            self.start_ms = m.get('start_ms')

        return self

