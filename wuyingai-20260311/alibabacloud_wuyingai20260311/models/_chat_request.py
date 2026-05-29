# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_wuyingai20260311 import models as main_models
from darabonba.model import DaraModel

class ChatRequest(DaraModel):
    def __init__(
        self,
        authorization: str = None,
        external_user_id: str = None,
        input: List[main_models.ChatRequestInput] = None,
        routing_key: str = None,
        session_id: str = None,
        settings: main_models.ChatRequestSettings = None,
        stream_options: main_models.ChatRequestStreamOptions = None,
        template_id: str = None,
    ):
        self.authorization = authorization
        self.external_user_id = external_user_id
        self.input = input
        self.routing_key = routing_key
        self.session_id = session_id
        self.settings = settings
        self.stream_options = stream_options
        self.template_id = template_id

    def validate(self):
        if self.input:
            for v1 in self.input:
                 if v1:
                    v1.validate()
        if self.settings:
            self.settings.validate()
        if self.stream_options:
            self.stream_options.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.authorization is not None:
            result['Authorization'] = self.authorization

        if self.external_user_id is not None:
            result['ExternalUserId'] = self.external_user_id

        result['Input'] = []
        if self.input is not None:
            for k1 in self.input:
                result['Input'].append(k1.to_map() if k1 else None)

        if self.routing_key is not None:
            result['RoutingKey'] = self.routing_key

        if self.session_id is not None:
            result['SessionId'] = self.session_id

        if self.settings is not None:
            result['Settings'] = self.settings.to_map()

        if self.stream_options is not None:
            result['StreamOptions'] = self.stream_options.to_map()

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')

        if m.get('ExternalUserId') is not None:
            self.external_user_id = m.get('ExternalUserId')

        self.input = []
        if m.get('Input') is not None:
            for k1 in m.get('Input'):
                temp_model = main_models.ChatRequestInput()
                self.input.append(temp_model.from_map(k1))

        if m.get('RoutingKey') is not None:
            self.routing_key = m.get('RoutingKey')

        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        if m.get('Settings') is not None:
            temp_model = main_models.ChatRequestSettings()
            self.settings = temp_model.from_map(m.get('Settings'))

        if m.get('StreamOptions') is not None:
            temp_model = main_models.ChatRequestStreamOptions()
            self.stream_options = temp_model.from_map(m.get('StreamOptions'))

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        return self

class ChatRequestStreamOptions(DaraModel):
    def __init__(
        self,
        include_reasoning: bool = None,
        include_tool_calls: bool = None,
    ):
        self.include_reasoning = include_reasoning
        self.include_tool_calls = include_tool_calls

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.include_reasoning is not None:
            result['IncludeReasoning'] = self.include_reasoning

        if self.include_tool_calls is not None:
            result['IncludeToolCalls'] = self.include_tool_calls

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IncludeReasoning') is not None:
            self.include_reasoning = m.get('IncludeReasoning')

        if m.get('IncludeToolCalls') is not None:
            self.include_tool_calls = m.get('IncludeToolCalls')

        return self

class ChatRequestSettings(DaraModel):
    def __init__(
        self,
        output_file_mode: str = None,
    ):
        self.output_file_mode = output_file_mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.output_file_mode is not None:
            result['OutputFileMode'] = self.output_file_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OutputFileMode') is not None:
            self.output_file_mode = m.get('OutputFileMode')

        return self

class ChatRequestInput(DaraModel):
    def __init__(
        self,
        content: List[main_models.ChatRequestInputContent] = None,
        role: str = None,
    ):
        self.content = content
        self.role = role

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
        result['Content'] = []
        if self.content is not None:
            for k1 in self.content:
                result['Content'].append(k1.to_map() if k1 else None)

        if self.role is not None:
            result['Role'] = self.role

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.content = []
        if m.get('Content') is not None:
            for k1 in m.get('Content'):
                temp_model = main_models.ChatRequestInputContent()
                self.content.append(temp_model.from_map(k1))

        if m.get('Role') is not None:
            self.role = m.get('Role')

        return self



class ChatRequestInputContent(DaraModel):
    def __init__(
        self,
        file_url: str = None,
        image_url: str = None,
        text: str = None,
        type: str = None,
    ):
        self.file_url = file_url
        self.image_url = image_url
        self.text = text
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_url is not None:
            result['FileUrl'] = self.file_url

        if self.image_url is not None:
            result['ImageUrl'] = self.image_url

        if self.text is not None:
            result['Text'] = self.text

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')

        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')

        if m.get('Text') is not None:
            self.text = m.get('Text')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

