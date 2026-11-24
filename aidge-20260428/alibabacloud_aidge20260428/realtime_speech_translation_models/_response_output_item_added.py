# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aidge20260428 import realtime_speech_translation_models as main_models
from darabonba.model import DaraModel

class ResponseOutputItemAdded(DaraModel):
    def __init__(
        self,
        type: str = None,
        event_id: str = None,
        response_id: str = None,
        output_index: int = None,
        item: main_models.ResponseOutputItemAddedItem = None,
    ):
        self.type = type
        self.event_id = event_id
        self.response_id = response_id
        self.output_index = output_index
        self.item = item

    def validate(self):
        if self.item:
            self.item.validate()

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

        if self.output_index is not None:
            result['output_index'] = self.output_index

        if self.item is not None:
            result['item'] = self.item.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('event_id') is not None:
            self.event_id = m.get('event_id')

        if m.get('response_id') is not None:
            self.response_id = m.get('response_id')

        if m.get('output_index') is not None:
            self.output_index = m.get('output_index')

        if m.get('item') is not None:
            temp_model = main_models.ResponseOutputItemAddedItem()
            self.item = temp_model.from_map(m.get('item'))

        return self

class ResponseOutputItemAddedItem(DaraModel):
    def __init__(
        self,
        id: str = None,
        object: str = None,
        type: str = None,
        status: str = None,
        role: str = None,
        content: List[main_models.ResponseOutputItemAddedItemContent] = None,
    ):
        self.id = id
        self.object = object
        self.type = type
        self.status = status
        self.role = role
        self.content = content

    def validate(self):
        if self.content:
            for v1 in self.content:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['id'] = self.id

        if self.object is not None:
            result['object'] = self.object

        if self.type is not None:
            result['type'] = self.type

        if self.status is not None:
            result['status'] = self.status

        if self.role is not None:
            result['role'] = self.role

        result['content'] = []
        if self.content is not None:
            for k1 in self.content:
                result['content'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('object') is not None:
            self.object = m.get('object')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('role') is not None:
            self.role = m.get('role')

        self.content = []
        if m.get('content') is not None:
            for k1 in m.get('content'):
                temp_model = main_models.ResponseOutputItemAddedItemContent()
                self.content.append(temp_model.from_map(k1))

        return self

class ResponseOutputItemAddedItemContent(DaraModel):
    def __init__(
        self,
        type: str = None,
        text: str = None,
        transcript: str = None,
    ):
        self.type = type
        self.text = text
        self.transcript = transcript

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.type is not None:
            result['type'] = self.type

        if self.text is not None:
            result['text'] = self.text

        if self.transcript is not None:
            result['transcript'] = self.transcript

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('text') is not None:
            self.text = m.get('text')

        if m.get('transcript') is not None:
            self.transcript = m.get('transcript')

        return self

