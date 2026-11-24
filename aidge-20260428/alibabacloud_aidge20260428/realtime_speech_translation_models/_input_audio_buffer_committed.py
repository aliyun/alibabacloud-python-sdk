# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class InputAudioBufferCommitted(DaraModel):
    def __init__(
        self,
        type: str = None,
        event_id: str = None,
        session_id: str = None,
        segment_id: str = None,
        caused_by: str = None,
        audio_duration_ms: int = None,
        item_id: str = None,
        previous_item_id: str = None,
    ):
        self.type = type
        self.event_id = event_id
        self.session_id = session_id
        self.segment_id = segment_id
        self.caused_by = caused_by
        self.audio_duration_ms = audio_duration_ms
        self.item_id = item_id
        self.previous_item_id = previous_item_id

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

        if self.caused_by is not None:
            result['caused_by'] = self.caused_by

        if self.audio_duration_ms is not None:
            result['audio_duration_ms'] = self.audio_duration_ms

        if self.item_id is not None:
            result['item_id'] = self.item_id

        if self.previous_item_id is not None:
            result['previous_item_id'] = self.previous_item_id

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

        if m.get('caused_by') is not None:
            self.caused_by = m.get('caused_by')

        if m.get('audio_duration_ms') is not None:
            self.audio_duration_ms = m.get('audio_duration_ms')

        if m.get('item_id') is not None:
            self.item_id = m.get('item_id')

        if m.get('previous_item_id') is not None:
            self.previous_item_id = m.get('previous_item_id')

        return self

