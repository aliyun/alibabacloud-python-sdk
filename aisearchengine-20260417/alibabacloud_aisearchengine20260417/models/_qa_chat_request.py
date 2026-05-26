# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any, List

from alibabacloud_aisearchengine20260417 import models as main_models
from darabonba.model import DaraModel

class QaChatRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        message: main_models.QaChatRequestMessage = None,
        options: Dict[str, Any] = None,
        session_id: str = None,
    ):
        # This parameter is required.
        self.app_id = app_id
        # This parameter is required.
        self.message = message
        self.options = options
        self.session_id = session_id

    def validate(self):
        if self.message:
            self.message.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['appId'] = self.app_id

        if self.message is not None:
            result['message'] = self.message.to_map()

        if self.options is not None:
            result['options'] = self.options

        if self.session_id is not None:
            result['sessionId'] = self.session_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appId') is not None:
            self.app_id = m.get('appId')

        if m.get('message') is not None:
            temp_model = main_models.QaChatRequestMessage()
            self.message = temp_model.from_map(m.get('message'))

        if m.get('options') is not None:
            self.options = m.get('options')

        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')

        return self

class QaChatRequestMessage(DaraModel):
    def __init__(
        self,
        parts: List[main_models.QaChatRequestMessageParts] = None,
        role: str = None,
    ):
        self.parts = parts
        self.role = role

    def validate(self):
        if self.parts:
            for v1 in self.parts:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['parts'] = []
        if self.parts is not None:
            for k1 in self.parts:
                result['parts'].append(k1.to_map() if k1 else None)

        if self.role is not None:
            result['role'] = self.role

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.parts = []
        if m.get('parts') is not None:
            for k1 in m.get('parts'):
                temp_model = main_models.QaChatRequestMessageParts()
                self.parts.append(temp_model.from_map(k1))

        if m.get('role') is not None:
            self.role = m.get('role')

        return self

class QaChatRequestMessageParts(DaraModel):
    def __init__(
        self,
        data: Any = None,
        media_type: str = None,
        text: str = None,
        type: str = None,
        url: str = None,
    ):
        self.data = data
        self.media_type = media_type
        self.text = text
        self.type = type
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['data'] = self.data

        if self.media_type is not None:
            result['mediaType'] = self.media_type

        if self.text is not None:
            result['text'] = self.text

        if self.type is not None:
            result['type'] = self.type

        if self.url is not None:
            result['url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            self.data = m.get('data')

        if m.get('mediaType') is not None:
            self.media_type = m.get('mediaType')

        if m.get('text') is not None:
            self.text = m.get('text')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('url') is not None:
            self.url = m.get('url')

        return self

