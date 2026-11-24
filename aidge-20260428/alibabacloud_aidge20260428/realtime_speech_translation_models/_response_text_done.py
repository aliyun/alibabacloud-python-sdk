# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ResponseTextDone(DaraModel):
    def __init__(
        self,
        type: str = None,
        event_id: str = None,
        response_id: str = None,
        item_id: str = None,
        output_index: int = None,
        content_index: int = None,
        text: str = None,
    ):
        self.type = type
        self.event_id = event_id
        self.response_id = response_id
        self.item_id = item_id
        self.output_index = output_index
        self.content_index = content_index
        self.text = text

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

        if self.response_id is not None:
            result['response_id'] = self.response_id

        if self.item_id is not None:
            result['item_id'] = self.item_id

        if self.output_index is not None:
            result['output_index'] = self.output_index

        if self.content_index is not None:
            result['content_index'] = self.content_index

        if self.text is not None:
            result['text'] = self.text

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('event_id') is not None:
            self.event_id = m.get('event_id')

        if m.get('response_id') is not None:
            self.response_id = m.get('response_id')

        if m.get('item_id') is not None:
            self.item_id = m.get('item_id')

        if m.get('output_index') is not None:
            self.output_index = m.get('output_index')

        if m.get('content_index') is not None:
            self.content_index = m.get('content_index')

        if m.get('text') is not None:
            self.text = m.get('text')

        return self

