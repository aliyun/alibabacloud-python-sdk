# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_farui20240628 import models as main_models
from darabonba.model import DaraModel

class RunLegalAdviceConsultationRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        assistant: main_models.RunLegalAdviceConsultationRequestAssistant = None,
        extra: main_models.RunLegalAdviceConsultationRequestExtra = None,
        stream: bool = None,
        thread: main_models.RunLegalAdviceConsultationRequestThread = None,
    ):
        self.app_id = app_id
        self.assistant = assistant
        self.extra = extra
        self.stream = stream
        self.thread = thread

    def validate(self):
        if self.assistant:
            self.assistant.validate()
        if self.extra:
            self.extra.validate()
        if self.thread:
            self.thread.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['appId'] = self.app_id

        if self.assistant is not None:
            result['assistant'] = self.assistant.to_map()

        if self.extra is not None:
            result['extra'] = self.extra.to_map()

        if self.stream is not None:
            result['stream'] = self.stream

        if self.thread is not None:
            result['thread'] = self.thread.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appId') is not None:
            self.app_id = m.get('appId')

        if m.get('assistant') is not None:
            temp_model = main_models.RunLegalAdviceConsultationRequestAssistant()
            self.assistant = temp_model.from_map(m.get('assistant'))

        if m.get('extra') is not None:
            temp_model = main_models.RunLegalAdviceConsultationRequestExtra()
            self.extra = temp_model.from_map(m.get('extra'))

        if m.get('stream') is not None:
            self.stream = m.get('stream')

        if m.get('thread') is not None:
            temp_model = main_models.RunLegalAdviceConsultationRequestThread()
            self.thread = temp_model.from_map(m.get('thread'))

        return self

class RunLegalAdviceConsultationRequestThread(DaraModel):
    def __init__(
        self,
        messages: List[main_models.RunLegalAdviceConsultationRequestThreadMessages] = None,
    ):
        self.messages = messages

    def validate(self):
        if self.messages:
            for v1 in self.messages:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['messages'] = []
        if self.messages is not None:
            for k1 in self.messages:
                result['messages'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.messages = []
        if m.get('messages') is not None:
            for k1 in m.get('messages'):
                temp_model = main_models.RunLegalAdviceConsultationRequestThreadMessages()
                self.messages.append(temp_model.from_map(k1))

        return self

class RunLegalAdviceConsultationRequestThreadMessages(DaraModel):
    def __init__(
        self,
        content: str = None,
        role: str = None,
    ):
        self.content = content
        self.role = role

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['content'] = self.content

        if self.role is not None:
            result['role'] = self.role

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')

        if m.get('role') is not None:
            self.role = m.get('role')

        return self

class RunLegalAdviceConsultationRequestExtra(DaraModel):
    def __init__(
        self,
        deep_think: bool = None,
        online_search: bool = None,
    ):
        self.deep_think = deep_think
        self.online_search = online_search

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.deep_think is not None:
            result['deepThink'] = self.deep_think

        if self.online_search is not None:
            result['onlineSearch'] = self.online_search

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('deepThink') is not None:
            self.deep_think = m.get('deepThink')

        if m.get('onlineSearch') is not None:
            self.online_search = m.get('onlineSearch')

        return self

class RunLegalAdviceConsultationRequestAssistant(DaraModel):
    def __init__(
        self,
        id: str = None,
        meta_data: Dict[str, str] = None,
        type: str = None,
        version: str = None,
    ):
        self.id = id
        self.meta_data = meta_data
        self.type = type
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['id'] = self.id

        if self.meta_data is not None:
            result['metaData'] = self.meta_data

        if self.type is not None:
            result['type'] = self.type

        if self.version is not None:
            result['version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('metaData') is not None:
            self.meta_data = m.get('metaData')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('version') is not None:
            self.version = m.get('version')

        return self

