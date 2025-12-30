# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any, List

from alibabacloud_dianjin20240628 import models as main_models
from darabonba.model import DaraModel

class RunChatResultGenerationRequest(DaraModel):
    def __init__(
        self,
        inference_parameters: Dict[str, Any] = None,
        messages: List[main_models.RunChatResultGenerationRequestMessages] = None,
        model_id: str = None,
        session_id: str = None,
        stream: bool = None,
        tools: List[main_models.RunChatResultGenerationRequestTools] = None,
    ):
        self.inference_parameters = inference_parameters
        # This parameter is required.
        self.messages = messages
        # This parameter is required.
        self.model_id = model_id
        self.session_id = session_id
        self.stream = stream
        self.tools = tools

    def validate(self):
        if self.messages:
            for v1 in self.messages:
                 if v1:
                    v1.validate()
        if self.tools:
            for v1 in self.tools:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.inference_parameters is not None:
            result['inferenceParameters'] = self.inference_parameters

        result['messages'] = []
        if self.messages is not None:
            for k1 in self.messages:
                result['messages'].append(k1.to_map() if k1 else None)

        if self.model_id is not None:
            result['modelId'] = self.model_id

        if self.session_id is not None:
            result['sessionId'] = self.session_id

        if self.stream is not None:
            result['stream'] = self.stream

        result['tools'] = []
        if self.tools is not None:
            for k1 in self.tools:
                result['tools'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('inferenceParameters') is not None:
            self.inference_parameters = m.get('inferenceParameters')

        self.messages = []
        if m.get('messages') is not None:
            for k1 in m.get('messages'):
                temp_model = main_models.RunChatResultGenerationRequestMessages()
                self.messages.append(temp_model.from_map(k1))

        if m.get('modelId') is not None:
            self.model_id = m.get('modelId')

        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')

        if m.get('stream') is not None:
            self.stream = m.get('stream')

        self.tools = []
        if m.get('tools') is not None:
            for k1 in m.get('tools'):
                temp_model = main_models.RunChatResultGenerationRequestTools()
                self.tools.append(temp_model.from_map(k1))

        return self

class RunChatResultGenerationRequestTools(DaraModel):
    def __init__(
        self,
        function: main_models.RunChatResultGenerationRequestToolsFunction = None,
        type: str = None,
    ):
        self.function = function
        self.type = type

    def validate(self):
        if self.function:
            self.function.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.function is not None:
            result['function'] = self.function.to_map()

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('function') is not None:
            temp_model = main_models.RunChatResultGenerationRequestToolsFunction()
            self.function = temp_model.from_map(m.get('function'))

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class RunChatResultGenerationRequestToolsFunction(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        parameters: main_models.RunChatResultGenerationRequestToolsFunctionParameters = None,
        required: List[str] = None,
    ):
        self.description = description
        self.name = name
        self.parameters = parameters
        self.required = required

    def validate(self):
        if self.parameters:
            self.parameters.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['description'] = self.description

        if self.name is not None:
            result['name'] = self.name

        if self.parameters is not None:
            result['parameters'] = self.parameters.to_map()

        if self.required is not None:
            result['required'] = self.required

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('parameters') is not None:
            temp_model = main_models.RunChatResultGenerationRequestToolsFunctionParameters()
            self.parameters = temp_model.from_map(m.get('parameters'))

        if m.get('required') is not None:
            self.required = m.get('required')

        return self

class RunChatResultGenerationRequestToolsFunctionParameters(DaraModel):
    def __init__(
        self,
        properties: Dict[str, Any] = None,
        type: str = None,
    ):
        self.properties = properties
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.properties is not None:
            result['properties'] = self.properties

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('properties') is not None:
            self.properties = m.get('properties')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class RunChatResultGenerationRequestMessages(DaraModel):
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

