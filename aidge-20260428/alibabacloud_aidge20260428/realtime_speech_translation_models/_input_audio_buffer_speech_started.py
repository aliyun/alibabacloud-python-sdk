# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class InputAudioBufferSpeechStarted(DaraModel):
    def __init__(
        self,
        type: str = None,
        event_id: str = None,
        audio_start_ms: int = None,
        item_id: str = None,
    ):
        self.type = type
        self.event_id = event_id
        self.audio_start_ms = audio_start_ms
        self.item_id = item_id

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

        if self.audio_start_ms is not None:
            result['audio_start_ms'] = self.audio_start_ms

        if self.item_id is not None:
            result['item_id'] = self.item_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('event_id') is not None:
            self.event_id = m.get('event_id')

        if m.get('audio_start_ms') is not None:
            self.audio_start_ms = m.get('audio_start_ms')

        if m.get('item_id') is not None:
            self.item_id = m.get('item_id')

        return self

