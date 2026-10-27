# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_maasqiservice20260831 import models as main_models
from darabonba.model import DaraModel

class CuaChatCompletionStreamRequest(DaraModel):
    def __init__(
        self,
        messages: List[main_models.CuaChatCompletionStreamRequestMessages] = None,
        metadata: main_models.CuaChatCompletionStreamRequestMetadata = None,
        model: str = None,
        stream: bool = None,
        stream_options: main_models.CuaChatCompletionStreamRequestStreamOptions = None,
        tools: List[Dict[str, Any]] = None,
    ):
        # This parameter is required.
        self.messages = messages
        self.metadata = metadata
        self.model = model
        # This parameter is required.
        self.stream = stream
        self.stream_options = stream_options
        self.tools = tools

    def validate(self):
        if self.messages:
            for v1 in self.messages:
                 if v1:
                    v1.validate()
        if self.metadata:
            self.metadata.validate()
        if self.stream_options:
            self.stream_options.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['messages'] = []
        if self.messages is not None:
            for k1 in self.messages:
                result['messages'].append(k1.to_map() if k1 else None)

        if self.metadata is not None:
            result['metadata'] = self.metadata.to_map()

        if self.model is not None:
            result['model'] = self.model

        if self.stream is not None:
            result['stream'] = self.stream

        if self.stream_options is not None:
            result['streamOptions'] = self.stream_options.to_map()

        if self.tools is not None:
            result['tools'] = self.tools

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.messages = []
        if m.get('messages') is not None:
            for k1 in m.get('messages'):
                temp_model = main_models.CuaChatCompletionStreamRequestMessages()
                self.messages.append(temp_model.from_map(k1))

        if m.get('metadata') is not None:
            temp_model = main_models.CuaChatCompletionStreamRequestMetadata()
            self.metadata = temp_model.from_map(m.get('metadata'))

        if m.get('model') is not None:
            self.model = m.get('model')

        if m.get('stream') is not None:
            self.stream = m.get('stream')

        if m.get('streamOptions') is not None:
            temp_model = main_models.CuaChatCompletionStreamRequestStreamOptions()
            self.stream_options = temp_model.from_map(m.get('streamOptions'))

        if m.get('tools') is not None:
            self.tools = m.get('tools')

        return self

class CuaChatCompletionStreamRequestStreamOptions(DaraModel):
    def __init__(
        self,
        include_usage: bool = None,
    ):
        self.include_usage = include_usage

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.include_usage is not None:
            result['includeUsage'] = self.include_usage

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('includeUsage') is not None:
            self.include_usage = m.get('includeUsage')

        return self

class CuaChatCompletionStreamRequestMetadata(DaraModel):
    def __init__(
        self,
        screen_height: int = None,
        screen_width: int = None,
    ):
        self.screen_height = screen_height
        self.screen_width = screen_width

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.screen_height is not None:
            result['screenHeight'] = self.screen_height

        if self.screen_width is not None:
            result['screenWidth'] = self.screen_width

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('screenHeight') is not None:
            self.screen_height = m.get('screenHeight')

        if m.get('screenWidth') is not None:
            self.screen_width = m.get('screenWidth')

        return self

class CuaChatCompletionStreamRequestMessages(DaraModel):
    def __init__(
        self,
        content: List[main_models.CuaChatCompletionStreamRequestMessagesContent] = None,
        role: str = None,
        tool_call_id: str = None,
    ):
        # This parameter is required.
        self.content = content
        # This parameter is required.
        self.role = role
        self.tool_call_id = tool_call_id

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
        result['content'] = []
        if self.content is not None:
            for k1 in self.content:
                result['content'].append(k1.to_map() if k1 else None)

        if self.role is not None:
            result['role'] = self.role

        if self.tool_call_id is not None:
            result['toolCallId'] = self.tool_call_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.content = []
        if m.get('content') is not None:
            for k1 in m.get('content'):
                temp_model = main_models.CuaChatCompletionStreamRequestMessagesContent()
                self.content.append(temp_model.from_map(k1))

        if m.get('role') is not None:
            self.role = m.get('role')

        if m.get('toolCallId') is not None:
            self.tool_call_id = m.get('toolCallId')

        return self

class CuaChatCompletionStreamRequestMessagesContent(DaraModel):
    def __init__(
        self,
        image_data: str = None,
        image_url: main_models.CuaChatCompletionStreamRequestMessagesContentImageUrl = None,
        text: str = None,
        type: str = None,
    ):
        self.image_data = image_data
        self.image_url = image_url
        self.text = text
        # This parameter is required.
        self.type = type

    def validate(self):
        if self.image_url:
            self.image_url.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.image_data is not None:
            result['imageData'] = self.image_data

        if self.image_url is not None:
            result['imageUrl'] = self.image_url.to_map()

        if self.text is not None:
            result['text'] = self.text

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('imageData') is not None:
            self.image_data = m.get('imageData')

        if m.get('imageUrl') is not None:
            temp_model = main_models.CuaChatCompletionStreamRequestMessagesContentImageUrl()
            self.image_url = temp_model.from_map(m.get('imageUrl'))

        if m.get('text') is not None:
            self.text = m.get('text')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class CuaChatCompletionStreamRequestMessagesContentImageUrl(DaraModel):
    def __init__(
        self,
        url: str = None,
    ):
        # This parameter is required.
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.url is not None:
            result['url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('url') is not None:
            self.url = m.get('url')

        return self

