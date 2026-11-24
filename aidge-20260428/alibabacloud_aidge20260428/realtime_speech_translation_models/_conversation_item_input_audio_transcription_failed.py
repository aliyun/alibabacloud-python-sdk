# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_aidge20260428 import realtime_speech_translation_models as main_models
from darabonba.model import DaraModel

class ConversationItemInputAudioTranscriptionFailed(DaraModel):
    def __init__(
        self,
        type: str = None,
        event_id: str = None,
        item_id: str = None,
        content_index: int = None,
        error: main_models.ConversationItemInputAudioTranscriptionFailedError = None,
    ):
        self.type = type
        self.event_id = event_id
        self.item_id = item_id
        self.content_index = content_index
        self.error = error

    def validate(self):
        if self.error:
            self.error.validate()

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

        if self.error is not None:
            result['error'] = self.error.to_map()

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

        if m.get('error') is not None:
            temp_model = main_models.ConversationItemInputAudioTranscriptionFailedError()
            self.error = temp_model.from_map(m.get('error'))

        return self

class ConversationItemInputAudioTranscriptionFailedError(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        param: str = None,
    ):
        self.code = code
        self.message = message
        self.param = param

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.message is not None:
            result['message'] = self.message

        if self.param is not None:
            result['param'] = self.param

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('param') is not None:
            self.param = m.get('param')

        return self

