# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_agentcore20260804 import models as main_models
from darabonba.model import DaraModel

class CreateModelRequest(DaraModel):
    def __init__(
        self,
        body: main_models.CreateModelRequestBody = None,
        client_token: str = None,
    ):
        # The request body.
        self.body = body
        # The client token for idempotence. Not currently supported.
        self.client_token = client_token

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.body is not None:
            result['body'] = self.body.to_map()

        if self.client_token is not None:
            result['clientToken'] = self.client_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = main_models.CreateModelRequestBody()
            self.body = temp_model.from_map(m.get('body'))

        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')

        return self

class CreateModelRequestBody(DaraModel):
    def __init__(
        self,
        capabilities: main_models.CreateModelRequestBodyCapabilities = None,
        connection_id: str = None,
        context_size: int = None,
        description: str = None,
        max_tokens: int = None,
        model_name: str = None,
    ):
        # The model capability configuration.
        self.capabilities = capabilities
        # The model connection ID.
        # 
        # This parameter is required.
        self.connection_id = connection_id
        # The model context window size, in tokens. The value must be a positive integer.
        self.context_size = context_size
        # The model description. Maximum length: 255 characters.
        self.description = description
        # The maximum number of output tokens supported per model generation.
        self.max_tokens = max_tokens
        # The upstream model name.
        # 
        # This parameter is required.
        self.model_name = model_name

    def validate(self):
        if self.capabilities:
            self.capabilities.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.capabilities is not None:
            result['capabilities'] = self.capabilities.to_map()

        if self.connection_id is not None:
            result['connectionId'] = self.connection_id

        if self.context_size is not None:
            result['contextSize'] = self.context_size

        if self.description is not None:
            result['description'] = self.description

        if self.max_tokens is not None:
            result['maxTokens'] = self.max_tokens

        if self.model_name is not None:
            result['modelName'] = self.model_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('capabilities') is not None:
            temp_model = main_models.CreateModelRequestBodyCapabilities()
            self.capabilities = temp_model.from_map(m.get('capabilities'))

        if m.get('connectionId') is not None:
            self.connection_id = m.get('connectionId')

        if m.get('contextSize') is not None:
            self.context_size = m.get('contextSize')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('maxTokens') is not None:
            self.max_tokens = m.get('maxTokens')

        if m.get('modelName') is not None:
            self.model_name = m.get('modelName')

        return self

class CreateModelRequestBodyCapabilities(DaraModel):
    def __init__(
        self,
        audio: bool = None,
        document: bool = None,
        multi_tool_call: bool = None,
        reasoning: bool = None,
        stream_tool_call: bool = None,
        tool_call: bool = None,
        video: bool = None,
        vision: bool = None,
    ):
        # Specifies whether the model supports audio input or output.
        self.audio = audio
        # Specifies whether the model supports document input.
        self.document = document
        # Specifies whether the model is able to invoke multiple tools in a single response.
        self.multi_tool_call = multi_tool_call
        # Specifies whether the model supports reasoning capabilities.
        self.reasoning = reasoning
        # Specifies whether the model supports streaming tool calling.
        self.stream_tool_call = stream_tool_call
        # Specifies whether the model supports tool calling.
        self.tool_call = tool_call
        # Specifies whether the model supports video input.
        self.video = video
        # Specifies whether the model supports image input.
        self.vision = vision

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.audio is not None:
            result['audio'] = self.audio

        if self.document is not None:
            result['document'] = self.document

        if self.multi_tool_call is not None:
            result['multiToolCall'] = self.multi_tool_call

        if self.reasoning is not None:
            result['reasoning'] = self.reasoning

        if self.stream_tool_call is not None:
            result['streamToolCall'] = self.stream_tool_call

        if self.tool_call is not None:
            result['toolCall'] = self.tool_call

        if self.video is not None:
            result['video'] = self.video

        if self.vision is not None:
            result['vision'] = self.vision

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('audio') is not None:
            self.audio = m.get('audio')

        if m.get('document') is not None:
            self.document = m.get('document')

        if m.get('multiToolCall') is not None:
            self.multi_tool_call = m.get('multiToolCall')

        if m.get('reasoning') is not None:
            self.reasoning = m.get('reasoning')

        if m.get('streamToolCall') is not None:
            self.stream_tool_call = m.get('streamToolCall')

        if m.get('toolCall') is not None:
            self.tool_call = m.get('toolCall')

        if m.get('video') is not None:
            self.video = m.get('video')

        if m.get('vision') is not None:
            self.vision = m.get('vision')

        return self

