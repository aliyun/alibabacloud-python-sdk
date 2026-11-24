# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class TranslationTextDelta(DaraModel):
    def __init__(
        self,
        type: str = None,
        event_id: str = None,
        session_id: str = None,
        segment_id: str = None,
        direction: str = None,
        source_language: str = None,
        target_language: str = None,
        text: str = None,
        stash: str = None,
    ):
        self.type = type
        self.event_id = event_id
        self.session_id = session_id
        self.segment_id = segment_id
        self.direction = direction
        self.source_language = source_language
        self.target_language = target_language
        self.text = text
        self.stash = stash

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

        if self.direction is not None:
            result['direction'] = self.direction

        if self.source_language is not None:
            result['source_language'] = self.source_language

        if self.target_language is not None:
            result['target_language'] = self.target_language

        if self.text is not None:
            result['text'] = self.text

        if self.stash is not None:
            result['stash'] = self.stash

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

        if m.get('direction') is not None:
            self.direction = m.get('direction')

        if m.get('source_language') is not None:
            self.source_language = m.get('source_language')

        if m.get('target_language') is not None:
            self.target_language = m.get('target_language')

        if m.get('text') is not None:
            self.text = m.get('text')

        if m.get('stash') is not None:
            self.stash = m.get('stash')

        return self

