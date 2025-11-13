# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_farui20240628 import models as main_models
from darabonba.model import DaraModel

class RunContractRuleGenerationRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        assistant: main_models.RunContractRuleGenerationRequestAssistant = None,
        stream: bool = None,
    ):
        self.app_id = app_id
        self.assistant = assistant
        self.stream = stream

    def validate(self):
        if self.assistant:
            self.assistant.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['appId'] = self.app_id

        if self.assistant is not None:
            result['assistant'] = self.assistant.to_map()

        if self.stream is not None:
            result['stream'] = self.stream

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appId') is not None:
            self.app_id = m.get('appId')

        if m.get('assistant') is not None:
            temp_model = main_models.RunContractRuleGenerationRequestAssistant()
            self.assistant = temp_model.from_map(m.get('assistant'))

        if m.get('stream') is not None:
            self.stream = m.get('stream')

        return self

class RunContractRuleGenerationRequestAssistant(DaraModel):
    def __init__(
        self,
        meta_data: main_models.RunContractRuleGenerationRequestAssistantMetaData = None,
        type: str = None,
        version: str = None,
    ):
        self.meta_data = meta_data
        self.type = type
        self.version = version

    def validate(self):
        if self.meta_data:
            self.meta_data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.meta_data is not None:
            result['metaData'] = self.meta_data.to_map()

        if self.type is not None:
            result['type'] = self.type

        if self.version is not None:
            result['version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('metaData') is not None:
            temp_model = main_models.RunContractRuleGenerationRequestAssistantMetaData()
            self.meta_data = temp_model.from_map(m.get('metaData'))

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('version') is not None:
            self.version = m.get('version')

        return self

class RunContractRuleGenerationRequestAssistantMetaData(DaraModel):
    def __init__(
        self,
        file_id: str = None,
        position: str = None,
    ):
        self.file_id = file_id
        self.position = position

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_id is not None:
            result['fileId'] = self.file_id

        if self.position is not None:
            result['position'] = self.position

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fileId') is not None:
            self.file_id = m.get('fileId')

        if m.get('position') is not None:
            self.position = m.get('position')

        return self

