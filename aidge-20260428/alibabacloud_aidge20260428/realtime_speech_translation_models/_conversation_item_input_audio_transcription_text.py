# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ConversationItemInputAudioTranscriptionText(DaraModel):
    def __init__(
        self,
        type: str = None,
        event_id: str = None,
        item_id: str = None,
        content_index: int = None,
        text: str = None,
        stash: str = None,
        language: str = None,
        emotion: str = None,
    ):
        self.type = type
        self.event_id = event_id
        self.item_id = item_id
        self.content_index = content_index
        self.text = text
        self.stash = stash
        self.language = language
        self.emotion = emotion

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

        if self.item_id is not None:
            result['item_id'] = self.item_id

        if self.content_index is not None:
            result['content_index'] = self.content_index

        if self.text is not None:
            result['text'] = self.text

        if self.stash is not None:
            result['stash'] = self.stash

        if self.language is not None:
            result['language'] = self.language

        if self.emotion is not None:
            result['emotion'] = self.emotion

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('event_id') is not None:
            self.event_id = m.get('event_id')

        if m.get('item_id') is not None:
            self.item_id = m.get('item_id')

        if m.get('content_index') is not None:
            self.content_index = m.get('content_index')

        if m.get('text') is not None:
            self.text = m.get('text')

        if m.get('stash') is not None:
            self.stash = m.get('stash')

        if m.get('language') is not None:
            self.language = m.get('language')

        if m.get('emotion') is not None:
            self.emotion = m.get('emotion')

        return self

